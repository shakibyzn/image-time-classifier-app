from backend import model

import pytest
import clip
import torch
import numpy as np
from PIL import Image

@pytest.fixture
def pred_pipeline():
    pipe = model.PredictionPipeline('/backend/demo.png')
    return pipe


@pytest.mark.parametrize('model_name', clip.available_models()[:2])
def test_consistency(model_name, pred_pipeline):
    pred_pipeline.model_name = model_name
    prediction = pred_pipeline.predict()
    label = prediction['label']
    assert label in pred_pipeline.labels, (
        "Expected the label to match the labels defined before"
    )