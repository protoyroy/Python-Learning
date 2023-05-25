# rows = 3

# for i in range(rows):
#  if i == 0 or i == rows-1:
#      print("* " * rows)
#  else:
#          print("*   *")
rows = 5

for i in range(1, rows + 1, +1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

for i in range(rows-1, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))
