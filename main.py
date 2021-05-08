import subprocess
import sys
from pathlib import Path


def main():
    command = sys.argv[1:]

    command.insert(0, "brew")
    result = subprocess.run(command)
    return_code = result.returncode

    if return_code != 0:
        return

    if len(command) <= 1:
        return

    if command[1] == "install" and len(command) > 2:
        package = command[2]
        if len(package) > 0:
            add_to_brew("brew \"" + package + "\"")
    elif command[1] == "tap" and len(command) > 2:
        package = command[2]
        if len(package) > 0:
            add_to_brew("tap \"" + package + "\"")


def add_to_brew(data):
    with open(str(Path.home()) + "/Brewfile", "a") as brewfile:
        brewfile.write(data + "\n")


if __name__ == '__main__':
    main()
