# for i in range(1, 6):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

# Dynamic pattern
# n = int(input("Enter number: "))
# for i in range(1, n + 1):
#     for j in range(n, i - 1, -1):
#         print(j, end=" ")
#     print()

# using list unpacking
# n = int(input("Enter a number: "))
# for i in range(n):
#     print(*list(range(n, i, -1)))

# while loop
# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     j = n
#     while j >= i:
#         print(j, end=" ")
#         j -= 1
#     print()
#     i += 1
