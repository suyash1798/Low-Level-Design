from FileSystem.Models.Node import Node

class Folder(Node):
    children: dict[str, Node]

    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.children = {}