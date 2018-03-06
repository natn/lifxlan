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
    rainbow_colors = []
    for row in range(rows):
        color_row = []
        for col in range(cols):
            color_row.append((hue, 65535, 1000, 4500))
            hue += int(65535.0/(cols*rows))
        rainbow_colors.append(color_row)

    matrix = copy.deepcopy(rainbow_colors)
    t.project_matrix(matrix, num_tiles, 2000)
    sleep(2)

    duration_ms = 500

    while(True):
        for dots in range(150):
            matrix[choice(range(rows))][choice(range(cols))] = get_random_color()
            t.project_matrix(matrix, num_tiles,duration_ms, rapid=True)
            sleep(duration_ms/2000)

        sleep(2)
        matrix = copy.deepcopy(rainbow_colors)
        t.project_matrix(matrix, num_tiles, 5000)




def cycle_row(matrix):
    new_matrix = [matrix[-1]]
    for row in matrix[:-1]:
        new_matrix.append(row)
    return new_matrix

def get_random_color():
    return (randint(0,65535), randint(0,65535), randint(0,65535), randint(2500,9000))

if __name__=="__main__":
    main()
