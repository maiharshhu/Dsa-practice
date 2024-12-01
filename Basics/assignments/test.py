"""
You need to make a string.
Enter char = a
Enter char = !
Enter char = 9
Enter char = b
Enter char = c
Enter char = q/Q
a!9bc
"""

# s = ""
# while True:
#     ch = input("Enter a char = ")
#     if ch == "q" or ch == "Q":
#         break
#     s = s + ch
# print(s, reversed)


# /////////////////////////////////////////////////////////

"""
s= aniRUdh

ANIRUDH
"""
s = "anirudh$#$#HDKJWA642842dgwakh^&*^$#*^()"
n = len(s)
result = ""
for i in range(0, n):
    ascii_value = ord(s[i])
    if ascii_value >= 97 and ascii_value <= 122:
        new_ascii_val = ascii_value - 32
        new_ch = chr(new_ascii_val)
        result = result + new_ch
    elif:
        new_ascii_value = ascii_value + 32
        new_ch = chr(new_ascii_val)
        result = result + new_ch
    else:
        result = result + s[i]
print(result)
