from time import sleep

def menu():
    while(True):
        choice1=input("Menu:\n------------\na. IP System\nb.DNS System\n")
        if(choice1=="a"):
            choice2=input("\nMenu IP System:\n-----------\n1.Search for IP address from a list\n2.Add IP address to a list\n3.Delete IP address to a list\n4.Print all the IPs to the screen\n")
            if(choice2=="1"):
                search_ip()
            elif (choice2 == "2"):
                add_ip()
            elif (choice2 == "3"):
                delete_ip()
            elif (choice2 == "4"):
                print_ips()
        elif(choice1=="b"):
            choice3=input("\nMenu DNS System:\n------------\n1.search for URL from a dictionary\n2.add URL+IP address to a dictionary\n3.delete URL from a dictionary\n4.update the IP address of specific URL\n5.Print all the URL:IP to the screen\n")
            if(choice3=="1"):
                search_url()
            elif (choice3 == "2"):
                add_url_ip()
            elif (choice3 == "3"):
                delete_url()
            elif (choice3 == "4"):
                update_ip_dict()
            elif (choice3 == "5"):
                print_dict()
        else:
            print("Enter a or b only!!!")
            continue
        exit=input("Do you want to exit? yes/no")
        if(exit=="yes"):
            print("Bye Bye")
            break

def search_ip():
    Print("1")

def add_ip():
    Print("2")

def delete_ip():
    Print("3")

def print_ips():
    Print("4")

def search_url():
    Print("a")

def add_url_ip():
    Print("b")

def delete_url():
    Print("c")

def update_ip_dict():
    Print("d")

def print_dict():
    Print("e")
