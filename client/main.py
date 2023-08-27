import requests
import cv2


url = "http://localhost:2000/yolo8/"

data = {
    "image": "value1"
}

image = cv2.imread("./laptop.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

data = {"image": image.tolist()}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("POST request was successful!")
    print("Response:", response.json())
else:
    print("POST request failed with status code:", response.status_code)