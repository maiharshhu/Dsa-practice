# i = int(input("Enter a number-"))
# if i % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# -----------------------------------------------------------------------
# Que2: print negative,positive or zero
# i = int(input("Enter a number:"))
# if i < 0:
#     print("Negative")
# elif i > 0:
#     print("Positive")
# else:
#     print("Zero")
# ______________________________________________________________________________

# Question:3
# i = int(input("Enter a number:"))
# if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#     print(f"Your number {i} is divisible with 2,3 and 5")
# else:
#     print(f"Your number {i} is  not divisible with 2,3 and 5")
# ----------------------------------------------------------------------------------

#  Q4.
# i = int(input("Enter a number:"))
# if i < 0 and i % 2 != 0:
#     print("Negative and odd")
# elif i < 0 and i % 2 == 0:
#     print("Negative and Even")
# elif i > 0 and i % 2 != 0:
#     print("Positive and Odd")
# elif i > 0 and i % 2 == 0:
#     print("Positive and Even")
# else:
#     print("Zero")
# ______________________________________________________________________________________

# Question 5
sub1 = float(input("Enter subject 1 marks:"))
sub2 = float(input("Enter subject 2 marks:"))
sub3 = float(input("Enter subject 3 marks:"))
av = sub1 + sub2 + sub3 / 3
if av >= 90:
    print("A")
elif 80 >= av <= 89:
    print("B")
elif 80 >= av <= 89:
    print("C")
elif 80 >= av <= 89:
    print("D")
else:
    print("fail")
# ______________________________________________________________________________________

# Question 6
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))
# if a == b == c:
#     print("All numbers are same")
# else:
#     if a >= b and a >= c:
#         print(f"Number {a} is maximum and", end=" ")
#     elif b >= a and b >= c:
#         print(f"Number {b} is maximum and", end=" ")
#     else:
#         print(f"Number {c} is maximum and", end=" ")

#     if a <= b and a <= c:
#         print(f"{a} is minimum number")
#     elif b <= a and b <= c:
#         print(f"{b} is minimum number")
#     else:
#         print(f"{c} is minimum number")
# =====================================================================================

# Question 7
# w = float(input("Enter weight:"))
# h = float(input("Enter height:"))
# bmi = w / h**2
# if bmi >= 30:
#     print("obesity")
# elif 25 <= bmi < 29:
#     print("Overweight")
# elif 18.5 <= bmi < 24.9:
#     print("Normal weight")
# else:
#     print("under weight")
# ========================================================================================
# Question 8
# m = int(input("Enter maths marks:"))
# s = int(input("Enter science marks:"))
# e = int(input("Enter english marks:"))
# total = m + s + e

# if m >= 70 and s >= 65 and e >= 60 and total >= 200:
#     print("You are eligible for college addmission")
# else:
#     print("Your are not eligible for college addmission")
# ========================================================================================
