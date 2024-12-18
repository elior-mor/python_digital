## conditions lab6
from time import sleep
Number=int(input("Menu: \n" + "1.Insert number and ** it by 3 \n" + "2.Insert 4 IPs to a list and print it \n" + "3. Insert 4 entries to DNS_Dictionary and print it \n" + "4. Check if a string is Polindrom \n" + "Please choose one of the 1-4 above. \n"))
if(Number==1):
    number1=int(input("Please insert a number: "))
    number2=number1**3
    print("The number you have entered **3: " + str(number2))
elif(Number==2):
    new_list=input("Please insert 4 IPs to a list: ").split(',')
    print("IPs list: " + str(new_list))
elif(Number==3):
    DNS_Dictionary = str(input("Please insert 4 enteries: "))
    new_dict = dict(item.split(":") for item in DNS_Dictionary.split(","))
    print("Dns_Dictionary: " + str(new_dict))
elif(Number==4):
    string=str(input("Please insert a string: "))
    if(string==string[::-1]):
        print("It's a polindrom!")
    else:
        print("It's not a polindrom!")
else:
    print("You must insert 1-4 only!")




