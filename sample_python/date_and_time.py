'''
Created on 18-Dec-2018

@author: divya
'''
from datetime import datetime

now = datetime.now()

mon = str(now.month)

dd = str(now.day)

year = str(now.year)

hour = str(now.hour)

min = str(now.minute)

sec = str(now.second)

print (mon + "/" + dd + "/" + year + " " + hour + ":" + min + ":" + sec)