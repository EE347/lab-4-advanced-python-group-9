import csv

file=open("task5.csv","w")
while(1):
    name=input("Enter Name: ")
    if(name == "quit"):
        break
    file.write(name+"\n")
file.close()