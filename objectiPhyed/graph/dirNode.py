from typing import List
from .node import Node
from .edge import Edge
from .graphErrors.graphBreakingError import GraphBreakingError


class DirNode(Node):
    def __init__(self, value):
        super(self).__init__(self, value)
        self.file_edges: List[Edge] = []

    def add_file_edge(self, edge):
        if edge.parent == self:
            self.file_edges.append(edge)
        else:
            raise GraphBreakingError('Edge does not contain this node as a parent: ' + str(edge))

    def remove_file_edge(self, edge):
        self.file_edges.remove(edge)
