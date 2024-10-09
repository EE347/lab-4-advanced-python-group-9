name = input("Enter Name: ")
file = open("task3.txt","w")
file.writelines(name)
file.close()