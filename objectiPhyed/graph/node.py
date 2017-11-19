from typing import List
from .edge import Edge
from .graphErrors.graphBreakingError import GraphBreakingError


class Node:
    def __init__(self, value):
        self.value = value
        self.is_parent_edges: List[Edge] = []
        self.is_child_edges: List[Edge] = []

    def add_edge(self, edge):
        if edge.parent == self:
            self.is_parent_edges.append(edge)
        elif edge.child == self:
            self.is_child_edges.append(edge)
        else:
            raise GraphBreakingError('Edge does not contain this node as a parent or a child: ' + str(edge))

    def remove_edge_child(self, edge):
        self.is_child_edges.remove(edge)

    def remove_edge_parent(self, edge):
        self.is_parent_edges.remove(edge)

    def child_exists(self, value):
        for edge in self.is_parent_edges:
            if edge.child.value == value:
                return True, edge
        return False, None

    def parent_exists(self, value):
        for edge in self.is_child_edges:
            if edge.parent.value == value:
                return True, edge
        return False, None
