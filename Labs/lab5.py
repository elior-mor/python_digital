## Dictionary Lab 5
new_dictionary={"Noam":100,"Adi":200,"Erez":300,"Kobi":400,"Matan":500}
sum=new_dictionary["Noam"]+new_dictionary["Matan"]
print("First & last names sum of money is: " + str(sum))
new_dictionary.update({"Lior":sum} )
print("The new dictionary is: " + str(new_dictionary))
print("Number of entries is: " + str(len(new_dictionary)))
print("idan" in new_dictionary)