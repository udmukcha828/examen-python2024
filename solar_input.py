# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet, Orbit


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            if object_type == "orbit":
                orbit = Orbit()
                parse_orbit_parameters(line, orbit)
                objects.append(orbit)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    star.type = "star"
    r, color, m, x, y, vx, vy, theta= line.split()[1:]
    star.theta=int(theta)
    star.R = int(r)
    star.color = color
    star.m = float(m)
    star.x = float(x)
    star.y = float(y)
    star.Vx = float(vx)
    star.Vy = float(vy)
    star.theta = float(theta)

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.type = "star"
    r, color, m, x, y, vx, vy,theta= line.split()[1:]
    planet.theta=int(theta)
    planet.R = int(r)
    planet.color = color
    planet.m = float(m)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(vx)
    planet.Vy = float(vy)
    planet.theta = float(theta)


def parse_orbit_parameters(line, orbit):
    orbit.type = "orbit"
    r, color,colr, x, y= line.split()[1:]
    orbit.R = int(r)
    orbit.color = color
    orbit.colr = color
    orbit.x = float(x)
    orbit.y = float(y)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if obj.type == 'star':
                s = 'Star '
            if obj.type == 'planet':
                s = 'Planet'
            if obj.type == 'orbit':
                s = 'Orbit'
            if obj.type != 'orbit':
                s += str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' + str(obj.x) + ' '
                s += str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n' + '\n'
                out_file.write(s)
            if obj.type == 'orbit':
                s += str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.colr) + ' ' + str(obj.x) + ' '
                s += str(obj.y) + '\n' + '\n'
                out_file.write(s)



if __name__ == "__main__":
    print("This module is not for direct call!")
