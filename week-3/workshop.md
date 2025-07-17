# CS4051 Information Systems  
## Lab Work – Week 3  
### Python List & Loop Practice

---

###  1. Sum of Numbers from 1 to N
```python
# Ask user to input a number N
n = int(input("Enter a number N: "))

# Initialize sum
total = 0

# Add numbers from 1 to N
for i in range(1, n + 1):
    total += i

print("Sum from 1 to", n, "is:", total)
```

---

###  2. Sum of Even and Odd Numbers in a List
```python
# Ask how many numbers to input
n = int(input("How many numbers will you enter? "))

# Create an empty list
numbers = []

# Collect numbers from the user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize sums
even_sum = 0
odd_sum = 0

# Loop through list to calculate sums
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("List entered:", numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
```

---

###  3. Find Maximum and Minimum from a List
```python
# Ask how many numbers to input
n = int(input("Enter how many numbers: "))

# Create an empty list
numbers = []

# Collect input from user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Assume first element as max and min
max_num = numbers[0]
min_num = numbers[0]

# Compare each element
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Numbers entered:", numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
```

---

###  4. Generate N Fibonacci Numbers (Using List)
```python
# Input how many Fibonacci numbers to generate
n = int(input("Enter number of Fibonacci terms: "))

# Initialize list
fibonacci = []

# Generate the sequence
for i in range(n):
    if i == 0 or i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("Fibonacci sequence:", fibonacci)
```

---

###  5. Create List with Only Unique Elements
```python
# Existing list with duplicates
original = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]

# Create a new list for unique elements
unique = []

# Add only if not already in unique
for item in original:
    if item not in unique:
        unique.append(item)

print("Original list:", original)
print("Unique elements:", unique)
```

---

###  6. Reverse a List
```python
# Existing list
original = [1, 2, 3, 4, 5, 6]

# Reverse using slicing
reversed_list = original[::-1]

print("Original list:", original)
print("Reversed list:", reversed_list)
```
