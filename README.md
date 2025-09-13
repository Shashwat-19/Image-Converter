# 🔄 Image Converter

A professional Flask-based web application for seamless image format conversion. Upload, convert, and download images with ease using a modern, intuitive interface.

## 🌟 Overview

Image Converter is a powerful yet simple web application that allows users to:
- **Upload** images in various formats (JPG, PNG, WEBP, BMP, TIFF, GIF)
- **Convert** between different image formats instantly
- **Download** converted images with customizable quality settings
- **Process** multiple images simultaneously with batch conversion

## ✨ Features

- 🖼️ **Multi-Format Support**: Convert between JPG, PNG, WEBP, BMP, TIFF, and GIF formats
- 📦 **Batch Processing**: Upload and convert multiple images at once
- ⚡ **Fast Processing**: Powered by OpenCV and Pillow for optimal performance
- 🎨 **Modern UI**: Clean, responsive interface with drag-and-drop functionality
- 🔒 **Secure**: File validation, size limits, and temporary file cleanup
- 📱 **Mobile-Friendly**: Works seamlessly on desktop and mobile devices
- 🎛️ **Quality Control**: Adjustable compression and quality settings
- 📊 **Progress Tracking**: Real-time conversion progress indicators

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Image Processing**: OpenCV, Pillow (PIL)
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug, os
- **Security**: File validation, CSRF protection

## 🚀 Quick Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shashwat-19/Image-Converter.git
   cd Image-Converter
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 Usage

### Basic Conversion
1. Visit the web application in your browser
2. Click "Choose Files" or drag and drop images
3. Select desired output format from the dropdown
4. Adjust quality settings if needed
5. Click "Convert" to process images
6. Download converted files individually or as a ZIP

### Batch Conversion
1. Select multiple images using Ctrl/Cmd + click
2. Choose output format for all images
3. Set global quality preferences
4. Convert all images with one click
5. Download as a compressed ZIP file

### Supported Formats
- **Input**: JPG, JPEG, PNG, WEBP, BMP, TIFF, GIF
- **Output**: JPG, PNG, WEBP, BMP, TIFF
- **Max file size**: 50MB per image
- **Max batch size**: 20 images

## ☁️ Deployment

### Local Development
```bash
export FLASK_ENV=development
python app.py
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Using Docker
```bash
# Build image
docker build -t image-converter .

# Run container
docker run -p 5000:5000 image-converter
```

#### Deploy to Heroku
```bash
heroku create your-app-name
git push heroku main
```

### Environment Variables
```bash
FLASK_ENV=production
MAX_FILE_SIZE=52428800  # 50MB
MAX_BATCH_SIZE=20
UPLOAD_FOLDER=uploads/
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add appropriate comments
   - Test your changes thoroughly
4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Guidelines
- Write clear, concise commit messages
- Include tests for new features
- Update documentation as needed
- Ensure backward compatibility

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Shashwat**
- GitHub: [@Shashwat-19](https://github.com/Shashwat-19)
- Email: [Contact via GitHub](https://github.com/Shashwat-19)

---

### 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Image processing powered by [OpenCV](https://opencv.org/) and [Pillow](https://pillow.readthedocs.io/)
- Icons from [Font Awesome](https://fontawesome.com/)

**⭐ Star this repository if you find it helpful!**
