shoppingList = ["egg", "bread", "pasta", "spam", "banana", "rice"]

# for list in shoppingList:
#     if list == "spam":
#         continue
#     print("My shop: "+list)


for item in shoppingList:
    if item == "spam":
        break
    print("My shop: " + item)
