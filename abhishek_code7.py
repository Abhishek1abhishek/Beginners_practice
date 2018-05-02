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


print ("the current hour time is ::")
print (now.hour)
print ("the current minute time is::")
print(now.minute)
print ("the current second time is ::")
print(now.second)
print ("the time is::")
print (('%02d:%02d:%02d') %(now.hour, now.minute,now.second))


#to print the pass or fail in the subjects
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

            
# to print the lowercase 
z="the HERO is HERE"
z.lower()
print (z.lower())

#to print the length of the string
s= "Abhishek"
x = len(s)
print (x)





#to print both, uppercase and lowercase
c = "My house Is VerY gooD"
c= c.lower()
print (c)
c= c.upper()
print(c)


# Python code for implementation of isalpha()
  
# checking for alphabets
string = 'Ayush'
print(string.isalpha())
  
 
string = 'Ayush0212'
print(string.isalpha())
  
# checking if space is an alphabet
string = 'AyushSaxena'
print( string.isalpha())



pat = "My name is Abhishek Pandit."
sat = " I live in katmandu."
tat = " I am a good boy."
aqua = pat + sat + tat
print (aqua)


def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


#to print the square number
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  root = n **0.5
  print ("%d square number is: %d" % (n, squared))
  print ("%d root number is :%d" % (n, root))
  return squared
  return root

square(float(input("Input a number:")))  


def cube(number):
    i = number **3
    print ("the cube of %d is : %d"% (number,i))
    return i
cube(float(input("Input a number:")))



def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


from math import sqrt
def a(q):
  print (sqrt(q))
  return sqrt
a(int(input("enter the number for square root :")))


# the value of pie is :
import math
print ("the value of pi is : ")
print (math.pi)

#to import math
import math
print("the squre root is:", math.sqrt(81))












