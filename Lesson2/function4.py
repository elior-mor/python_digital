def add_ip(list, ip1,ip2,ip3):
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list


ip_list=[]
ip_n1=input("Enter 1st IP: ")
ip_n2=input("Enter 2nd IP: ")
ip_n3=input("Enter 3rd IP: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
#ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)