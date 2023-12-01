from fastapi import FastAPI
from model import PredictionPipeline
from pydantic import BaseModel
from redis_om import HashModel, get_redis_connection


redis = get_redis_connection(
    host="redis-13090.c55.eu-central-1-1.ec2.cloud.redislabs.com",
    port=13090,
    password="yGKEhSvvF2IDRq738JPGaicSMmJm9E7A",
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
