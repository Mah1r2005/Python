#Arithmetic
print(1+2)         #Addition
print(2*3)         #Multiplication
print(2/3)         #Division
print(3//2)        #Floor division
print(3**2)        #Power
print(2-1)         #Subtraction
print(3%2)         #Modular
#Comparison and logical
x=3
print(3>2)         #Greater than
print(3!=2)        #Not greater than
print(3<2)         #lesser
print(3==2)        #Equal
print(3>=2)        #Greater than or equal
print(3<=2)        #Lesser than or equal
print(3 and 2)
print(x<3 and x<10) # Returns True if both are true
print(x<3 or x>3)   # Returns True if one of them is True
print(not(3 or 2))  # Reverse the result
print(3 is 2)
print(2 is not 4)
print("3" in "3")
print("3" not in "x")
#Bitwise
print(2&3)       #AND
print(3|2)       #OR
print(3^2)       #XOR
#print(3~x)       #NOT
print(3<<2)      #Zero fil left
print(3>>2)      #signed right swift


"""
&  	AND 	Sets each bit to 1 if both bits are 1
| 	OR 	Sets each bit to 1 if one of two bits is 1
 ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
~  	NOT 	Inverts all the bits
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""
print(False == (True or False))    #False
print(False == False or True)      #True
print((False == False) or True)      #True
print(False or True or False)      #True
  
