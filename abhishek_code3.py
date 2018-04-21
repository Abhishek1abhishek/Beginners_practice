# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 07:56:52 2018

@author: Dell
"""

day = 6
print ("03 - %s - 2019" % day)
# 03 - 6 - 2019
print( "03 - %02d - 2019"  % day)

# 03 - 06 - 2019



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
