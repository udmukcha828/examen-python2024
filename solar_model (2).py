# coding: utf-8
# license: GPLv3
from math import atan2, cos, sin



def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    for obj in space_objects:
        obj.theta += 1
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        body.x += body.r * math.cos(body.theta)
        body.y += body.r * math.sin(body.theta)







if __name__ == "__main__":
    print("This module is not for direct call!")
