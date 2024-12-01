num = int(input("Enter a number:"))
n = num
rev = 0
while n > 0:
    ld = n % 10
    rev = (rev * 10) + ld
    n //= 10
print(rev)

if rev == num:
    print("Yes")
else:
    print("NO")
