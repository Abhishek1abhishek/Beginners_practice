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
print("........................................................")
print("........................................................")
from datetime import datetime
now = datetime.now()

print ("todays date and time is being shown::::")
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

b = int(input("enter a  number"))
c = int(input("enter a numer")) 

if b >= 30 and c >= 30:
    print ("pass in math")
    print ("pass in science also")
elif b<30 and c>= 30:
    print ("you are fail in maths ")
    print ("you are pass in science")
elif b>=30 and c< 30 :
    print ("you are pass in math")
    print ("you are fail in science")
else:
    print ("you are failed in both subjects")
    print("read hard")

            

z="the HERO is HERE"
z.lower()
print (z.lower())

s= "Abhishek"
x = len(s)
print (x)

a= "Hellow"
b = len(a)
c=0
for j in b:
    q= a[c]
    print (c)
    c +=1
            























