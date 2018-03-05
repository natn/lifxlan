#!/usr/bin/env python
# coding=utf-8
import sys

from lifxlan import RED, BLUE, LifxLAN
from time import sleep


def main():
    num_lights = None
    if len(sys.argv) != 2:
        print("\nDiscovery will go much faster if you provide the number of lights on your LAN:")
        print("  python {} <number of lights on LAN>\n".format(sys.argv[0]))
    else:
        num_lights = int(sys.argv[1])

    # instantiate LifxLAN client, num_lights may be None (unknown).
    # In fact, you don't need to provide LifxLAN with the number of bulbs at all.
    # lifx = LifxLAN() works just as well. Knowing the number of bulbs in advance
    # simply makes initial bulb discovery faster.
    print("Discovering lights...")
    lifx = LifxLAN(num_lights)

    # get devices
    devices = lifx.get_devices()
    lights = lifx.get_lights()
    print("Found {} devices(s).".format(len(devices)))
    print("Found {} light(s):\n".format(len(lights)))

    cpulight = lifx.get_device_by_name("CPU")
    print(cpulight)
    workbenchlight = lifx.get_device_by_name("Workbench")
    print(workbenchlight)

    cpulight.set_color(RED, rapid=True)
    workbenchlight.set_color(RED, rapid=True)
    sleep(5)
    cpulight.set_waveform(is_transient=0, color=BLUE, period=55000, cycles=10000, duty_cycle=0.5, waveform=1, rapid=False)
    workbenchlight.set_waveform(is_transient=0, color=BLUE, period=60000, cycles=10000, duty_cycle=0.5, waveform=1, rapid=False)



if __name__=="__main__":
    main()