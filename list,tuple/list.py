# ipAddress = input("Please insert ip: ")
# print(ipAddress.count("."))

# shoppingList = ["cat ", "Bamboo", "dog"]
#
# print(shoppingList)
# shoppingList.append("shop")
# for item in shoppingList:
#     print("There are: {}".format(item))
#

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# number = even+odd
# # print(number.sort())
# # print(number)
# print(sorted(number))

# list_1 = []
# list_2 = list()
# #
# # if list_1 == list_2:
# #     print("The list are equal.")
#
# print(list("This is a list"))
#
# even = [2, 4, 6, 8]
#
# ano_even = even
#
# ano_even.sort(reverse=True)
#
# print(even)

# even = [2, 4, 6, 8]

# ano_even = sorted(even, reverse=True)
# print(even == ano_even)
# print(even is ano_even)
# ano_even.sort(reverse=True)
#
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = [even, odd]
print(number)

for number_set in number:
    print(number_set)
    for item in number_set:
        print(item)











