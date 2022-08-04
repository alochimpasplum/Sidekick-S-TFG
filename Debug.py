import cv2
from Classes import Block


def show_detections(blocks: [Block], img) -> None:
    img = cv2.imread(img)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for block in blocks:
        cv2.rectangle(img, (int(block.x_max), int(block.y_max)), (int(block.x_min), int(block.y_min)), (0, 255, 0))
        cv2.putText(img, str(block.objet_type.name),
                    (int(block.x_max), int((block.y_max+block.y_min)/2)), font, 1, (0, 255, 0))

    cv2.imshow('image', img)
    cv2.waitKey(0)
