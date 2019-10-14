#%%
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt

filename = "C:/Users/hp/Desktop/Work/activity.csv"

dict = {}
dictinterval = {}
dictinterval1weekdays = {}
dictinterval1weekends = {}
intervalof5 = {} 
NA_total = 0

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if(steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(steps))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(steps))
                intervalof5.setdefault(interval,[])
                intervalof5[interval].append(int(steps))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(steps))
                intervalof5.setdefault(interval,[])
                intervalof5[interval].append(int(steps))
        else:
            NA_total += 1
            
                
listDate = []
listTotal = []
listAve = []
listInter = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))

for i in intervalof5:
    listInter.append(st.mean(intervalof5[i]))
    

plt.hist(listTotal)
plt.title("Total Steps per day")
plt.xlabel("Steps per day")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))
plt.show()        

print("Mean: ", st.mean(listTotal))
print("Median: ", st.median(sorted(listTotal)))
print(NA_total)

#%%
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt

filename = "C:/Users/hp/Desktop/Work/activity.csv"

dict = {}
dictinterval = {}
dictinterval1weekdays = {}
dictinterval1weekends = {}

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if(steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(steps))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(steps))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(steps))
                
listDate = []
listTotal = []
listAve = []
listInter = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))

for i in dictinterval:
    listInter.append(st.mean(dictinterval[i]))

plt.title("Average Steps per 5 Minute interval")
plt.xlabel("5 minute interval")
plt.ylabel("Average Steps")
plt.xticks(range(0,2355,5))
plt.plot(listInter)
plt.show()


#%%
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt

filename = "C:/Users/hp/Desktop/Work/activity.csv"

dict = {}
dictinterval = {}
dictinterval1weekdays = {}
dictinterval1weekends = {}
NA_total = 0

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if(steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(steps))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(steps))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(steps))
            
listInter = []               

for i in dictinterval:
    listInter.append(st.mean(dictinterval[i]))
    
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        listnum = 0
        if(steps == "NA"):
            NA_total += 1
            steps = steps.replace("NA", str(listInter[listnum]))
            listnum += 1
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(float(steps)))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(float(steps)))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(float(steps)))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(float(steps)))
                
listDate = []
listTotal = []
listAve = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))

plt.hist(listTotal)
plt.title("Total Steps per day")
plt.xlabel("Steps per day")
plt.ylabel("Frequency")
plt.yticks(range(0,25,5))
plt.show()        

print("Mean: ", st.mean(listTotal))
print("Median: ", st.median(sorted(listTotal)))
print(NA_total)
#%%
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt

filename = "C:/Users/hp/Desktop/Work/activity.csv"

dict = {}
dictinterval = {}
dictinterval1weekdays = {}
dictinterval1weekends = {}
NA_total = 0

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if(steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(steps))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(steps))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(steps))
            
listInter = []               

for i in dictinterval:
    listInter.append(st.mean(dictinterval[i]))
    
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        listnum = 0
        if(steps == "NA"):
            NA_total += 1
            steps = steps.replace("NA", str(listInter[listnum]))
            listnum += 1
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(float(steps)))
            
            dictinterval.setdefault(interval,[])
            dictinterval[interval].append(int(float(steps)))
            
            if(date2%7 == 0):
                dictinterval1weekends.setdefault(interval,[])
                dictinterval1weekends[interval].append(int(float(steps)))
            else:
                dictinterval1weekdays.setdefault(interval,[])
                dictinterval1weekdays[interval].append(int(float(steps)))
                
listDate = []
listTotal = []
listAve = []
listWeekends = []
listWeekdays = []
listInterEnds = []
listInterDays = []

for i in dictinterval1weekdays.keys():
    listWeekdays.append(sum(dictinterval1weekdays.get(i)))
    listInterDays.append(st.mean(dictinterval1weekdays[i]))
    
for i in dictinterval1weekends.keys():
    listWeekends.append(sum(dictinterval1weekends.get(i)))
    listInterEnds.append(st.mean(dictinterval1weekends[i]))

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))

plt.plot(listInterDays)
plt.plot(listInterEnds)
plt.title("Weekdays and ends comparison")
plt.xlabel("5 minute interval")
plt.ylabel("Average Steps")
plt.show()        

print("Mean: ", st.mean(listTotal))
print("Median: ", st.median(sorted(listTotal)))
print(NA_total)