# Class used to test api functions locally

# https://docs.ovh.com/ca/en/publiccloud/ai/training/web-service-yolov5/?xtor=AL-94-[fr_int_2021_ovh_multiuniverse_multiproduct_deeplink_awareness_reach]-[txt_v1]
import torch

def Detect(img: str):
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

    # Inference
    results = model(img)

    return results.pandas().xyxy[0].to_json(orient="records")


LABELS = ['start_end',
          'scan',
          'decision',
          'print',
          'process',
          'arrow_line_up',
          'arrow_line_down',
          'arrow_line_right',
          'arrow_line_left',
          'pointer']
