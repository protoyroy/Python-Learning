def calculate_sum(n):
    if n==0:
        return(0)
    else:
        return n + calculate_sum(n-1)
n = int(input("enter the number:"))
if n < 0:
    print("Error: Please enter a non-negative number.")
else:
    f= calculate_sum(n)
    print("The sum of first n naturam number is " + str(f))

# def calculate_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + calculate_sum(n - 1)
# n = 10  # Replace 10 with the desired value
# result = calculate_sum(n)
# print("Sum of the first", n, "natural numbers:", result)

# def factorial_recursive(n):
#     if n==1 or n == 0:
#         return 1
#     return n * factorial_recursive(n-1)
# # f = factorial_recursive(5)
# f= factorial_iter(5)
# print(f)

