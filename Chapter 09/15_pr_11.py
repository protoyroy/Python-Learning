import os
oldname = "Chapter 09/hookah.txt"
newname = "Chapter 09/renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)
os.remove(oldname)