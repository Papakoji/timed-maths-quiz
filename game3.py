import random
import time 

max_operand =  15 
min_operand = 3 
operators = ['-', '+', '*']

user_input = input("Press Enter to continue . . . .")
print("Your time starts now")

start_time = time.time()
for i in range(10) :
    op1 =  random.randint(min_operand,max_operand)
    op2 =  random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    print(f"Problem #{i+1}: {op1} {operator} {op2}")
    if operator == '-':
        ans = op1 - op2 
    elif operator == '+': 
        ans = op1 + op2
    else : 
        ans = op1 * op2 
    while True: 
        user_ans = int(input("Enter the answer "))
        if user_ans == ans :
            print("Correct ans!") 
            break
        else: 
            print("Oops, wrong answer! Try again")

end_time = time.time()

print(f"Your total time taken is {end_time-start_time}")
    



