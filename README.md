#  Image Converter

A professional Flask-based web application for seamless image format conversion with modern UI and powerful processing capabilities.

##  Overview

Image Converter is a user-friendly web application that allows you to:
- **Upload** images in various formats (JPG, PNG, WEBP, BMP, TIFF, etc.)
- **Convert** between different image formats with high quality
- **Download** converted images instantly

Perfect for photographers, designers, developers, and anyone who needs quick and reliable image format conversion.

## ✨ Features

-  **Multi-Format Support** - Convert between JPG, PNG, WEBP, BMP, TIFF, GIF and more
-  **Batch Processing** - Convert multiple images simultaneously
-  **Fast Processing** - Powered by OpenCV and Pillow for optimal performance
-  **Modern UI** - Clean, responsive interface that works on all devices
-  **Secure** - Files are processed locally and automatically cleaned up
-  **Quality Control** - Adjust compression and quality settings
-  **Mobile Friendly** - Responsive design for mobile and tablet devices
-  **No Registration** - Start converting immediately without sign-up

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Image Processing**: OpenCV, Pillow (PIL)
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug
- **Deployment**: Gunicorn, Docker (optional)

##  Quick Setup

### Prerequisites
- Python 3.8 or higher
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

5. **Open your browser**
   Navigate to `http://localhost:5000`

##  Usage

### Basic Image Conversion

1. **Upload Image**: Click "Choose File" or drag & drop your image
2. **Select Format**: Choose your desired output format (JPG, PNG, WEBP, etc.)
3. **Adjust Settings**: Optionally modify quality and compression settings
4. **Convert**: Click "Convert Image" to process
5. **Download**: Your converted image will be ready for download

### Batch Conversion

1. **Select Multiple Files**: Choose multiple images at once
2. **Set Output Format**: Pick the target format for all images
3. **Batch Convert**: Process all images simultaneously
4. **Download ZIP**: Get all converted images in a convenient ZIP file

### Supported Formats

| Input Formats | Output Formats |
|---------------|----------------|
| JPG/JPEG      | JPG/JPEG       |
| PNG           | PNG            |
| WEBP          | WEBP           |
| BMP           | BMP            |
| TIFF          | TIFF           |
| GIF           | GIF            |

##  Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```
3. **Deploy**
   ```bash
   git push heroku main
   ```

### Docker Deployment

1. **Build image**
   ```bash
   docker build -t image-converter .
   ```
2. **Run container**
   ```bash
   docker run -p 5000:5000 image-converter
   ```

### Manual Server Deployment

1. **Install dependencies**
2. **Configure Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. **Set up reverse proxy** (Nginx recommended)

##  Contributing

We welcome contributions! Here's how you can help:

### Development Setup

1. **Fork the repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make changes and test**
4. **Commit with clear message**
   ```bash
   git commit -m "Add: your feature description"
   ```
5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Areas for Contribution

-  Bug fixes and improvements
-  New image format support
-  UI/UX enhancements
-  Documentation improvements
-  Test coverage expansion
-  Performance optimizations

### Code Guidelines

- Follow PEP 8 for Python code
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Contact

- **Developer**: Shashwat
- **GitHub**: [@Shashwat-19](https://github.com/Shashwat-19)
- **Issues**: [Report bugs or request features](https://github.com/Shashwat-19/Image-Converter/issues)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!

Made with ❤️ for the developer community
