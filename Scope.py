def fun():
    x=300
    print(x)
    
fun()
#print(x)  x not ddefined. Variable defined in function cant be used outside.
y=5
def fun():
    print(y)

fun()
print(y)

#Global variable
def fun():
   global x
   x=56
   print(x)

fun()
print(x)
