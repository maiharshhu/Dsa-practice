# for i in range(1, 6):
#     for j in range(6 - i, 0, -1):
#         print(j, end=" ")
#     print()

# using while loop
# n = int(input("Enter a num: "))
# i = 1
# while i <= n:
#     j = n - i
#     while j > 0:
#         print(j, end=" ")
#         j -= 1
#     print()
#     i += 1

# using list unpacking
# n = int(input("Enter a num: "))
# for i in range(n):
#     print(*list(range(n - i, 0, -1)))
