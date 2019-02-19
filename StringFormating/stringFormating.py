age = 20

print("my age is :"+str(age)+"years")

print("I am {0} years old".format(age))

print("There is {0} days in {1}, {2}, {3}, {4}, {5}, {6}".format(6, "sat", "sun", "mon", "twe", "wed", "last"))

print("""
january:{2}
feb:{0}
march:{2}
april:{1}
may:{1}
june:{2}
july:{1}
auguste:{2}
sep:{1}
oct:{1}
nov:{2}
dec:{1}

""".format(28, 30, 31))
print("my age :%d"% age)

print("I am %d years %s"% (20, "old"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cube is %4d " % (i, i**2, i**3))  #python 2

print("*"*20)

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cube is {2:4} ".format(i, i**2, i**3))  #pyhton 3 and it will start from right

print("#"*20)

for i in range(1, 12):
    print("No. {0:<2} squared is {1:<4} and cube is {2:<4} ".format(i, i**2, i**3))   #pyhton 3 and it will start from left

print("#"*20)

for i in range(1, 12):
    print("No. {:<2} squared is {:<4} and cube is {:<4} ".format(i, i**2, i**3))   #pyhton 3 and it will start from left


print("pi %12.50f" % (22/7))

print("pi {0:12.50f}".format(22/7))












