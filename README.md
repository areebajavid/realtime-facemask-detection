# 😷 Real-Time Face Mask Detection

> A real-time face mask detection web application using a pre-trained CNN model, Flask backend, and OpenCV webcam streaming.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)

---

## ✨ Features

- 🎥 **Live Webcam Feed** — Captures and processes frames in real-time via OpenCV
- 🧠 **CNN Model** — Pre-trained Keras `.h5` model for mask classification
- ✅ **Visual Feedback** — Green **"Mask"** / Red **"No Mask"** label overlay
- 🌐 **Browser Streaming** — Flask streams MJPEG video directly to the browser
- ⚡ **Zero Frontend Framework** — Lightweight vanilla HTML interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| ML Model | TensorFlow / Keras |
| Computer Vision | OpenCV |
| Streaming | Flask multipart streaming |
| Interface | HTML |

---

## 📁 Project Structure

```
realtime-facemask-detection/
├── app.py               # Flask server & /video_feed route
├── mask_detector.py     # Model loading + prediction logic
├── templates/
│   └── index.html       # Frontend web page
├── model/
│   └── mask_detector.h5 # Pre-trained Keras weights
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Webcam connected to your computer

### Installation

```bash
# Clone the repository
git clone https://github.com/areebajavid/realtime-facemask-detection.git
cd realtime-facemask-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Open **http://localhost:5000** in your browser and allow camera permissions.

---

## 🖥️ Usage

| Scenario | Result |
|----------|--------|
| 😷 Wearing a mask | 🟢 Green **"Mask"** label |
| 😐 No mask | 🔴 Red **"No Mask"** label |

---

## 🏗️ How It Works

```
Webcam → OpenCV Capture → Resize (224x224)
      → Keras Model Prediction → Draw Label
      → JPEG Encode → Flask Stream → Browser
```

1. OpenCV captures frames from `VideoCapture(0)`
2. Each frame is resized to `224x224` and normalized
3. The Keras model predicts: `0 = Mask`, `1 = No Mask`
4. A colored label is drawn on the frame
5. Flask streams frames as `multipart/x-mixed-replace` to the browser

---

## 📦 Dependencies

| Package | Version |
|---------|---------|
| `Flask` | 2.0.1 |
| `TensorFlow` | 2.6.0 |
| `opencv-python` | 4.5.3.56 |
| `numpy` | 1.19.5 |

---

## 📄 License

MIT License © 2026
