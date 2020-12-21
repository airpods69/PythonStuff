#mypy
from datetime import datetime
from csv import reader
import time

def myfunc():
    List=[]
    s=""
    with open('TimeTable2.csv','r') as schedule:
        csvreader = reader(schedule)
        now = datetime.now()
        day = now.strftime('%A')
        s += "The day is "+day+"\n"
        for row in csvreader:
            if row[0] == day:
                x= " Link-> "+row[1]+" Time->"+row[2]+" Subject->"+row[3]+" \n"
                s+= x
        print(s)

myfunc()