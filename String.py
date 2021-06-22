print("I am mahir")
print('I am mahir')
print("""
Multiline
String
""")
mls="""
Hi
I
am
mahir
"""
print(mls)
mls='''
Hi
I
am
mahir
'''
print(mls)
x="mahir"
print("%s"%x)
print(x[0])        #Outputs (0+1)or 1st character of the string.Here position starts at 0
y="m a h i r"
print(y[4])        #Counts space also..Outputs "h".
print(len(x))      #Outputs the length of the string
print(len(y))      #Counts spaces also
print("m" in x)    #Output True if present
print("f" in x)    #False if absent
print(x[1:3])      #Outputs from (1+1) or 2nd character to (3+1) or 4th character
print(x[:3])       #Starts outputing from beginning and stops at (3+1) or 4th character
print(x[2:])       #Starts outputing from (2+1) or 3rd character and stops at the end
print(x[1])        #Outputs 1st character from backward
print(x[-3:-1])    #Outputs from  3rd character from backward to 1st character from backward

print(x.upper())   #Outputs uppercase of the string

print(x.lower())   #Lowercase

print(y.strip())   #Removes whitespace
string = 'android is awesome'
print(string.strip('an'))

print(x.replace("h", "J")) #Replace

print(y.split(","))   #Splits
grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))
grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())


print(x.capitalize())	#Converts the first character to upper case

print(x.casefold())	#Converts string into lower case

print(x.center(20))	#Returns a centered string
print(x.center(20,"O"))

print(x.count("m"))       #Returns the number of times a specified value occurs in a string
print(x.count("h",2,5))

print(x.encode())	#Returns an encoded version of the string
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "H\te\tl\tl\to"
print(x.endswith("."))	#Returns true if the string ends with the specified value
print(x.endswith("my world.", 5, 11))

print(txt.expandtabs())
print(txt.expandtabs(2))	#Sets the tab size of the string

print(x.find("m"))	        #Searches the string for a specified value and returns the position of where it was found
print(x.find("j"))              #returns -1
print(x.find("h",2,5))




txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
txt = "We have {:<8} chickens."         #Use "<" to left-align the value
print(txt.format(49))
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))
#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))
String1 = "|{:<10}|{:^10}|{:>10}|".format('mahir','for','mahir') 
print(String1)
String1 = "{0:.2f}".format(1/6) 
print(String1)
Integer1 = 12.3456789

print('The value of Integer1 is %3.2f' %Integer1) 
print('The value of Integer1 is %3.4f' %Integer1) 
x="mahir"










print(x.format_map("g"))	#Formats specified values in a string
print(x.format_map("h"))

print(x.index("m"))	        #Searches the string for a specified value and returns the position of where it was found
print(x.index("h",2,5))

x1 = "Company12"
print(x1.isalnum())	#Returns True if all characters in the string are alphanumeric

print(x1.isalpha())	#Returns True if all characters in the string are in the alphabet

print(x1.isdecimal())	#Returns True if all characters in the string are decimals

print(x1.isdigit())	#Returns True if all characters in the string are digits
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(x1.isidentifier())	#Returns True if the string is an identifier

print(x.islower())	#Returns True if all characters in the string are lower case

print(x1.isnumeric())	#Returns True if all characters in the string are numeric

print(x.isprintable())	#Returns True if all characters in the string are printable

print(x.isspace())	#Returns True if all characters in the string are whitespaces

print(x.istitle()) 	#Returns True if the string follows the rules of a title

print(x.isupper())	#Returns True if all characters in the string are upper case

myTuple = ("John", "Peter", "Vicky")
print("#".join(myTuple))        #Joins the elements of an iterable to the end of the string
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x2 = mySeparator.join(myDict)
print(x2)

x2 = txt.ljust(20)
print(x2, "is my favorite fruit.")        #Returns a left justified version of the string
print(x.ljust(20, "O"))


print(x.lower())	        #Converts a string into lower case

print(x.lstrip())	#Returns a left trim version of the string
website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))

print(x.maketrans("M","F"))	#Returns a translation table to be used in translations
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))
# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))

print(x.partition("h"))	#Returns a tuple where the string is parted into three parts
print(x.partition("k"))

print(x.rfind("i"))	        #Searches the string for a specified value and returns the last position of where it was found
print(x.rfind("i",0,2))

print(x.rindex("m"))	#Searches the string for a specified value and returns the last position of where it was found
print(x.rindex("m",0,5))

print(x.rjust(10))	        #Returns a right justified version of the string
print(x.rjust(10,"O"))

print(x.rpartition("m"))	#Returns a tuple where the string is parted into three parts

print(x.rsplit(","))	#Splits the string at the specified separator, and returns a list

txt = "apple, banana, cherry"
print(txt.rsplit(", ", 1))
print(y.rstrip())	#Returns a right trim version of the string
website = 'www.programiz.com/'
print(website.rstrip('m/.'))

txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())	#Splits the string at line breaks and returns a list
print(txt.splitlines(True))

print(x.startswith("m"))	#Returns true if the string starts with the specified value
print(x.startswith("h",2,5))

print(x.strip())	        #Returns a trimmed version of the string

print(x.swapcase())	#Swaps cases, lower case becomes upper case and vice versa

print(x.title())	        #Converts the first character of each word to upper case

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))	#Returns a translated string
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))
      
print(x.upper())	        #Converts a string into upper case

txt = "50"
print(x.zfill(10))	        #Fills the string with a specified number of 0 values at the beginning

x='mahir'
del x
#X is deleted
String1 = "This is x47x65x65x6bx73 in x48x45x58"
print(String1)
String1 = r"This is x47x65x65x6bx73 in x48x45x58"
print(String1)

