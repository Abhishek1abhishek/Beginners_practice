start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for start_list in start_list:
  square_list.append(start_list**2)
  square_list.sort()	
  



print (square_list)


a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = []
for a in a:
    b.append(a**2)
    print(b)
    
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for me in a:
  if me % 2 == 0:
  	print ("the even numbers form list is %d"% me)
      
print("%d" % 34.6)
print (max(1,2,3,4,5))


def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

  
fizz= ["fizz","cat","fizz"]
work = fizz_count(fizz)
print (work)

print()
print()

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0
for food in prices:
  print (prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print (total)
print()
print()



def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

n = [1, 2, 5, 10, 13]
print (sum(n))



animal_sounds = {
  "cat": ["meow", "purr"],
  "dog": ["woof", "bark"],
  "fox": [],
}
print (animal_sounds["cat"])










