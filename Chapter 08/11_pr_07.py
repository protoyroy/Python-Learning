def remove_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this= "     Protoy is good    "
n = remove_split(this, "Protoy")  # unnecesary space deleting remove_split
print(n)