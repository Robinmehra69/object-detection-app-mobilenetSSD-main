Explaining how to run your Flask app first locally and then with Docker.


> Object Detection with Flask and Docker

This project implements an object detection application using Flask and OpenCV, where users can upload an image, and the app detects and highlights the objects in the image. This guide explains how to run the app locally with Flask first, and then how to containerize it using Docker.

> Prerequisites

Before you start, make sure you have the following installed:

- Python 3.x
- Flask
- OpenCV
- Docker (for containerization)


1. Install Dependencies

Before running the Flask app, you need to install the required Python dependencies.

Install the dependencies using pip:

bash
pip install -r requirements.txt


//This will install the required Python libraries like Flask, OpenCV, and others.

> Running the Application Locally with Flask

1. Start Flask Application

To test the application locally, you can run the Flask app directly on your machine:

 1.Navigate to the directory where your mobdetapp.py file is located.

 2. Run the Flask app:

   bash
   python mobdetapp.py


 3. Open your browser and visit http://localhost:5000.

 4. You can now upload an image, and the application
 will detect objects in the image using a pre-trained MobileNet-SSD model.

2. Test Locally

- Upload an image using the upload form.
- The image will be processed, and detected objects will be highlighted on the image.
- You can see the results directly on the webpage.



 Dockerizing the Flask Application

Once the Flask application is working locally, you can run it inside a Docker container. Docker ensures that the application will work on any system, regardless of the environment.

> 1. Build the Docker Image

1. Make sure you are in the project directory where the Dockerfile and all your app files are located.

2. Build the Docker image with the following command:

bash
docker build -t flask-object-detection .


This command will build the Docker image using the Dockerfile and tag it as flask-object-detection.

> 2. Run the Docker Container

After building the image, you can run the Flask application in a Docker container:

bash
docker run -p 5000:5000 flask-object-detection


This command will run the container and map port 5000 of the container to port 5000 of your host machine.

> 3. Access the Application in Docker

1. Open your web browser and navigate to http://localhost:5000.

2. You should be able to upload an image just like you did with the local Flask app. The image will be processed, and the detected objects will be shown on the screen.

---

> Troubleshooting

If you encounter any issues while running the application locally or inside Docker, here are some common solutions:

- Webcam Issues: If the webcam doesn't work inside Docker, ensure the necessary libraries and system dependencies are installed, like libgl1-mesa-glx and libxrender1 in the Dockerfile.

- File Paths: Ensure that all model files (like MobileNetSSD_deploy.prototxt and MobileNetSSD_deploy.caffemodel) are correctly placed and are being copied into the Docker image.

- Permissions: Sometimes file permissions may cause issues, especially when uploading files. Make sure the uploads and processed directories are properly set up in your Flask app.

---

> Conclusion

You have now successfully set up an object detection app using Flask and Docker. You can upload images and detect objects, either locally or within a Docker container. This app provides a great base for deploying machine learning models as web applications.

---

> Reference :
1. https://opencv-tutorial.readthedocs.io/en/latest/index.html
2. https://medium.com/@techmayank2000/object-detection-using-ssd-mobilenetv2-using-tensorflow-api-can-detect-any-single-class-from-31a31bbd0691
3. https://flask.palletsprojects.com/en/stable/
4. https://docs.docker.com/reference/
5. https://docs.docker.com/reference/