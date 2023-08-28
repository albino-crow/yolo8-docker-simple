from fastapi import FastAPI
from pydantic import BaseModel,Field

import numpy as np
from fastapi.responses import JSONResponse

import cv2

import base64
from ultralytics import YOLO


model = YOLO('yolov8n.pt')

def predict_yolo(image):
    result = model(image)
    return result

app = FastAPI()

def convert_base64_image(image: str):
    image = base64.b64decode(image)

    image = np.frombuffer(image, dtype=np.uint8)

    image = cv2.imdecode(image, flags=cv2.IMREAD_COLOR)
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = np.array(image)

    return image



class YOLOImage(BaseModel):
    image:str =  Field(...,description="will get base64 image ")
    

@app.get("/")
def read_root():
    print("here")
    return {"docker": "yolo"}


@app.post("/yolo8/")
async def create_item(file: YOLOImage):
    image = convert_base64_image(file.image)
    result = predict_yolo(image=image)
    
    return JSONResponse(content=result[0].tojson())
