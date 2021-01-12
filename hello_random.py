import random
import time

hello = "Hello World"
string1 = ""
i = 0
while string1 != hello:
    random_num = random.randint(0,127)
    if chr(random_num) == hello[i]:
        string1 += chr(random_num)
        print(string1)
        i+=1
    
    else:
        print(string1 + chr(random_num), end = "\r")
        time.sleep(1)
