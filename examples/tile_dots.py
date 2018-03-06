from lifxlan import *
from random import randint, choice
import timeit

from time import sleep
import copy

def main():
    lan = LifxLAN()

    t = TileChain("d0:73:d5:33:14:21", "192.168.1.143")
    num_tiles = 5 #depends on light, hardcoded for now
    (cols, rows) = t.get_canvas_dimensions(num_tiles)
    hue = 0
    background_colors = []
    for row in range(rows):
        color_row = []
        for col in range(cols):
            color_row.append((hue, 65535, 2000, 4900))
            hue += int(65535.0/(cols*rows))
        background_colors.append(color_row)

    matrix = copy.deepcopy(background_colors)
    t.project_matrix(matrix, num_tiles, 2000)
    sleep(2)

    duration_ms = 150


    dots=[]
    max_dots=50
    while(True):
        dot = [choice(range(rows)),choice(range(cols))]
        dots.append(dot)
        if len(dots) > max_dots:
            old_dot = dots.pop(0)
            matrix[int(old_dot[0])][int(old_dot[1])] = background_colors[int(old_dot[0])][int(old_dot[1])]

        matrix[int(dot[0])][int(dot[1])] = get_random_color()
        t.project_matrix(matrix, num_tiles,duration_ms, rapid=True)
        sleep(duration_ms/2000)


def cycle_row(matrix):
    new_matrix = [matrix[-1]]
    for row in matrix[:-1]:
        new_matrix.append(row)
    return new_matrix


def get_random_color():
    return randint(0, 65535), randint(65535, 65535), randint(0, 65535), randint(2500, 9000)


if __name__=="__main__":
    main()
