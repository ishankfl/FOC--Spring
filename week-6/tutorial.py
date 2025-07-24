# def add(a,b):
#     # a = 10 
#     # b = 20
#     sum = a+b #sum = 30
#     return sum  # return 30

# def difference(a,b):
#     diff = a - b
#     return diff

# def product (a,b):
#     product = a * b
#     return product

# def divide(a,b):
#     divide = a / b
#     return divide

# def calculation(a,b,operator): 
#     if operator == '+':
#         sum = add(a,b) # add(10,20) = 30 = sum
        
#         print(sum) # 30
        
#     elif operator == '-':
#         diff = difference(a,b)
#         print(diff)

# while True:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     operator = input("Enter the operator: ")
#     calculation(a,b,operator)




def count_letter(user_input):
    vowels_letters = "aeiouAEIOU"
    
    vowels_count = 0
    other_count = 0
    
    for each in user_input:
        
        if each in vowels_letters:
            
            vowels_count+=1
    
    return vowels_count, other_count
            
user_input = input("Enter any word: ")
v_count, other_count = count_letter(user_input)
print(v_count, other_count)


