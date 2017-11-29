from typing import List

from .graph.node import Node
from .smartLine import SmartLine
from .smartClass import SmartClass


class SmartFunction(Node):
    def __init__(self, file, parent=None, line_list=[]):
        super(self).__init__(self, self)
        self.file = file
        self.parent: SmartClass = parent
        self.line_list: List[SmartLine] = line_list
