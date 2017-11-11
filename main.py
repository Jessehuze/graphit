from objectiPhyed.smartFile import SmartFile


def main():
    smartfile = SmartFile("objectiPhyed/augTokGen.py")

    smartfile.load_file()

    smartfile.print_raw()

if __name__ == '__main__':
    main()