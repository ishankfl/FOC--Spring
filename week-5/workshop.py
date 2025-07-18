# -----------------------------
# Question 2: Matrix with 1 (diagonal), 2 (above), 3 (below)
# -----------------------------
print("\nQuestion 2: Custom Matrix Generation")
A = []
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

for i in range(row):
    temp = []
    for j in range(col):
        if i == j:
            temp.append(1)
        elif i < j:
            temp.append(2)
        else:
            temp.append(3)
    A.append(temp)

print("Generated Matrix:")
for r in A:
    print(r)


# -----------------------------
# Question 3: Matrix Sum Calculations
# -----------------------------
print("\nQuestion 3: Matrix Sum Calculations")
A = [
    [2, 3, 4],
    [1, 5, 6],
    [5, 8, 5]
]

diag_sum = 0
above_diag = 0
below_diag = 0
elements = []

for i in range(len(A)):
    for j in range(len(A[i])):
        elements.append(A[i][j])
        if i == j:
            diag_sum += A[i][j]
        elif i < j:
            above_diag += A[i][j]
        elif i > j:
            below_diag += A[i][j]

print("Matrix:")
for r in A:
    print(r)

print("Diagonal Sum:", diag_sum)
print("Above Diagonal Sum:", above_diag)
print("Below Diagonal Sum:", below_diag)
print("Max Element:", max(elements))
print("Min Element:", min(elements))


# -----------------------------
# Question 4: Student Marks Dictionary
# -----------------------------
print("\nQuestion 4: Student Marks Dictionary")
N = int(input("Enter total number of students: "))
details = {}

for i in range(N):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    details[name] = marks

marks = list(details.values())
print("Details:", details)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks)/N)


# -----------------------------
# Question 5: Student Subject Averages
# -----------------------------
print("\nQuestion 5: Average Marks of Students")
students = [
    ["john", 88, 86, 76, 66, 76],
    ["sam", 77, 67, 87, 67, 56],
    ["anna", 67, 65, 67, 76, 65],
    ["ben", 87, 78, 67, 77, 57],
    ["jeff", 90, 80, 79, 88, 70]
]

print("Average marks of each student:")
for student in students:
    name = student[0]
    subjects = student[1:]
    avg = sum(subjects) / len(subjects)
    print(f"{name.title()}: {avg}")
