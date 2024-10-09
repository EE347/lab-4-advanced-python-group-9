name = input("Enter Name: ")
file = open("task3.txt","a")
file.write(name + "\n")
file.close()