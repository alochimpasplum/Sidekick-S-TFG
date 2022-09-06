import base64


def encode(text_to_encode: str) -> str:
    graph_bytes = text_to_encode.encode("ascii")
    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string
