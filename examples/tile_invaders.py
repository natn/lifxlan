from lifxlan import *
from random import randint
from time import sleep


def main():
    t = TileChain("d0:73:d5:33:14:21", "192.168.1.143")
    num_tiles = t.get_tile_count()

    duration_ms = 0

    palette = {0: [0, 0, 0, 0],
               1: [43634, 65535, 30000, 3500]
                }

    num_frames = 2
    invader_matrix = \
           [[[1, 1, 1, 0, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 1, 0, 1],
             [0, 1, 1, 1, 1, 1, 1, 0],
             [1, 0, 1, 1, 1, 1, 0, 1]],

            [[1, 1, 1, 0, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 1, 1, 0, 1, 1],
             [1, 0, 1, 0, 0, 1, 0, 1],
             [0, 1, 0, 1, 1, 0, 1, 0]]]

    while True:
        for frame in range(num_frames):
            sprite = []
            for x in range(8):
                for y in range(8):
                        sprite.append(palette[invader_matrix[frame][x][y]])
            for index in range(num_tiles):
                t.set_tile_colors(index, sprite, duration_ms)
            sleep(1)


def get_random_color():
    return randint(0, 65535), randint(0, 65535), randint(0, 65535), randint(2500, 9000)


if __name__ == "__main__":
    main()
