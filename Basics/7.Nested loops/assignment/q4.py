# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

# Dyanmic
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n, i - n, -1):
        print(j, end=" ")
    print()
