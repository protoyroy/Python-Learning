f = open('Chapter 09/poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present!")
else:
    print("Twinkle is not present")
word = 'twinkle'
count = t.lower().count(word.lower()) + t.count(word.capitalize())
print(count) #to count how many times twinkle is present
f.close()

