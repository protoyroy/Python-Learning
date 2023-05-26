found_python =False

with open("chapter 09/log.txt") as f:
    content = f.readline()
    i= 1
    while content:
        if 'python' in content.lower():
             found_python = True
             print(content)
             print(f"Yes python is present line number {i}")
        content = f.readline()
        i+=1
if not found_python:
        print("Python is not present")
    


