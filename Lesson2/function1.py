from random import randint
from time import sleep
##########################
def Market():
    tomato = int(input("how much tamatos do you want?"))
    cucumber = int(input("how much cucumbers do you want?"))
    cola = int(input("how much colas do you want?"))
    chicken = int(input("how much chickens in KG do you want?"))
    Sum = int(float(((tomato * 3) + (cucumber * 2) + (cola * 5) + (chicken * 20)) * 1.17))
    print("total cost: " + str(Sum))
##########################
####### Main code#########
for i in range(10):
    Market()