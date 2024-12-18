##Lab7 -  Cube project
from random import randint
total_money=int(input("How much money do you have for playing?"))
print("You have a money for " + str(total_money//3) + " rounds, with a change of " + str(total_money%3) + " shekels.")
prize=0

for i in range(int(total_money//3)):
    print("Round Number " + str(i+1) + " :\n---------------")
    cube1=randint(1,6)
    cube2=randint(1, 6)
    print("Cube1: " + str(cube1) + " \nCube2: " + str(cube2) + "\n")
    if(cube1==cube2):
        if(cube1==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(cube1==1):
        prize=prize+20
    elif(cube2==2):
        prize=prize+40

print("Your prize: " + str(prize) + " shekels")





