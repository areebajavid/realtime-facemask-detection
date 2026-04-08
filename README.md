<div align="center">
  
# 😷 Real-Time Face Mask Detection System

### *Flask + TensorFlow + OpenCV Web Application*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.6.0-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=for-the-badge)]()

</div>

---

## 📌 Project Overview

> **A real-time face mask detection web application using a pre-trained Keras model, Flask backend, and OpenCV for webcam feed processing.**

This system captures live video from your webcam, processes each frame through a CNN model, and displays whether a mask is detected or not.

### What It Does:
- 🎥 Captures live webcam feed
- 🧠 Processes frames using a pre-trained `.h5` Keras model
- ✅ Displays "Mask" (green) or "No Mask" (red) label on video
- 🌐 Streams video to a web browser interface

---

## 🏗️ Architecture

┌─────────────────┐ Web Browser ┌─────────────────┐
│ Webcam (USB) │ ┌──────────────────► │ index.html │
│ Video Source │ │ │ (Frontend) │
└────────┬────────┘ │ └────────┬────────┘
│ │ │
▼ │ ▼
┌─────────────────┐ │ ┌─────────────────┐
│ OpenCV Capture │ │ │ Flask Server │
│ (cv2.VideoCapture)│◄──────────────────│ (app.py) │
└────────┬────────┘ │ HTTP GET │ Port 5000 │
│ │ /video_feed └────────┬────────┘
▼ │ │
┌─────────────────┐ │ │
│ Preprocessing │ │ │
│ Resize to │ │ │
│ 224x224 │ │ │
└────────┬────────┘ │ │
│ │ │
▼ │ ▼
┌─────────────────┐ │ ┌─────────────────┐
│ Keras Model │ │ │ mask_detector │
│ (mask_detector │ │ │ .py (Model │
│ .h5) │ │ │ Loading) │
└────────┬────────┘ │ └─────────────────┘
│ │
▼ │
┌─────────────────┐ │
│ Prediction: │ │
│ 0 = Mask │ │
│ 1 = No Mask │ │
└────────┬────────┘ │
│ │
▼ │
┌─────────────────┐ │
│ Draw Label │ │
│ Green/Red Box │ │
│ + Text │ │
└────────┬────────┘ │
│ │
▼ │
┌─────────────────┐ │
│ JPEG Encode │ │
│ & Stream to ├─┘
│ Browser │
└─────────────────┘



---

## ✨ Features (What Actually Exists)

| Feature | Implementation |
|---------|----------------|
| **Live Webcam Feed** | OpenCV `VideoCapture(0)` |
| **Face Mask Detection** | Pre-trained Keras model (`mask_detector.h5`) |
| **Real-time Streaming** | Flask streaming response (multipart/x-mixed-replace) |
| **Visual Feedback** | Green "Mask" label / Red "No Mask" label |
| **Web Interface** | `index.html` template |

---

## 📁 Project Structure (Actual)

realtime-facemask-detection/
│
├── app.py # Flask server & video feed route
├── mask_detector.py # Model loading + detection logic
├── index.html # Frontend web page (templates/)
├── requirements.txt # Python dependencies
├── README.md # Documentation
│
└── model/ # (Assumed - for .h5 file)
└── mask_detector.h5 # Pre-trained Keras weights


---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Webcam connected to your computer

Installation
# 1. Clone the repository
git clone https://github.com/areebajavid/realtime-facemask-detection.git
cd realtime-facemask-detection

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

Run the Application
# Start the Flask server
python app.py


🔧 Dependencies (From requirements.txt)
Package	Version
Flask	2.0.1
TensorFlow	2.6.0
opencv-python	4.5.3.56
numpy	1.19.5


🖥️ Usage Instructions
Run the server: python app.py

Open browser to http://localhost:5000

Allow camera permissions

Show your face to the webcam:

Wearing a mask → Green "Mask" label

No mask → Red "No Mask" label
