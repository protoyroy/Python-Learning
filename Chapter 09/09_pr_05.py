words = ["donkey", 'word', "what", "slang"]

with open("Chapter 09/five.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "$5&#")   #replacing four.txt donkey to $5&#
    with open("Chapter 09/five.txt", 'w') as f:
        f.write(content)