# num = int(input("Enter a number:"))
# nod = 0
# n = num
# while n > 0:
#     n = n // 10
#     nod += 1

# n = num
# total = 0
# while n > 0:
#     ld = n % 10
#     total = total + (ld**nod)
#     n = n // 10
# print(total)
# if total == num:
#     print("Yes")
# else:
#     print("No")

num = int(input("Enter a number"))
n = num
nod = 0
while n > 0:
    nod = nod + 1
    n //= 10
n = num
tot = 0
while n > 0:
    ld = n % 10
    tot = tot + (ld**nod)
    n //= 10
print(f"Total is {tot}")

if tot == num:
    print(f"yes {num} is a armstrong")
else:
    print(f"No {num} is not a armstrong")
