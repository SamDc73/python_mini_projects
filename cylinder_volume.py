import math
import argparse

parser = argparse.ArgumentParser(description="Calculate the Volume of a Cylinder")
parser.add_argument(
    "-r",
    "--radius",
    type=int,
    metavar="",
    required=True,
    help="The Radius of the cylinder",
)
parser.add_argument(
    "-H",
    "--hieght",
    type=int,
    metavar="",
    required=True,
    help="The hieght of the cylinder",
)
args = parser.parse_args()


def cylinder_volume(radius, hieght):
    vol = (math.pi) * (radius**2) * (hieght)
    return vol


if __name__ == "__main__":
    volume = cylinder_volume(args.radius, args.hieght)
