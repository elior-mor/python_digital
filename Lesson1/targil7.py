##While loops
while(true):
    name=input("Enter a name: ")
    if(name=="idan"):
        print("Hello Idan")
        break
    elif(name=="ben"):
        continue
    else:
        print("Where is Idan?")

    number=int(input("Enter a number: "))
    print(number*4)

print("Bye Bye...")