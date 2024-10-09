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
            headers=row
            headers.remove('\ufeffDate')
            line_count+=1
        else:
            DATE.append(datetime.strptime(row[0],'%d/%m/%Y'))
            META.append(float(row[1]))
            AAPL.append(float(row[2]))
            AMZN.append(float(row[3]))
            NFLX.append(float(row[4]))
            NVDIA.append(float(row[5]))
            GOOGL.append(float(row[6]))
plt.plot(DATE,META,color='blue')
plt.plot(DATE,AAPL,color='gray')
plt.plot(DATE,AMZN,color='black')
plt.plot(DATE,NFLX,color='red')
plt.plot(DATE,NVDIA,color='green')
plt.plot(DATE,GOOGL,color='yellow')
plt.legend(headers)
plt.title('Stock Prices of Companies')
plt.xlabel('Date')
plt.ylabel('Stock Prices EUR')
plt.show()