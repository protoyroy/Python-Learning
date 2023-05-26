file1 = "Chapter 09/copy.txt"
file2 = "Chapter 09/this.txt"


with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")

# When we say that two files are identical, it means that the content of both files is exactly the same. Every character, byte, or line in one file matches the corresponding character, byte, or line in the other file.