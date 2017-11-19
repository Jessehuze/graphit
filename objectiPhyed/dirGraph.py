from .smartFile import SmartFile
from .graph.graph import *


# TODO: Finish Implementing add dir and file
class DirGraph(Graph):
    def __init__(self):
        super(self).__init__()
        self.dir_root = Node('/')
        Edge('dir_root', self.root, self.dir_root)

    def add_directory(self, dir_path: str, curr_node=None):
        if dir_path.isspace():
            raise ValueError('Directory path should not be empty: "' + dir_path + '"')
        split_path = dir_path.split('/')
        if len(split_path) > 0:
            if curr_node is None:
                pass

    def add_file(self, file: SmartFile):
        pass
