import  requests
import cv2
import base64

import numpy as np

url = "http://localhost:2000/yolo8/"





image = cv2.imread("laptop.jpg")
_, encoded_image = cv2.imencode('.jpg', image)
base64_encoded = base64.b64encode(encoded_image).decode('utf-8')


response = requests.post(url, json={"image" : base64_encoded})

if response.status_code == 200:
    print("POST request was successful!")
    print("Response:", response.json())
else:
    print("POST request failed with status code:", response.status_code,response)