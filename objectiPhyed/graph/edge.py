from .node import Node


class Edge:
    def __init__(self, value, parent: Node, child: Node):
        self.value = value
        self.parent = parent
        self.parent.add_edge(self)
        self.child = child
        self.child.add_edge(self)
