# Image Time Classifier App with FastAPI and Streamlit

This is an image classification app designed to determine the time of day using the CLIP model, specifically the `ViT-B/32` variant from torchvision. Users can easily upload an image, and the app will classify it into one of the following time categories: 'morning,' 'noon,' 'afternoon,' 'night,' or 'sunrise or sunset.' The app utilizes FastAPI for handling backend functionalities and Streamlit for a straightforward user interface. Docker and Docker Compose are employed for easy deployment and management of the application.



## Requirements

- Python 3.6 or higher
- FastAPI
- Streamlit
- Torch
- Pillow
- Redis OM
- Matplotlib
- Requests

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/shakibyzn/image-time-classifier-app.git
   ```

2. Navigate to the project directory:

   ```
   cd image-time-classifier-app
   ```

## Usage

   ```
   docker compose up --build -d
   ```
## Run unittests

```
docker compose exec backend-container pytest
```

## Demo

![samples](https://github.com/shakibyzn/image-time-classifier-app/blob/main/demo.png)

## License

This project is licensed under the [MIT License](LICENSE).
