print(2>3)   #Returns False
print(2==3)  
print(2<3)   #Returns True
z=2>3
print(z)
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
#True
print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#False
print(bool(False))     
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = 200
print(isinstance(x, int))           #Check int or not
print("hello"=='hello')  #True
print(7==7.0)            #True
print("Anta">"and")      #True (Anta(4)>and(3))
print(7>7.0)             #False
print(8.7==8.70)         #True
print(7<7.0)             #False
print(8.7>8.70)          #False
print(id(True))   

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
