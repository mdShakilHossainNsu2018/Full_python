# for i in range(10):
#     print("i is now {}".format(i))

exits = ["jaw", "jaa"]
input_chosen = ''
while input_chosen not  in exits:
    input_chosen = input("Input :")
    if input_chosen == "quit":
        print("you lost")
        break
else:
    print("your out of game")

