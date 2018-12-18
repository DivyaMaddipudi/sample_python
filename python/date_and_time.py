'''
Created on 18-Dec-2018

@author: divya
'''

from datetime import datetime

now = datetime.now()

mon = str(now.month)

date = str(now.day)

year = str(now.year)

hour = str(now.hour)

min = str(now.minute)

sec = str(now.second)

print (date + "/" + mon + "/" + year + " " + hour + ":" + min + ":" + sec)
