# coding: utf-8
# license: GPLv3
from math import atan2, cos, sin


def calculate_force(body, space_objects):
    """

    Параметры:

    body — тело, для которого нужно вычислить дейстующую силу.
    space_objects — список объектов, которые воздействуют на тело.
    """

    for obj in space_objects:
        if isinstance(body, Planet):
            body.theta += 1
            body.x += body.R * cos(body.theta)
            body.y += body.R * sin(body.theta)


if __name__ == "__main__":
    print("This module is not for direct call!")
