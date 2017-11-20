from typing import List
from .node import Node
from .edge import Edge
from .graphErrors.graphBreakingError import GraphBreakingError


# TODO: Change these add edges to add nodes across the board.
class FileNode(Node):
    def __init__(self, value):
        super(self).__init__(self, value)
        self.dir_edge: List[Edge] = []
        self.import_edges: List[Edge] = []
        self.class_edges: List[Edge] = []
        self.unbound_function_edges: List[Edge] = []

    def set_dir_edge(self, edge):
        self.dir_edge = edge

    def add_import_edge(self, edge):
        if edge.parent == self:
            self.import_edges.append(edge)
        else:
            raise GraphBreakingError('Edge does not contain this node as a parent: ' + str(edge))

    def remove_import_edge(self, edge):
        self.import_edges.remove(edge)

    def add_class_edge(self, edge):
        if edge.parent == self:
            self.class_edges.append(edge)
        else:
            raise GraphBreakingError('Edge does not contain this node as a parent: ' + str(edge))

    def remove_class_edge(self, edge):
        self.class_edges.remove(edge)
