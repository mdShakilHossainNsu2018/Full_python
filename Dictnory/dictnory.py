fruit = {
    "orange": "It is a sour fruit",
    "apple": "It is a good fruit",
    "banana": "It is a fruit like stick",
    "lime": "Lime is a fruit",
    "coconut": "Coconut is maybe a fruit"
}
# print(fruit)
# print(fruit["orange"])
# fruit["graps"] = "it is small Fruit"
# print(fruit)
# fruit["lemon"] = "now it is upto dated"
# print(fruit)
# del fruit["lemon"]
# print(fruit)

# # del fruit
# fruit.clear()
# print(fruit)
print(fruit)
#
# while True:
#     dic_key = input("Enter the fruit name: ")
#     if dic_key == "quit":
#         break
#     f = fruit.get(dic_key, "sorry You don't have such a fruit :"+dic_key)
#     print(f)
#     # if dic_key in fruit:
#     #     f = fruit.get(dic_key)
#     #     print(f)
#     # else:
#     #     print("sorry You don't have such a fruit :"+dic_key)

# for f in fruit:
#     print(f)
#
# for f in fruit:
#     print(fruit[f])
#

# for snack in fruit:
#     print(fruit[snack])
#
# for i in range(10):
#     for snack in fruit:
#         print(snack+" is "+fruit[snack])
#     print("*"*49)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
'''this is another method'''
# ordered_keys = sorted(list(fruit.keys()))
# for i in ordered_keys:
#     print(i +"="+fruit[i])

# for i in sorted(list(fruit.keys())):
# #     print(i + "=" + fruit[i])
#     '''same conjunctive'''
# for i in sorted(fruit.keys()):
#     print(i + "=" + fruit[i])

# for i in sorted(fruit):
#     print(i + "=" +fruit[i])
# for i in fruit:
#     print(i + "=" +fruit[i])
#
#
# print(fruit.keys())
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)
# fruit["Tomato"] = "Tomato is red"
# print(fruit_keys)
print(fruit.items())
f_tuple = tuple(fruit.items())
print("*"*60)
print(f_tuple)

for i in f_tuple:
    key, dis = i
    print(key+"="+dis)

print(dict(f_tuple))
























