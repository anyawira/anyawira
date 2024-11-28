var = 1
print(var)
print()
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print()
var = "3.8.5"
print("Python version: " + var)
print()
#to assign a new value to an already existing variable
var = 1
print(var)
var = var + 1
print(var)
print()
var = 100
var = 200 + 300
print(var)
print()
#solving mathematical equations
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print()
#new problem
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)
print()
#shortcuts
x = 3
x = x * 2
print()
x *= 2
print()
sheep = 3
sheep = sheep + 1
print()
sheep += 1
print()
#simple conveter
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print()
#example scenario
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
print()