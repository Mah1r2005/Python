#Kinda if else
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

#Assertation
print(1)
assert 2+2==4


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 

