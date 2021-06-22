#Uses loops for returning object separately
x="mahir"
for i in x:
 print(x)         #Will print mahir 5 times

fruits=[1,2,3,4]
for j in fruits:
    print(j)         #Will print  elements in fruits separately

for i in "jajama":
   print(i)           #Will print the letters separately


#Will stop in banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Stop after banana
for x in fruits:
  if x == "banana":
    break
  print(x)

#Skip banana
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Print from 0 to 5
for x in range(6):
  print(x)

#2 to 5
for x in range(2, 5):
  print(x)

#2 to 29 with difference 3 between each term
for x in range(2, 30, 3):
  print(x)

#Message will appear after ending loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Wont appear
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#No output
for x in [0, 1, 2]:
  pass

#Range
n=list(range(10))  #1 to 9
print(n)

n=list(range(1,10)) #1 to 9
print(n)

n=list(range(1,10,3)) #1,4,7
print(n)

for i in range(10):
    print("mahir")   #repeat 10 times

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
    print(key, value)

questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 
  
# using zip() to combine two containers  
# and print values 
for question, answer in zip(questions, answers): 
    print('What is your {0}?  I am {1}.'.format(question, answer))

d = { "geeks" : "for", "only" : "geeks" } 
  
      
# using items to print the dictionary key-value pair 
print ("The key value pair using items is : ") 
for i,j in d.items(): 
    print (i,j)

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya' 
        } 
  
# using items to print the dictionary key-value pair 
for key, value in king.items(): 
    print(key, value)

def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    while True: 
        name = (yield) 
        if prefix in name: 
            print(name) 
  
# calling coroutine, nothing will happen 
corou = print_name("Dear") 
corou.__next__() 
  
# sending inputs 
corou.send("Atul") 
corou.send("Dear Atul") 

cars = ["Aston" , "Audi", "McLaren "] 
for i, x in enumerate(cars): 
    (print (x))
    
cars = ["Aston" , "Audi", "McLaren "] 
for x in enumerate(cars): 
    (print (x[0], x[1]))
    
cars = ["Aston" , "Audi", "McLaren "] 
print (enumerate(cars)) 


# Two separate lists 
cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS kit", "Car repair-tool kit"] 
  
# Single dictionary holds prices of cars and  
# its accessories. 
# First three items store prices of cars and 
# next two items store prices of accessories. 
prices = {1:"570000$", 2:"68000$", 3:"450000$", 
          4:"8900$", 5:"4500$"} 
  
# Printing prices of cars 
for index, c in enumerate(cars, start=1): 
    print ("Car: %s Price: %s"%(c, prices[index])) 
  
# Printing prices of accessories 
for index, a in enumerate(accessories,start=1): 
    print ("Accessory: %s Price: %s" 
           %(a,prices[index+len(cars)])) 


cars = ["Aston", "Audi", "McLaren"] 
accessories = ["GPS", "Car Repair Kit",  
               "Dolby sound kit"] 
  
# Combining lists and printing 
for c, a in zip(cars, accessories): 
    (print ("Car: %s, Accessory required: %s" 
          %(c, a)))

l1,l2 = zip(*[('Aston', 'GPS'),  
              ('Audi', 'Car Repair'),  
              ('McLaren', 'Dolby sound kit')  
           ]) 
  
# Printing unzipped lists       
print(l1) 
print(l2)










    
