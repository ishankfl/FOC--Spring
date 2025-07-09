# CS4051 – Python Practice: Lists & Sequences

---

###  1. Program to Calculate Sum of Odd and Even Numbers from a List
```python
# Ask the user for how many numbers to enter
n = int(input("How many numbers do you want to enter? "))

# Create an empty list
numbers = []

# Take input and add to the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize sum variables
even_sum = 0
odd_sum = 0

# Loop through the list to calculate even and odd sums
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Display results
print("List of numbers:", numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
```

---

###  2. Program to Find Maximum and Minimum from a List
```python
# Ask the user for how many integers to enter
n = int(input("How many numbers do you want to enter? "))

# Create an empty list
numbers = []

# Take input and add to the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Assume first element as max and min
max_num = numbers[0]
min_num = numbers[0]

# Iterate through the list to find max and min
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Display the results
print("Full list of numbers:", numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
```

---

### 🏠 Homework – Fibonacci Sequence Using List
```python
# Ask the user for how many Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci terms: "))

# Initialize Fibonacci list
fibonacci = []

# Generate the sequence
for i in range(n):
    if i == 0 or i == 1:
        fibonacci.append(1)
    else:
        next_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_num)

# Display the Fibonacci sequence
print("Fibonacci sequence:")
print(fibonacci)
```
