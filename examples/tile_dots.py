from lifxlan import *
from random import randint, choice
from time import sleep
from threading import Thread
import copy
import queue



def main():

    #Discovery and setup
    lights = LifxLAN()
    threads = []
    tile_chain = TileChain("d0:73:d5:33:14:21", "192.168.1.143")
    dungeon = lights.get_devices_by_group("Dungeon").get_device_list()
    (cols, rows) = tile_chain.get_canvas_dimensions()

    #set tile background
    background_colors = set_background(cols, rows)
    tile_chain.project_matrix(background_colors, 2000)

    #start tile dots
    duration_ms, max_dots = 150, 50
    tile_thread = Thread(target=do_dots_thread, args=(tile_chain, background_colors, rows, cols, duration_ms, max_dots))
    threads.append(tile_thread)
    tile_thread.start()

    #start random lights
    min_time, max_time = 5, 90
    for light_iter in dungeon:
       light_thread = Thread(target=do_random_light_thread, args=(light_iter, min_time, max_time))
       threads.append(light_thread)
       light_thread.start()





def set_background(cols, rows):
    hue = 0
    background_colors = []
    for row in range(rows):
        color_row = []
        for col in range(cols):
            color_row.append((hue, 65535, 2000, 4900))
            hue += int(65535.0 / (cols * rows))
        background_colors.append(color_row)
    sleep(2)
    return background_colors


def do_dots_thread(tile_chain, background_colors, rows, cols, duration_ms=150, max_dots=50):
    dots = []
    matrix = copy.deepcopy(background_colors)
    while True:

        dot = [choice(range(rows)), choice(range(cols))]
        dots.append(dot)

        if len(dots) > max_dots:
            old_dot = dots.pop(0)
            matrix[int(old_dot[0])][int(old_dot[1])] = background_colors[int(old_dot[0])][int(old_dot[1])]

        matrix[int(dot[0])][int(dot[1])] = get_random_saturated_color()
        try:
            tile_chain.project_matrix(matrix, duration_ms, rapid=True)
        except:
            pass
        sleep(duration_ms / 2000)

def do_random_light_thread(light, min_time, max_time):
    while True:
        time = randint(min_time, max_time)
        color = [get_random_hue(), 65535, 65535, 2500]
        try:
            light.set_color(color , time * 1000)
        except:
            pass
        sleep(time)


def cycle_row(matrix):
    new_matrix = [matrix[-1]]
    for row in matrix[:-1]:
        new_matrix.append(row)
    return new_matrix


def get_random_saturated_color():
    return randint(0, 65535), 65535, randint(0, 65535), 3000

def get_random_hue():
    return randint(0, 65535)


if __name__=="__main__":
    main()
