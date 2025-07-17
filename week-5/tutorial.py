
# items=[
#     [2,3],
#     [4,5]
#     ]
# for i in range(len(items)):
#     # print(items[i]) # items[i]=[2,3]
#     for j in range(len(items[i])): # 0, 1
#         if items[i][j] % 2 != 0:
            
#             print(items[i][j])
A = [
   	[1, 2, 3],
    [4, 5, 6]
]
print("Odd numbers")
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] % 2 != 0:
            print(A[i][j],end=' ')
            
print("Even numbers")
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] % 2 == 0:
            print(A[i][j])
print("Sum of all numbers: ")
sum = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        sum += A[i][j]
        # print(A[i][j])
print("Sum of all elements",sum)

print("Elements of first row: ")
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == 0:
            print(A[i][j])
