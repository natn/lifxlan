#!/usr/bin/env python
# coding=utf-8
import sys

import lifxlan


def main():
    num_lights = None
    if len(sys.argv) != 2:
        print("\nDiscovery will go much faster if you provide the number of lights on your LAN:")
        print("  python {} <number of lights on LAN>\n".format(sys.argv[0]))
    else:
        num_lights = int(sys.argv[1])

    t = lifxlan.TileChain("d0:73:d5:33:14:21", "192.168.1.143", verbose=True)
    print(t)

    # # instantiate LifxLAN client, num_lights may be None (unknown).
    # # In fact, you don't need to provide LifxLAN with the number of bulbs at all.
    # # lifx = LifxLAN() works just as well. Knowing the number of bulbs in advance
    # # simply makes initial bulb discovery faster.
    # print("Discovering lights...")
    # lifx = LifxLAN(num_lights)
    #
    # # get devices
    # devices = lifx.get_devices()
    # print("\nFound {} light(s):\n".format(len(devices)))
    # for d in devices:
    #     print(d)

if __name__=="__main__":
    main()
