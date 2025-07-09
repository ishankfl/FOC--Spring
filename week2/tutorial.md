# Python Practice – Conditional & Loop Programs

---

### 1. Program to Check if a Number is Even or Odd
```python
# Ask user to enter a number
num = int(input("Enter a number: "))

# Check if the number is even or odd using modulus operator
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

---

### 2. Program to Find the Greatest of Three Numbers
```python
# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare using if-else
if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)
```

---

### 3. Program to Find GCD Using Euclidean Algorithm (While Loop)
```python
# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Apply Euclidean algorithm
while b != 0:
    a, b = b, a % b

print("The GCD is:", a)
```

---

### 4. Program to Calculate Factorial Using While Loop
```python
# Input a non-negative integer
n = int(input("Enter a non-negative integer: "))

# Initialize factorial result
factorial = 1
i = 1

# Use while loop to calculate factorial
while i <= n:
    factorial *= i
    i += 1

print("Factorial of", n, "is:", factorial)
```

---

### 5. Program to Check if a Number is Prime (While Loop)
```python
# Input a number
num = int(input("Enter a number: "))

# Check for prime
if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    i = 2
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
