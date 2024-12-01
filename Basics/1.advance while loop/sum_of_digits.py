n = int(input("Enter a number:"))
num = n
total = 0
while num > 0:
    ld = num % 10
    total = total + ld
    num //= 10
print(total)
