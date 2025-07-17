# CS4051 Fundamentals of Computing  
## Lab Work – Week 2

---

### 1. Program to Find the Greater of Two Numbers
```python
# Input two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Compare and print the greater number
if a > b:
    print("The greater number is:", a)
elif b > a:
    print("The greater number is:", b)
else:
    print("Both numbers are equal.")
```

---

### 2. Program to Check Even or Odd
```python
# Input a number
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

---

### 3. Program to Check if It's a Weekday or Weekend
```python
# Input day of the week
day = input("Enter the current day of the week: ").lower()

# Check and respond
if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print("Happy weekday! Work hard!")
elif day in ['saturday', 'sunday']:
    print("Enjoy your weekend!")
else:
    print("Invalid day entered.")
```

---

### 4. Program to Calculate Average and Grade
```python
# Input student name
name = input("Enter student name: ")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / 5

# Assign grade
if 70 <= average <= 100:
    grade = 'A'
elif 60 <= average <= 69:
    grade = 'B'
elif 50 <= average <= 59:
    grade = 'C'
elif 43 <= average <= 49:
    grade = 'D'
elif 40 <= average <= 42:
    grade = 'E'
else:
    grade = 'F'

# Output
print("\nStudent Name:", name)
print("Marks:", marks)
print("Average Marks:", average)
print("Overall Grade:", grade)
```

---

### 5. Program to Check Prime Number (Using While Loop)
```python
# Input a number
num = int(input("Enter a number: "))

# Check if number is prime
if num <= 1:
    print("Not a prime number.")
else:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
```

---

### 6. Program to Find GCD Using Euclidean Algorithm (While Loop)
```python
# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm
while b != 0:
    a, b = b, a % b

print("The GCD is:", a)
```

---

### 7. Program to Calculate Factorial (Using While Loop)
```python
# Input a non-negative integer
n = int(input("Enter a non-negative integer: "))

# Calculate factorial using while loop
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is:", fact)
```

---

### 8. Program to Generate First N Fibonacci Numbers (Using For Loop)
```python
# Input number of terms
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize first two terms
a, b = 1, 1

# Print sequence
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
```
