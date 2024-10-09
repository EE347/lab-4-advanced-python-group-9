import csv
import matplotlib.pyplot as plt
from datetime import datetime

DATE=[]
META=[]
AAPL=[]
AMZN=[]
NFLX=[]
GOOGL=[]
NVDIA=[]
with open("task9.csv") as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count=0
    for row in csv_reader:
        if(line_count==0):
            header=row
            line_count+=1
        else:
            DATE.append(datetime.strptime(row[0],'%d/%m/%Y'))
            META.append(float(row[1]))
            AAPL.append(float(row[2]))
            AMZN.append(float(row[3]))
            NFLX.append(float(row[4]))
            NVDIA.append(float(row[5]))
            GOOGL.append(float(row[6]))
plt.plot(DATE,META)
plt.plot(DATE,AAPL)
plt.plot(DATE,AMZN)
plt.plot(DATE,NFLX)
plt.plot(DATE,NVDIA)
plt.plot(DATE,GOOGL)
plt.show()