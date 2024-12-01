# find factors
# Method -1
# num = int(input("Enter a number:"))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")

# Method -2
# num = int(input("Enter a number:"))
# for i in range(1, (num // 2) + 1):
#     if num % i == 0:
#         print(i, end=" ")
# print(num)

# Method-3
# num = int(input("Enter a number:"))
# for i in range(1, int(num**0.5) + 1):
#     if num % i == 0:
#         print(i, end=" ")
# # To sort out all factors
# for i in range(int(num**0.5), 0, -1):
#     if i != num // i:
#         print(num // i, end=" ")
