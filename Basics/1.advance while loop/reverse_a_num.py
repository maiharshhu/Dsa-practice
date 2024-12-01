# num = int(input("Enter a number:"))
# n = num
# rev = 0
# while n > 0:
#     ld = n % 10
#     rev = (rev * 10) + ld
#     n //= 10
# print(rev)


num = int(input("Enter a number:"))
# n = num
n = abs(num)  # To convert -ve to +ve
ans = 0
while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n //= 10
print(ans)
