i=1
while i<6:
    print(i)
    i=i+1
    
#Gonna print till the value of i is 6

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#Gonna stop when the value of i is 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Gonna skip 3

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Stopping message
  
x=1
while x<10:
    if x%2==0:
        print(str(x)+"is even")
    else:
        print(str(x)+"is odd")
    x=x+1
