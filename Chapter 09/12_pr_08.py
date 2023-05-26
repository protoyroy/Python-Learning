with open('Chapter 09/this.txt') as f:
    content = f.read()

with open("Chapter 09/copy.txt", 'w') as f:
    f.write(content)