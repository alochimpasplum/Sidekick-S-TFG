import Constants
from ImgbbUploadFile import upload_image
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from Classes.Block import Block
from Classes.Text import Text
from OCR.EasyOCR import __get_inner_texts as get_inner_texts
from OCR.EasyOCR import __get_outer_text as get_outer_text

from array import array
import os
from PIL import Image
import sys
import time


def OCR(img: Image, blocks: [Block]) -> [Block]:

    subscription_key = Constants.AZURE_OCR_SUBSCRIPTION_KEY
    endpoint = Constants.AZURE_OCR_ENDPOINT

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Get an image with text
    read_image_url = upload_image(img)

    # Call API with URL and raw response (allows you to get the operation location)
    read_response = computervision_client.read(read_image_url,  raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    texts: [Text] = []
    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        index: int = 0
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                x_min: float = line.bounding_box[0]
                y_min: float = line.bounding_box[1]
                x_max: float = line.bounding_box[4]
                y_max: float = line.bounding_box[5]
                text: Text = Text(index, line.bounding_box[0], line.bounding_box[1], line.bounding_box[4], line.bounding_box[5], line.words[0].confidence, line.text)
                index = index + 1
                texts.append(text)

    temp: [[Block], [Text]] = get_inner_texts(texts, blocks)
    blocks = get_outer_text(temp[0], temp[1])

    return blocks
