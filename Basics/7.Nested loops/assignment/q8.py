# for i in range(1, 6):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

# while loop
# n = int(input("Enter num: "))
# i = 1
# while i <= n:
#     j = i
#     while j <= n:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

# using list unpacking
# Approach:
# We'll generate a list of numbers in each iteration, starting from i to n.
# Then, we'll use the unpacking operator * in the print statement to unpack the list and print the numbers on the same line.
# Code with list unpacking:
n = int(input("Enter num: "))
for i in range(1, n + 1):
    print(*range(i, n + 1))
# Explanation:
# range(i, n + 1): This generates numbers starting from i to n (inclusive).
# * (unpacking): The * operator unpacks the range object into individual elements, so they are printed space-separated without needing an explicit loop inside the print statement.
