# Calculator program in Python

# Import math library for advanced math functions
import math

# Function to add two numbers
def add(x, y):
   return x + y

# Function to subtract two numbers
def subtract(x, y):
   return x - y

# Function to multiply two numbers
def multiply(x, y):
   return x * y

# Function to divide two numbers
def divide(x, y):
   return x / y

# Function to calculate square root of a number
def square_root(x):
   return math.sqrt(x)

# Function to calculate exponential of a number
def exponential(x):
   return math.exp(x)

# Function to calculate logarithm of a number
def logarithm(x):
   return math.log(x)

# Function to calculate trigonometric sine of a number
def sine(x):
   return math.sin(x)

# Function to calculate trigonometric cosine of a number
def cosine(x):
   return math.cos(x)

# Function to calculate trigonometric tangent of a number
def tangent(x):
   return math.tan(x)

# Prompt user for operation choice
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square root")
print("6.Exponential")
print("7.Logarithm")
print("8.Sine")
print("9.Cosine")
print("10.Tangent")

# User input for operation choice
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

# Perform selected operation based on user input
if choice in ('1', '2', '3', '4'):
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))

   if choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   num = float(input("Enter a number: "))
   print("Square root of", num, "is", square_root(num))

elif choice == '6':
   num = float(input("Enter a number: "))
   print("Exponential of", num, "is", exponential(num))

elif choice == '7':
   num = float(input("Enter a number: "))
   print("Logarithm of", num, "is", logarithm(num))

elif choice == '8':
   num = float(input("Enter a number in radians: "))
   print("Sine of", num, "is", sine(num))

elif choice == '9':
   num = float(input("Enter a number in radians: "))
   print("Cosine of", num, "is", cosine(num))

elif choice == '10':
   num = float(input("Enter a number in radians: "))
   print("Tangent of", num, "is", tangent(num))

else:
   print("Invalid input")