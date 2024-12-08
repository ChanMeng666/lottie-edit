<div align="center">
 <h1> Lottie Theme Converter</h1>
 <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=normal"/>
 <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=normal"/>
 <img src="https://img.shields.io/badge/pillow-11.0.0-orange?style=normal"/>
</div>
<br/>

# Features
A powerful Lottie animation theme converter that helps you easily switch between light and dark themes:

### ⚡ Color Inversion While Preserving Transparency
Smartly inverts colors of embedded images in Lottie files while maintaining alpha channel transparency.

### 🎨 Support for Both Light & Dark Themes  
Perfect for applications requiring both light and dark mode animations.

### 💻 Simple Python Implementation
Easy-to-understand Python script using only Pillow library for image processing.

### 🔄 Base64 Image Handling
Efficiently processes base64 encoded images embedded in Lottie JSON files.

## 🤔 How to Use
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Place your light theme Lottie animation file as "Animation-ClickMe.json"

3. Run the conversion script:
```python
python convert_lottie.py
```

4. Get your dark theme animation in "Animation-ClickMe-dark.json"

## Tech Used
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-%23000.svg?style=for-the-badge&logo=python&logoColor=white)

## Getting Started

First, install the required dependency:

```bash
pip install pillow==11.0.0
```

You can start converting your Lottie animation by following these steps:

1. Save your Lottie animation file as "Animation-ClickMe.json"
2. Run convert_lottie.py
3. The script will generate "Animation-ClickMe-dark.json" with inverted colors

## Learn More

The script processes embedded base64 images in the Lottie JSON file:
- Decodes base64 to image
- Inverts colors while preserving transparency 
- Re-encodes to base64
- Updates the Lottie JSON with new image data

Feel free to modify the code to work with different input/output filenames or add additional image processing features!
