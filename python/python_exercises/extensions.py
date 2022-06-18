import re

extentions = { 
    '.gif': 'media/gif',
    ".jpeg": "media/jpeg",
    ".jpg": "media/jpg",
    ".png": "media/png",
    ".pdf": "media/pdf",
    ".txt": "media/txt",
    ".zip": "media/zip"
}

file_name = input("file name: ")
if file_name.endswith(".gif"):
    print(extentions[".gif"])
elif file_name.endswith(".jpeg"):
    print(extentions[".jpeg"])
elif file_name.endswith(".jpg"):
    print(extentions['.jpg'])
elif file_name.endswith(".png"):
    print(extentions['.png'])
elif file_name.endswith(".pdf"):
    print(extentions['.pdf'])
elif file_name.endswith(".txt"):
    print(extentions['.txt'])
elif file_name.endswith(".zip"):
    print(extentions['.zip'])
else:
    print("application/octet-stream")


