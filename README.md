# Image Object Detection Client-Server

This repository demonstrates a simple example of using YOLOv8 for object detection with FastAPI and Docker.

Client: Sends images to the server.
Server: Dockerized FastAPI app processes images with YOLOv8, returns results.

## Getting Started

Follow these steps to set up and run the project:


1. Navigate to the server directory:
```bash
cd ./server
```
2. Build a Docker image from the Dockerfile:
```bash
docker build -t yolo8-docker-simple .
```


3. Create a Docker container and run the server:
```bash
docker container run -p 2000:8000 --rm -ti yolo8-docker-simple
```

Note: Ensure you have an active internet connection to install required dependencies when the server starts.



4. Open another terminal and Move to the client directory:
```bash
cd Client
```


5. Run the client-side application:
```bash
python main.py
```
After a short time, the client will display the response to your request.