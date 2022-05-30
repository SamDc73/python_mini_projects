import math
import argparse

praser = argparse.ArgumentParser(
    description="an app to calculate the volume of a cylinder"
)
praser.add_argument(
    '-r', '--radius', metavar='', help='Enter the cylinder radius in cm'
)
praser.add_argument(
    '-H', '--hieght', metavar='', help="Enter the hieght of the cylinder please"
)

args = praser.parse_args()


def cylinder_volume(hieght, radius):
    vol = (math.pi) * (radius**2) * (hieght)
    return vol


if __name__ == "__main__":
    cylinder_volume(args.hieght, args.radius)
