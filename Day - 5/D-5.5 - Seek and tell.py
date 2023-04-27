# SEEK SEEK SEEK SEEK SEEK SEEK SEEK
with open("README.md", "r") as fh:
    x = fh.seek(10)
    read = fh.read(6)
    print(read)
    
    tell = fh.tell()
    print(tell)