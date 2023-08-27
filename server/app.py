from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np
from fastapi.responses import JSONResponse

from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.predict(stream=True, imgsz=(640,480))

def predict_yolo(image):
    result = model(image)
    return result

app = FastAPI()




class YOLOImage(BaseModel):
    image:List[List[List[float]]]
    

@app.get("/")
def read_root():
    print("here")
    return {"docker": "yolo"}


@app.post("/yolo8/")
async def create_item(file: YOLOImage):
    image = np.array(file.image)
    result = predict_yolo(image=image)
    
    return JSONResponse(content=result[0].tojson())
