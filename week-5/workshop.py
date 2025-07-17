# # A =[ 
# #   [2, 3, 4],
# #   [1, 5, 6],
# #   [5, 8, 5]
# # ]
# # # print("Total sum")
# # # sum = 0
# # # for i in range(len(A)):
# # #     for j in range(len(A[i])):
# # #         print(A[i][j])
# # #         sum += A[i][j]
# # # print(sum)

# # print("Sum of diagonal elements")
# # sum = 0
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         if i == j:
# #             # print(A[i][j])
# #             sum += A[i][j]
# # print(sum)

# # print("Sum of above diagonal elements")
# # sum = 0
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         if i < j:
# #             # print(A[i][j])
# #             sum += A[i][j]
# # print(sum)

# # print("Sum of below diagonal elements")
# # sum = 0
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         if i > j:
# #             # print(A[i][j])
# #             sum += A[i][j]
# # print(sum)
# A =[ 
#   [2, 3, 4],
#   [1, 5, 6],
#   [5, 8, 5]
# ]
# min = A[0][0]
# max = A[0][0]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         if min > A[i][j]:
#             min = A[i][j]
            
#         if max < A[i][j]:
#             max=A[i][j]
            
# print("min", min)
# print("max", max)
            
#         # print(A[i][j])

N = int(input("Enter the total no. of students: ")) #N=2
details = {}
for i in range(N): # 0,1
    name = input("Enter the name: ")
    marks = int(input("Enter the marks of "+name))
    details[name]=marks
names = list(details.keys())
marks = list(details.values())

print('Highes Marks',max(marks))
print('Lowest Marks',min(marks))
print('Avg Marks',sum(marks)/N)

# print('keys',details.keys())
# print('values',details.values())