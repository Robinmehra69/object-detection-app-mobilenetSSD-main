from flask import Flask, render_template, request, redirect, send_from_directory, url_for
import cv2
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

# Ensure upload and processed directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

# Paths to the model files
prototxt = "MobileNetSSD_deploy.prototxt"
caffe_model = "MobileNetSSD_deploy.caffemodel"

# Load the Caffe model
net = cv2.dnn.readNetFromCaffe(prototxt, caffe_model)

# Dictionary with the object class id and names on which the model is trained
classNames = {0: 'background',
              2: 'bicycle', 3: 'bird', 4: 'boat',
              5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
              10: 'cow', 12: 'dog', 13: 'horse',
              14: 'motorbike', 15: 'person', 16: 'pottedplant',
              18: 'sofa'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded file
        filename = f"{uuid.uuid4().hex}_{file.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the file
        processed_filepath = os.path.join(app.config['PROCESSED_FOLDER'], filename)
        process_file(filepath, processed_filepath)

        # Return the processed file URL
        processed_image_url = url_for('send_processed_file', filename=filename)
        return render_template('index.html', processed_image=processed_image_url)

@app.route('/processed/<filename>')
def send_processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

def process_file(input_path, output_path):
    # Read the uploaded image
    image = cv2.imread(input_path)

    # Perform object detection on the image
    image = detect_objects(image)

    # Save the processed image
    cv2.imwrite(output_path, image)

def detect_objects(frame):
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0 / 127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            x_top_left = int(detections[0, 0, i, 3] * width)
            y_top_left = int(detections[0, 0, i, 4] * height)
            x_bottom_right = int(detections[0, 0, i, 5] * width)
            y_bottom_right = int(detections[0, 0, i, 6] * height)

            cv2.rectangle(frame, (x_top_left, y_top_left), (x_bottom_right, y_bottom_right), (0, 255, 0), 2)

            if class_id in classNames:
                label = f"{classNames[class_id]}: {confidence:.2f}"
                cv2.putText(frame, label, (x_top_left, y_top_left - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
