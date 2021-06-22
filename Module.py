def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


import Module
Module.greeting("mahir")
a = Module.person1["age"]
print(a)

import Module as mx
mx.greeting("mahir")

from math import *
print(eval('dir()'))
names = {'square_root': sqrt, 'power': pow}
print(eval('dir()', names))

# Using square_root in Expression
print(eval('square_root(9)', names))


a = 169
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))

from math import *
exec('print(dir())')
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})
# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})
exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})
# object can have squareRoot() module
exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})
globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print, 'dir': dir}
exec('print(dir())', globalsParameter, localsParameter)
x = globals()
print(x["__file__"])
