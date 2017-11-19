from objectiPhyed.smartFile import SmartFile
from objectiPhyed.lineType import LineType


def main():
    smartfile = SmartFile("objectiPhyed/augTokGen.py")

    smartfile.load_file()

    smartfile.print_lines()

if __name__ == '__main__':
    main()