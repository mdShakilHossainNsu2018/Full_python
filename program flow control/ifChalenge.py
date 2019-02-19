name = input("Enter your name: ")
age = int(input("Enter your age {}: ".format(name)))
if 17 < age < 31:
    print("{0} you are welcome in the holiday".format(name))
else:
    print("{0} you will be able to go to holiday when you will be {1} ".format(name, 18-age))




























