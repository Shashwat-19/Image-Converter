from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import cv2
import zipfile
from PIL import Image
import io
import uuid
from datetime import datetime
import shutil

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CONVERTED_FOLDER'] = 'converted'
app.secret_key = 'your-secret-key-here'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_image_info(filepath):
    """Get image dimensions and file size"""
    try:
        with Image.open(filepath) as img:
            return {
                'width': img.width,
                'height': img.height,
                'format': img.format,
                'size': os.path.getsize(filepath)
            }
    except Exception as e:
        return None


def convert_image(input_path, output_path, target_format, quality=95):
    """Convert image to target format using OpenCV and PIL"""
    try:
        if target_format.lower() == 'webp':
            # Use PIL for WebP conversion
            with Image.open(input_path) as img:
                # Convert RGBA to RGB if saving as JPEG
                if target_format.lower() == 'jpeg' and img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(output_path, format=target_format.upper(), quality=quality, optimize=True)
        else:
            # Use OpenCV for other formats
            img = cv2.imread(input_path)
            if img is None:
                # Fallback to PIL
                with Image.open(input_path) as pil_img:
                    if target_format.lower() == 'jpeg' and pil_img.mode == 'RGBA':
                        pil_img = pil_img.convert('RGB')
                    pil_img.save(output_path, format=target_format.upper(), quality=quality)
            else:
                if target_format.lower() == 'jpeg':
                    cv2.imwrite(output_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
                elif target_format.lower() == 'png':
                    cv2.imwrite(output_path, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                else:
                    cv2.imwrite(output_path, img)
        return True
    except Exception as e:
        print(f"Error converting image: {e}")
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400

    files = request.files.getlist('files')
    target_format = request.form.get('format', 'jpeg').lower()
    quality = int(request.form.get('quality', 95))

    if not files or all(file.filename == '' for file in files):
        return jsonify({'error': 'No files selected'}), 400

    # Create unique session folder
    session_id = str(uuid.uuid4())
    session_folder = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    converted_folder = os.path.join(app.config['CONVERTED_FOLDER'], session_id)
    os.makedirs(session_folder, exist_ok=True)
    os.makedirs(converted_folder, exist_ok=True)

    uploaded_files = []
    converted_files = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"

            # Save uploaded file
            upload_path = os.path.join(session_folder, unique_filename)
            file.save(upload_path)

            # Get image info
            img_info = get_image_info(upload_path)
            if img_info:
                uploaded_files.append({
                    'original_name': filename,
                    'unique_name': unique_filename,
                    'info': img_info
                })

                # Convert image
                base_name = os.path.splitext(unique_filename)[0]
                converted_name = f"{base_name}_converted.{target_format}"
                converted_path = os.path.join(converted_folder, converted_name)

                if convert_image(upload_path, converted_path, target_format, quality):
                    converted_info = get_image_info(converted_path)
                    converted_files.append({
                        'name': converted_name,
                        'original_name': filename,
                        'info': converted_info
                    })

    if not converted_files:
        return jsonify({'error': 'No files could be converted'}), 400

    return jsonify({
        'session_id': session_id,
        'uploaded_files': uploaded_files,
        'converted_files': converted_files,
        'total_files': len(converted_files)
    })


@app.route('/download/<session_id>')
def download_converted(session_id):
    converted_folder = os.path.join(app.config['CONVERTED_FOLDER'], session_id)

    if not os.path.exists(converted_folder):
        return jsonify({'error': 'Session not found'}), 404

    files = os.listdir(converted_folder)
    if not files:
        return jsonify({'error': 'No converted files found'}), 404

    if len(files) == 1:
        # Single file download
        file_path = os.path.join(converted_folder, files[0])
        return send_file(file_path, as_attachment=True, download_name=files[0])
    else:
        # Multiple files - create zip
        zip_path = os.path.join(app.config['CONVERTED_FOLDER'], f"{session_id}_converted.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                file_path = os.path.join(converted_folder, file)
                zipf.write(file_path, file)

        return send_file(zip_path, as_attachment=True, download_name="converted_images.zip")


@app.route('/preview/<session_id>/<filename>')
def preview_image(session_id, filename):
    """Serve preview images"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], session_id, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    return jsonify({'error': 'File not found'}), 404


@app.route('/cleanup/<session_id>', methods=['POST'])
def cleanup_session(session_id):
    """Clean up session files"""
    try:
        upload_folder = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
        converted_folder = os.path.join(app.config['CONVERTED_FOLDER'], session_id)

        if os.path.exists(upload_folder):
            shutil.rmtree(upload_folder)
        if os.path.exists(converted_folder):
            shutil.rmtree(converted_folder)

        # Also clean up zip file if it exists
        zip_path = os.path.join(app.config['CONVERTED_FOLDER'], f"{session_id}_converted.zip")
        if os.path.exists(zip_path):
            os.remove(zip_path)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)