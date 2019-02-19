# print("Please Guess between 1 to 10: ")
#
# guess = int(input())
#
# if guess>5:
#     print("Please give a lower input: ")
#     guess = int(input())
#     if guess == 5:
#         print("you guess correctly...")
#     else:
#         print("sorry you din't guess correctly")
# elif guess<5:
#     print("Please give a higher input: ")
#     guess = int(input())
#     if guess == 5:
#         print("you guess correctly...")
#     else:
#         print("sorry you din't guess correctly")
# else:
#     print("you guess correctly first time..")
#
#


# age = int(input("How old are you: "))

# if 16 <= age <= 65:
#     print("Have a good day at work..")
#
# if 15 < age < 66:
#     print("Have a good day at work..")

# if (age < 16) or (age > 66):
#     print("Enjoy your free time.")
# else:
#     print("Have a good work day.")

# x = "false"
#
# if x:
#     print("x is true")


# print("""False:{0}
# None: {1}
# 0:{2}
# 0.0:{3}
# empty List []:{4}
# empty tuple ():{5}
# empty string "":{6}
# empty sting '':{7}
# empty mapping {{}}:{8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(""), bool(''), bool({})))
#
# x = input("please enter some thing: ")
#
# if x:
#     print("you have entered: '{}' ".format(x))
# else:
#     print("nothing entered...")


# print(not False)
# print(not True)

#
# x = int(input("What is your age: "))
# if not (x<18):
#     print("you are adult..")
# else:
#     print("you will be adult in {} years ".format(18-x))

shakil = "Md Shakil Hossain"

name = input("Enter the Letter: ")

if name in shakil:
    print("yes Here is {} ".format(name))
else:
    print("No .....")


