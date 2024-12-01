# my_list = [56, 43, 12, 45, 6, 4, 6, 7, 34, -100]
# result = []
# for i in range(3, 8):
#     result.append(my_list[i])
# # result = my_list[3:8]
# # result = my_list[0:7]
# # result = my_list[0:7:2]
# # result = my_list[4:]
# # result = my_list[:]
# # result = my_list[::2]
# print(result)

# my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34, -100]
# #           0   1   2   3   4   5   6   7   8   9
# #         -10  -9  -8  -7  -6  -5  -4  -3  -2   -1
# #
# #
# # result = my_list[7:2:-1]
# # result = my_list[::-1]
# # result = my_list[-8:-5]
# # result = my_list[-9:]
# result = my_list[-4:-10:-1]
# print(result)

# --------------------------------------------------
my_list = [56, 43, 12, 45, 62, 41, 16, 97, 34]

n = len(my_list)
left = 0
right = n - 1
while left < right:
    my_list[left], my_list[right] = my_list[right], my_list[left]
    left += 1
    right -= 1
print(my_list)
