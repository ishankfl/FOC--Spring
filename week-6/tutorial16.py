# def add(a,b):
#     sum = a+b
#     return sum
# def difference(a,b):
#     diff = a - b 
#     return diff
# def product(a,b):
#     # product_ = a * b
#     # return product_
#     return a * b

# a = int(input("Enter the first num: "))
# b = int(input("Enter the second num: "))

# addition = add(a,b)
# diff = difference(a,b)
# multiplication = product(a,b)

# print("Sum",addition)
# print("Difference",diff)
# print("Multiplication",multiplication)


def vowels_count(user_input):
    vowels_letter='aeiouAEIOU'
    count = 0
    for each in user_input:
        
        if each in vowels_letter:
            count+=1
            print(each, "is vowels letter")
    print('count',count)
user_input = input("Enter any text here: ")
vowels_count(user_input)