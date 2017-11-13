from .augTokGen import AugTokGen
from .smartLine import SmartLine


class SmartFile:
    def __init__(self, file):
        self.file = file
        self.line_list = []

    def load_file(self):
        tokgen = AugTokGen(self.file)
        while True:
            try:
                line = SmartLine(tokgen.readline())
                self.line_list.append(line)
            except StopIteration:
                break

    def print_lines(self):
        for line in self.line_list:
            print(line)

    def print_raw(self):
        for line in self.line_list:
            print(str(line.num_indents) + ": " + line.get_raw())
