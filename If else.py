if True:            
    print("True")       #If this condition is correct then print . If not then goes below

elif False:
    print("False")  #If this condition is correct then print . If not then goes below

elif 3<4:
    print("Correct na")    #If this condition is correct then print . If not then goes below
    
else:
    print("None")     #If this condition is correct then print . If not then print nothing

    
if 3>4:
    print("Yes")
    
elif 4>3:
    print("no")

else:
    print("None")

#Shorted
a = 2
b = 330
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested
if 4>3:
    if 3>2:
        print("none")
    elif 3==2:
        print("Why")
    else:
        print("none")
else:
    pass

if False:
    print("f")
elif False:
    print("k")
else:
    print("l")



a, b = 10, 20
min= a if a < b else b 
print(min) 
print( (b, a) [a < b] )
print({True: a, False: b} [a < b])
print((lambda: b, lambda: a)[a < b]())
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")
min = a < b and a or b 
print(min)
var=100
if ( var == 100 ) : print("Value of expression is 100")
print("Good bye!")
    
    
