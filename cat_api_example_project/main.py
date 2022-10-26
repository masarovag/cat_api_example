from PIL import Image
import requests
from io import BytesIO
import json

responseGetCat = requests.get("https://api.thecatapi.com/v1/images/search").json()

url = responseGetCat[0]["url"]
responseGetImage = requests.get(url)
img = Image.open(BytesIO(responseGetImage.content))
img.show()