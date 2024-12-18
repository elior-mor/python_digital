##Lists
my_list=["hello",1,66.6,"Idan",55,77.7]
print("The length is: " + str(len(my_list)))

my_list.append("wow")
my_list.append("idan")
print(my_list)
print("The new length is: " + str(len(my_list)))

my_list.insert(7,2)
print(my_list)

my_list.pop(7)
print(my_list)

my_list2=["google","facebook","ebay","apple"]
print("net4u" in my_list)
