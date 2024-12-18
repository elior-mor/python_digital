''' file handling

#Write 192.168.1.1/2
filename = "C:/Users/.../Documents/Pycharm/hello.txt"
file = open(filename, "r+")
print(file.read())
file.write("192.168.1.1\n192.168.1.2")
print(file.read())
file.close()

#it will append
file = open(filename, "a+")
file.write("\n192.168.1.3\n192.168.1.4")
file.close()

#print to the screen the new output of the file
file=open(filename, "r")
print(file.read())
file.close()
'''
filename = "C:/Users/.../Documents/Pycharm/hello.txt"
file=open(filename, "r")
for line in file:
    print(line)
file.close()
