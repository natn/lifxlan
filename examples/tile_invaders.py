from lifxlan import *
from random import randint


from time import sleep


def main():
    t = TileChain("d0:73:d5:33:14:21", "192.168.1.143")
    num_tiles = 5  # depends on light, hardcoded for now

    duration_ms = 0

    COLOR1 = [43634, 65535, 20000, 3500]
    COLOR2 = [0, 0, 0, 0]

    grid = [[[COLOR1, COLOR1, COLOR1, COLOR2, COLOR2, COLOR1, COLOR1, COLOR1],
             [COLOR1, COLOR1, COLOR2, COLOR2, COLOR2, COLOR2, COLOR1, COLOR1],
             [COLOR1, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR1],
             [COLOR2, COLOR2, COLOR1, COLOR2, COLOR2, COLOR1, COLOR2, COLOR2],
             [COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2],
             [COLOR1, COLOR2, COLOR1, COLOR2, COLOR2, COLOR1, COLOR2, COLOR1],
             [COLOR2, COLOR1, COLOR1, COLOR1, COLOR1, COLOR1, COLOR1, COLOR2],
             [COLOR1, COLOR2, COLOR1, COLOR1, COLOR1, COLOR1, COLOR2, COLOR1]],

            [[COLOR1, COLOR1, COLOR1, COLOR2, COLOR2, COLOR1, COLOR1, COLOR1],
             [COLOR1, COLOR1, COLOR2, COLOR2, COLOR2, COLOR2, COLOR1, COLOR1],
             [COLOR1, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR1],
             [COLOR2, COLOR2, COLOR1, COLOR2, COLOR2, COLOR1, COLOR2, COLOR2],
             [COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2, COLOR2],
             [COLOR1, COLOR1, COLOR2, COLOR1, COLOR1, COLOR2, COLOR1, COLOR1],
             [COLOR1, COLOR2, COLOR1, COLOR2, COLOR2, COLOR1, COLOR2, COLOR1],
             [COLOR2, COLOR1, COLOR2, COLOR1, COLOR1, COLOR2, COLOR1, COLOR2]]]


    while (True):
        for g in [0, 1]:
            tilebox = []
            for i in range(8):
                for j in range(8):
                    tilebox.append(grid[g][i][j])
            for index in range(num_tiles):
                t.set_tile_colors(index, tilebox, duration_ms)
            sleep(1)

def get_random_color():
    return (randint(0, 65535), randint(0, 65535), randint(0, 65535), randint(2500, 9000))


if __name__ == "__main__":
    main()
