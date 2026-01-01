import cv2
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('model/mask_detector.h5')

# Prediction function
def detect_face_mask(img):
    y_pred = model.predict(img.reshape(1, 224, 224, 3), verbose=0)[0][0]
    return 0 if y_pred < 0.5 else 1  # 0 = mask, 1 = no mask

# Label drawer
def draw_label(img, text, pos, bg_color):
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, cv2.FILLED)
    end_x = pos[0] + text_size[0][0] + 2
    end_y = pos[1] + text_size[0][1] - 2
    cv2.rectangle(img, pos, (end_x, end_y), bg_color, cv2.FILLED)
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

# Main video stream function for Flask
def detect_mask():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        try:
            resized_frame = cv2.resize(frame, (224, 224))
            y_pred = detect_face_mask(resized_frame)

            if y_pred == 0:
                draw_label(frame, "Mask", (30, 30), (0, 255, 0))
            else:
                draw_label(frame, "No Mask", (30, 30), (0, 0, 255))

            # Encode frame for web streaming
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        except Exception as e:
            print(f"Processing error: {str(e)}")
            continue
