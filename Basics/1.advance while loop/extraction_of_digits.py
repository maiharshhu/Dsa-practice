num = int(input("Enter a number:"))
# if num < 0:
#     n = num * -1
# else:
#     n = num
# # or
n = abs(num)
while n > 0:
    ld = n % 10
    print(ld, end=" ")
    n = n // 10
