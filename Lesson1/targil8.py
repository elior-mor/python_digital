##while loops
from time import sleep

while(True):
    choice=input("Menu:\n------\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 entries to DNS_Dictionary and print it\n4.Checkif a string is a Polindron")
    if(choice=="1"):
        print("The new number is: " + str((int(input("enter a number: ")))**3))
    elif(choice=="2"):
        list_ip=[]
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        print("\nThe new list:\n-------------\n" + str(list_ip))
    elif(choice=="3"):
        dns_dict={}
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        print("\nThe new dns_dict:\n-----------\n" + str(dns_dict))
    elif(choice=="4"):
        word=input("Enter a word: ")
        if(word==word[::-1]):
            print("This is a polindrom!")
        else:
            print("This is not a polindrom!")
    else:
        print("Enter 1-4 only!!....\n")

    exit=input("Do you want to exit? y/n\n")
    if(exit=="y" or exit=="yes"):
        break
    else:
        print("Welcome back!\n")

print("Thank you and bye bye")