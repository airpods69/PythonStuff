#mypy
from datetime import datetime
import webbrowser
from csv import reader
import time
import os

def myfunc():
    with open('TimeTable2.csv','r') as schedule:
        csvreader = reader(schedule)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        day = now.strftime('%A')
        print(day)
        print(current_time)

        for row in csvreader:
            if row[0] == day:
                if current_time==row[2]:
                    zoom_link = row[1]
                    print(zoom_link)
                    webbrowser.open(zoom_link)
                    os. system("taskkill /f /im "+"brave.exe")
                    return 1
                
                else:
                    return 0

triggered = myfunc()
while triggered != 1:
    print("Wait for class to begin!")
    time.sleep(50)
    triggered = myfunc()