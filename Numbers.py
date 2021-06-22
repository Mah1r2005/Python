#3 types of number
Normal_num=4
Float=4.89988
Complex=5j

x=4
y=6
z=5
print(x+y)               #Sum
print(x*y)               #Multiply
print(x**y)              #Power
print(x/y)               #Divide
print(x//y)              #Divide but returns only the whole integer
print(x%y)               #Modulas or reminder
x+=1 #Means x=x+1  (Same for other operators)
print(x)
x%=2
print(x)
print(10000)
print(2.44)
print(5j)

# for NaN
print(float("nan"))
print(float("NaN"))

# for inf/infinity
print(float("inf"))
print(float("InF"))
print(float("InFiNiTy"))
print(float("infinity"))

# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))

# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))
