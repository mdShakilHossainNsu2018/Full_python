item_list = [1, 2, 3, 4, 5, 6, 7, 8]
string = "1234567890"
#
# for c in string:
# #     print(c)
#
# my_iter = iter(string)
# my_iter2 = iter(item_list)
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print()
# print("$"*9)
# print()
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))
# print(next(my_iter2))

# for i in iter(string):
#     print(i)

my_iter = iter(item_list)
for item in range(0, len(item_list)):
    next_item = next(my_iter)
    print(next_item)






