# 1. Program to enter two numbers and print their sum and difference
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum_result = a + b
diff_result = a - b

print("Sum:", sum_result)
print("Difference:", diff_result)

# 2. Program to input length and breadth of a rectangle and calculate area and perimeter
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

# 3. Program to greet the user by name
name = input("Enter your name: ")
print("Hello", name + ", have a nice day!")

# 4. Program to compute the algebraic expression: x³ + 3x²y
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

# Compute the expression
result = x**3 + 3 * x**2 * y

print("Result of the expression x³ + 3x²y is:", result)
