from FileSystem.Models.FIle import File
from FileSystem.Models.Folder import Folder
from FileSystem.Models.Node import Node

class FileSystem:
    root: Folder
    nodeDict: dict[int, Folder | File]

    def __init__(self):
        self.root = Folder(0, 'root')
        self.nodeDict = {}

    def newFileOrFolder(self, path: str, file: Folder | File):
        paths = [p for p in path.strip("/").split("/") if path]

        root = self.root

        for p in paths:
            if p not in root.children:
                raise Exception("Enter a vaild path")
            
            root = self.nodeDict[root.children[p]]
        
        if file.name in root.children:
            raise Exception("File already exists")
        
        root.children[file.name] = file.id
        self.nodeDict[file.id] = file
    
    def openFileOrFolder(self, path: str):
        paths = [p for p in path.strip("/").split("/") if path]

        root = self.root
        print(paths)
        for p in paths:
            if p not in root.children:
                raise Exception("Enter a vaild path")
            
            root = self.nodeDict[root.children[p]]
        
        return root
    
    def deleteFile(self, path: str):
        paths = [p for p in path.strip("/").split("/") if path]
        root = self.root
        parent = None

        for p in paths:
            if p not in root.children:
                raise Exception("Enter a vaild path")
            
            parent = root
            root = self.nodeDict[root.children[p]]
        
        del parent.children[root.name]
        del self.nodeDict[root.id]




    