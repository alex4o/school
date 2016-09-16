#!/bin/python

# #*#*#**#*#*#/#
import csv
import sys
from datetime import time,date,datetime,timedelta
timetable = []

now = datetime.now()
start = datetime(hour=7,minute=30,year=now.year,month=now.month,day=now.day)
timeperiod = 0
subject_no = 0

while start < now:
    if(timeperiod == 5):
        start += timedelta(minutes=20)
    elif timeperiod == 11:
        start += timedelta(minutes=5)
    elif timeperiod%2==0:
        start += timedelta(minutes=40)
        subject_no += 1
    else:
        start += timedelta(minutes=10)

    timeperiod += 1



#print(timeperiod, subject_no)
if subject_no > 7 or subject_no == -1:
    print("Свобода")
    exit()

if timeperiod%2 == 0:
    sys.stdout.write("Междучасие > ")

with open("timetable.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        timetable.append(row)

weekday = date.today().weekday()

if weekday in range(len(timetable)):
    #subject_no = input("Subject: ")
    subject_name = timetable[weekday][str(subject_no)]

    if timeperiod%2:
        sys.stdout.write(subject_name[0].upper() + subject_name[1:] + " > ")

    subject_no += 1


    subject_name = timetable[weekday][str(subject_no)]
    sys.stdout.write(subject_name[0].upper() + subject_name[1:] + "\n")
else: 
    #weekday = int(input("Weekday: "))
    weekday = 2
    print(timetable[weekday][str(subject_no)])
