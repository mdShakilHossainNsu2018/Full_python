import random

high = 10
answer = random.randint(1, high)
guss_loop = True
while(guss_loop):
    guss = int(input("Please inter your guss: "))
    if guss > answer:
        print("Please guess lower ")
    elif guss == 0:
        print("You are quiting ")
        break
    elif guss == answer:
        print("Congratulation You guss right number {} ".format(answer))
        guss_loop = False
    else:
        print("Please guess Higher")



