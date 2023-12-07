from fastapi import FastAPI
from model import PredictionPipeline
from pydantic import BaseModel
from redis_om import HashModel, get_redis_connection

# Sign up on https://redis.com/cloud/overview/ and paste your credentials here
redis = get_redis_connection(
    host="YOUR-HOST",
    port=13090,
    password="YOUR-PASSWORD",
    decode_responses=True
)

class ImageInput(BaseModel):
    path: str

class ImageModel(HashModel):
    path: str
    label: str

    class Meta:
        database = redis

app = FastAPI()

@app.post('/predict')
async  def predict(img: ImageInput):
    pipeline = PredictionPipeline(img.path)
    label = pipeline.predict()['label']
    img_model = ImageModel(
        path=img.path,
        label=label
    )
    img_model.save()
    return label
