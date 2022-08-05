import math


def distance_point_to_line(line: [[int, int], [int, int]], point: [int, int]) -> float:
    m: float = (line[1][1]-line[0][1])/(line[1][0]-line[0][0])
    # y - y0 =  m(x - x0) => -(A)mx + (B)y + (C)(m*x0 - y0) = 0
    a: float = -m
    b: float = 1
    c: float = m*line[1][0] - line[1][1]

    # D(line, point) = abs((A*Px + B*Py + C)/(sqr(A^2 + B^2)))
    d: float = (a*point[0] + b*point[1] + c) / math.sqrt(a**2 + b**2)
    return abs(d)
