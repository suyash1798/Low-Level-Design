from FileSystem.Models.Node import Node


class File(Node):
    extension: str
    content: str

    def __init__(self, id: int, name: str, extension: str, content: str):
        super().__init__(id, name)
        self.extension = extension
        self.content = content
