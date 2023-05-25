post = input("Enter a post\n")

if "protoy" in post.lower():
   print("YES!")
elif "protoy" in post.casefold():
   print("YES")
else:
   print("No")
   