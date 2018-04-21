# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 07:56:52 2018

@author: Dell
"""



name = "Abhishek"
print ("Hello %s" % name)


name  = "Abhishek"
quest = "Hello"
color = "Blue"

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color))

# to show date and time
from datetime import datetime
now = datetime.now()

print ("todays date and time is")
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




p = 300 / 10 / 10
print(p)


bool_one = not True

bool_two = not 3 ** 4 < 4 ** 3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

bool_five = not not False

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)



























