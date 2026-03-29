Requirements

1. Able to create new folder or file
2. Able access content of already create or save file or folder
3. Able to delete complete folder or file
4. Support 10 level of nest folder structure
5. Max 500 characters supported per file and 10 character per name

Entities

1. File
    - id
    - name
    - type (File or Folder)
    - content
    - extension ?

2. FileTypeEnum
    - File
    - Folder

3. FileSystem
    - rootFolder (root: { subRoot: {} })
    - newFile(path, file) (/ points to rootFolder)
    - openFolder(path)
    - deleteFile(path)

4. FileUtils
    - PathValidator


Flow

1. Create a File
    - First check if path valid or not
    - If path has extension in between then we can reject the request
    - Also, if path has more than one level or last path not already exists we can reject
    - Go to the path in rootFolder and create new file or folder

2. Delete a File
    - First check if path valid and exists
    - If yes, then got to path and delete that fil or folder node

