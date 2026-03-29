from FileSystem.Models.FIle import File
from FileSystem.Models.Folder import Folder
from FileSystem.Services.FileSystem import FileSystem


fs = FileSystem()

path = ''

count = 0
id = 1

while count < 5:

    folder = fs.openFileOrFolder(path)

    file1 = Folder(id, 'folder'+str(id))
    fs.newFileOrFolder(path, file1)

    id += 1

    file2 = File(id, 'file'+str(id), 'txt', 'Hello world! Again')
    fs.newFileOrFolder(path, file2)
    
    id += 1

    path += file1.name + '/'
    count += 1

print(fs.root)

file = fs.openFileOrFolder('/file2/')

print(file.content)

fs.deleteFile('/file2/')

file = fs.openFileOrFolder('/file2/')

print(file)



