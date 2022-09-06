import math


def distance_point_to_segment(A: [float], B: [float], P: [float]) -> float:
    a: float = math.dist(B, P)
    b: float = math.dist(A, P)
    p: float = math.dist(A, B)
    # cos theorem #
    # a^2 = b^2 + p^2 -2bp*cosA => a^2 - b^2 - p^2 = -2bp*cosA =>-a^2 + b^2 + p^2 = 2bp*cosA
    #   cosA = (-a^2 + b^2 + p^2) / 2bp
    cos_a: float = (-math.pow(a, 2) + math.pow(b, 2) + math.pow(p, 2)) / (2*b*p)
    cos_b: float = (math.pow(a, 2) - math.pow(b, 2) + math.pow(p, 2)) / (2*a*p)
    angle_a: float = math.degrees(math.acos(cos_a))
    angle_b: float = math.degrees(math.acos(cos_b))
    if angle_a > 90:
        return b
    elif angle_b > 90:
        return a
    else:
        # senA = h / b => h = b*senA
        return b * math.sin(math.radians(angle_a))
