# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 07:56:52 2018

@author: Dell
"""



name = "Mike"
print ("Hello %s" % name)


name  = "Abhishek"
quest = "Hello"
color = "Blue"

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color))


from datetime import datetime
now = datetime.now()
print(now)
current_year = now.year
current_month = now.month
current_day = now.day
print ("the current year is:")
print (current_year)
print("the current month is :")
print (current_month)
print ("the current day is:")
print (current_day)
print(('%02d/%02d/%04d') %(now.month, now.day, now.year))



print (now.hour)
print(now.minute)
print(now.second)
print (('%02d:%02d:%02d') %(now.hour, now.minute,now.second))