x="mahir"
print(ascii(x))
print(x.splitlines(3))
print(x.splitlines(1))
print(x.split)
print('TestHook'.removeprefix('Test'))
print('MiscTests'.removesuffix('Tests'))
print(b'\xf0\xf1\xf2'.hex())
print(bytes.fromhex('2Ef0 F1f2  '))
value = b'\xf0\xf1\xf2'
print(value.hex('-'))
print(value.hex('_', 2))
print(b'UUDDLRLRAB'.hex(' ', -4))
print(bytearray.fromhex('2Ef0 F1f2  '))
print(bytearray(b'\xf0\xf1\xf2').hex())
a = b"abc"
b = a.replace(b"a", b"f")
print(b)
print(b'TestHook'.removeprefix(b'Test'))
print(b'BaseTestCase'.removeprefix(b'Test'))
print(b'MiscTests'.removesuffix(b'Tests'))
print(b'read this short text'.translate(None, b'aeiou'))
print("abc".isascii())
v = memoryview(b'abcefg')
print(v[1])
print(v[-1])
print(v[1:4])
print(bytes(v[1:4]))
data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)
v[0] = ord(b'z')
print(data)
v[2:6] = b'spam'
print(data)
v = memoryview(b'abcefg')
print(hash(v) == hash(b'abcefg'))
print(hash(v[2:4]) == hash(b'ce'))
print(hash(v[::-2]) == hash(b'abcefg'[::-2]))
m = memoryview(b"abc")
print(m.tobytes)
print(bytes(m))
m = memoryview(b"abc")
print(m.hex())
print(memoryview(b'abc').tolist())
[97, 98, 99]
import array
a = array.array('d', [1.1, 2.2, 3.3])
m = memoryview(a)
print(m.tolist())
mm = m.toreadonly()
print(mm.tolist())
m = memoryview(b'abc')
print(m.release())
with memoryview(b'abc') as m:
  print(m[0])
b = bytearray(b'zyz')
x = memoryview(b)
y = x.cast('c')
y[0] = b'a'
print(b)
b  = bytearray(b'xyz')
m = memoryview(b)
print(m.obj is b)

#Byte
a = 'GeeksforGeeks'
c = b'GeeksforGeeks'
d = a.encode('ASCII') 
if (d==c): 
    print ("Encoding successful") 
else : print ("Encoding Unsuccessful") 
print(~False)
print(~True)

Str = "this is string example....wow!!!";
Str = Str.encode();

print (Str)
print (Str.decode())
print(any(""))
print(any("mahir"))
print(any("000"))
print(all(""))
print(all("mahir"))
print(all("000"))

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

size = 5
arr = bytearray(size)
print(arr)

rList = [1, 2, 3, 4, 5]
arr = bytearray(rList)
print(arr)

x = 5
print(callable(x))

def testFunction():
  print("Test")
y = testFunction
print(callable(y))

class Foo:
  def __call__(self):
    print('Print Something')
print(callable(Foo))

class Foo:
  def printLine(self):
    print('Print Something')
print(callable(Foo))

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct)

print(print(1))
# d, f and b are type

# integer
print(format(123, "d"))

# float arguments
print(format(123.4567898, "f"))

# binary format
print(format(12, "b"))

# integer 
print(format(1234, "*>+7,d"))

# float number
print(format(123.4567, "^-09.3f"))

"""
    * - It is the fill character that fills up the empty spaces after formatting
    > - It is the right alignment option that aligns the output string to the right
    + - It is the sign option that forces the number to be signed (having a sign on its left)
    7 - It is the width option that forces the number to take a minimum width of 7, other spaces will be filled by fill character
    , - It is the thousands operator that places a comma between all thousands.
    d - It is the type option that specifies the number is an integer.

When formatting the floating point number 123.4567, we've specified the format specifier ^-09.3f. These are:

    ^ - It is the center alignment option that aligns the output string to the center of the remaining space
    - - It is the sign option that forces only negative numbers to show the sign
    0 - It is the character that is placed in place of the empty spaces.
    9 - It is the width option that sets the minimum width of the number to 9 (including decimal point, thousands comma and sign)
    .3 - It is the precision operator that sets the precision of the given floating number to 3 places
    f - It is the type option that specifies the number is a float.
"""
print(globals())
age = 23
globals()['age'] = 25
print('The age is:', age)

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)

print(locals())
locals()

test = object()
print(type(test))
print(dir(test))

var = 'foo'
print(repr(var))

# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))

# contains indices (0, 1, 2)
result1 = slice(3)
print(result1)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))

# bytes
b = bytes('pythön', encoding='utf-8')

print(str(b, encoding='ascii', errors='ignore'))

mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))


text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result)
# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))
# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))

#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())

# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())

str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())

s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())

s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())

# .join() with dictionaries
test = {'mat': 1, 'that': 2}
s = '->'

# joins the keys only
print(s.join(test))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

n = -37
print(bin(n))
print(n.bit_length())

print(1+3j.conjugate())

num = 7
print(num.bit_length()) 
  
num = -7
print(num.bit_length()) 


# Returns byte representation of 1024 in a 
# big endian machine. 
print((1024).to_bytes(2, byteorder ='big')) 


# Returns integer value of 'x00x10' in big endian machine.
print(int.from_bytes(b'x00x10', byteorder ='big'))

x = compile('print(55)', 'test', 'eval')
exec(x) 
"""
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Returns the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the Unicode of the specified character
pow()	Returns the value of x to the power of y
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
@staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators
"""
