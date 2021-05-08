import subprocess
import sys
from pathlib import Path


def main():
    command = sys.argv[1:]

    command.insert(0, "brew")
    subprocess.run(command)

    if len(command) <= 1:
        return

    if command[1] == "install":
        package = command[2]
        add_to_brew("brew \"" + package + "\"")


def add_to_brew(data):
    with open(str(Path.home()) + "/Brewfile", "a") as brewfile:
        brewfile.write(data)


if __name__ == '__main__':
    main()
