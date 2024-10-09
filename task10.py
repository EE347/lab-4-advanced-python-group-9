import csv
import matplotlib.pyplot as plt
from datetime import datetime

DATE=[]
META=[]
AAPL=[]
AMZN=[]
NFLX=[]
GOOGL=[]
NVDA=[]
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
            NVDA.append(float(row[5]))
            GOOGL.append(float(row[6]))

#print(str("$.2f" % round(100*(META[250]/META[0]))))
#"{:.2f}".format(round(100 * (META[250] / META[0]), 2))
plt.plot(DATE,META,color='blue')
plt.plot(DATE,AAPL,color='gray')
plt.plot(DATE,AMZN,color='black')
plt.plot(DATE,NFLX,color='red')
plt.plot(DATE,NVDA,color='green')
plt.plot(DATE,GOOGL,color='yellow')
plt.legend(["META: {:.2f}%".format(round(100 * (META[250] / META[0]), 2)),"AAPL: {:.2f}%".format(round(100 * (AAPL[250] / AAPL[0]), 2)),"AMZN: {:.2f}%".format(round(100 * (AMZN[250] / AMZN[0]), 2)),"NFLX: {:.2f}%".format(round(100 * (NFLX[250] / NFLX[0]), 2)),"NVDA: {:.2f}%".format(round(100 * (NVDA[250] / NVDA[0]), 2)),"GOOGL: {:.2f}%".format(round(100 * (GOOGL[250] / GOOGL[0]), 2))])
plt.title('Stock Prices of Companies')
plt.xlabel('Date')
plt.ylabel('Stock Prices EUR')
plt.show()