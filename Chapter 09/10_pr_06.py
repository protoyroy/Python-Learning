with open("chapter 09/log.txt") as f:
    content = f.read().lower()

if 'python' in content:    #content.lower (i can use here also)   #as it works as case sensitive
    print("Yes python is present")
else:
    print("No python is not present")