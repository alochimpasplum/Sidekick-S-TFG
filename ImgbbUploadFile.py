from PIL.Image import Image
from io import BytesIO
import Constants
import requests
import base64


def upload_image(img: Image) -> None:
    url: str = "{}?key={}&expiration={}".format(
        Constants.IMGBB_URL, Constants.IMGBB_API_KEY, str(Constants.IMGBB_EXPIRATION_TIME))
    files = {'image': img}
    response = requests.post(url, files)
    print(response.content)
