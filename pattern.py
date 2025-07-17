for i in range(1,5):
    print("*" * i)
    # a = "8" * i
for i in range(5,0,-1):
    print('*'*i)

front = 4
middle = 1

for i in range(0,5):
    print(' ' * front + '* ' * middle)
    front -= 1
    middle += 1


front = 0
# back=0
for j in range(7,0,-2):
    print(' '*front + '*' * j + ' '*front)
    front+=1
