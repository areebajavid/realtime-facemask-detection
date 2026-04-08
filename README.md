<div align="center">
  
# 😷 Real-Time Face Mask Detection System

### *Deep Learning based COVID-19 Safety Compliance System*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-2.4+-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-96%25-success?style=for-the-badge)]()

</div>

---

## 🎯 Project Overview

> **A production-ready face mask detection system achieving 96% accuracy using VGG16 transfer learning and CNN architecture.**

This system processes real-time video feeds to identify individuals wearing masks or not, making it suitable for:
- 🏢 **Office & Workplace Security**
- 🏫 **Educational Institutions**  
- 🏥 **Healthcare Facilities**
- 🚇 **Public Transportation Hubs**

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **96% Accuracy** | State-of-the-art detection performance |
| ⚡ **Real-Time Processing** | Processes video frames at 30+ FPS |
| 🖼️ **Multi-Face Detection** | Detects multiple faces simultaneously |
| 📹 **Live & Static Input** | Supports webcam, video files, and images |
| 🧠 **Transfer Learning** | Leverages VGG16 architecture |

## 🏗️ Architecture

## 📊 Model Performance

```python
{
    "accuracy": "96%",
    "precision": "0.95",
    "recall": "0.94", 
    "f1_score": "0.945",
    "inference_time": "25ms per frame"
}
Python 3.8+
pip install -r requirements.txt
# Clone the repository
git clone https://github.com/areebajavid/realtime-facemask-detection.git

# Navigate to project
cd realtime-facemask-detection

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
realtime-facemask-detection/
│
├── app.py                    # Main application entry point
├── mask_detector.py          # CNN model training & inference
├── index.html                # Web interface
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
│
├── dataset/                  # Training data
│   ├── with_mask/
│   └── without_mask/
│
├── model/                    # Saved model weights
│   └── mask_detector.h5
│
└── utils/                    # Helper functions
    └── face_utils.py
