from lifxlan import *
from random import randint
import time

import math
import colorsys


from time import sleep
from math import sin,cos, sqrt, pi
import copy


def main():
    lan = LifxLAN()

    t = TileChain("d0:73:d5:33:14:21", "192.168.1.143")
    num_tiles = 5  # depends on light, hardcoded for now
    (cols, rows) = t.get_canvas_dimensions(num_tiles)
    hue = 0
    rainbow_colors = []
    for row in range(rows):
        color_row = []
        for col in range(cols):
            color_row.append((hue, 65535, 1000, 4500))
            hue += int(65535.0 / (cols * rows))
        rainbow_colors.append(color_row)

    matrix = copy.deepcopy(rainbow_colors)
    t.project_matrix(matrix, num_tiles, 2000)
    sleep(2)

    while(True):
        sec = time.mktime(time.gmtime())
        plasma(rows - 1, cols - 1, matrix, sec)
        t.project_matrix(matrix, num_tiles, 2000)
        sleep(2)


def plasma(w, h, matrix, sec):
    print(w,h)
    for x in range(w):
        for y in range(h):
            dx = x + 1 * sin(sec/5.0)
            dy = y + 1 * cos(sec/3.0)

            dv= sin(x*10 + sec) + sin(10*(x*sin(sec/2.0) + y*cos(sec/3.0)) + sec) + sin(sqrt(100*(dx*dx + dy*dy)+1)+sec)

            hsv = colorsys.rgb_to_hsv(abs(sin(dv * pi)), abs(sin(dv*pi + 2*pi/3)), abs(sin(dv*pi + 4*pi/3)))

            print(hsv)
            matrix[x][y] = [hsv[0] * 65535, hsv[1]*65535 ,5000]



def get_random_color():
    return (randint(0, 65535), randint(0, 65535), randint(0, 65535), randint(2500, 9000))


if __name__ == "__main__":
    main()
