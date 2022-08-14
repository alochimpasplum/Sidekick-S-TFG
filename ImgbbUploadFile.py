from PIL.Image import Image
from io import BytesIO
import Constants
import requests
import base64


def upload_image(img: Image) -> str:
    url: str = "{}?key={}&expiration={}".format(
        Constants.IMGBB_URL, Constants.IMGBB_API_KEY, str(Constants.IMGBB_EXPIRATION_TIME))
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)
    files = {'image': im_b64}
    response = requests.post(url, files)
    response.raise_for_status()
    data = response.json()
    return data['data']['url']
