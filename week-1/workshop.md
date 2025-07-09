# Python Basics Practice

### 1. Try arithmetic operators in IDLE (interactive shell)
Open IDLE and try the following:
```python
2 + 3
10 - 5
4 * 5
20 / 4
7 // 2
8 % 3
2 ** 3
```

---

### 2. Hello World Program
```python
# This is a simple program that prints "Hello World"
print("Hello World")
```

---

### 3. Program to Greet the User
```python
# Ask the user to enter their name
name = input("Enter your name: ")

# Print a personalized greeting
print("Hello", name + ", have a nice day!")
```

---

### 4. Program to Enter Two Numbers and Print Sum and Difference
```python
# Ask user to input two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate sum and difference
sum_result = a + b
diff_result = a - b

# Display the results
print("Sum:", sum_result)
print("Difference:", diff_result)
```

---

### 5. Program to Compute Algebraic Expression: x³ + 3x²y
```python
# Ask the user to input values of x and y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

# Compute the expression: x³ + 3x²y
result = x**3 + 3 * x**2 * y

# Display the result
print("Result of the expression x³ + 3x²y is:", result)
```

---

### 6. Program to Calculate Area of a Circle
```python
# Import math module to use pi
import math

# Ask the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius**2

# Display the area
print("Area of the circle is:", area)
```

---

### 7. Program to Calculate Area and Perimeter of a Rectangle
```python
# Ask the user to enter length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Display the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
```

---

### 8. Program to Solve a Quadratic Equation
```python
# Import math module for square root function
import math

# Ask the user to input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Calculate the two roots
root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

# Display the results
print("The solutions are:", root1, "and", root2)
```

*Test with a=1, b=3, c=-4 → You should get 1.0 and -4.0*

---

### 9. Program to Swap Two Numbers
```python
# Ask the user to input two numbers
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Swap the values
a, b = b, a

# Display the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
```
