'''def calculating():
    num1=int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum=num1*num2
    print("Your new number is: " + str(sum))
    return sum

a=calculating()+29
print("WOW: " + str(a))
'''

def calculatin2(x,y):
    print("Your first nuamber: " + str(x) + " \nYour second number: " + str(y))
    sum=x**y
    print("\nYour new number is: " + str(sum))
    return sum

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
idan=calculatin2(a,b) + 29
print("WOW: " + str(idan))