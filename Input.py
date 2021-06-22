m=input("Enter ur name:")
print("Your name is "+m)

m=int(input("Enter a number:"))  #Will take only int as input
print(m)

x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print()

x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 

x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print()

x, y, z = [int(x) for x in input("Enter three value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print()

x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x)

program = input('Enter a program:')
print(exec(program))
