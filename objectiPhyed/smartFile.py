from typing import List

from .augTokGen import AugTokGen
from .smartLine import SmartLine


class SmartFile:
    line_list: List[SmartLine] = []

    def __init__(self, file):
        self.file: str = file

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
