import sys 

# Helper function to create border. Border are helpfull in visualization of entire console output.
def seprator():
    print(58 * '=')

# prints a borderline
seprator()

print("__________________________Calculator______________________\n")



def get_float_input(prompt):
    while True:
        num = input()
        try:
            num1 = float(num)
            return num
        except ValueError:
            print("Invalid input!")
            continue

def get_opeartor(prompt):
    opeartor = input()
    try:
        if get_opeartor in ['+','-','/','*']:
            return opeartor
    except ValueError:
        print("Invalid input!")


num1 = get_float_input('Enter first number : ')
operator = get_opeartor('Enter the operation you want to perform: ')
num2 = get_float_input('Enter second number: ')




def power_fn(base,exponent):
    power = (base ** exponent)
    print(f"{base} to the power {exponent} is {power}")
    

def addition(para1,para2):
    sum_numbers = para1+para2
    print(f"Addition of {para1} and {para2} : ",(sum_numbers))

def subtraction(para1,para2):
    sub_numbers = (para1 - para2)
    print(f"Subtraction of {para1} and {para2} : ",(sub_numbers))

def multiplication(para1,para2):
    multi_numbers = (para1 * para2)
    print(f"Multiplication of {para1} and {para2} : ",(multi_numbers))

def division(para1,para2):
    divide_numbers = (para1 / para2)
    print(f"Division of {para1} and {para2} : ",(divide_numbers))


if operator == '+':
    addition(num1,num2)
elif operator == '-':
    subtraction(num1,num2)
elif operator == '*':
    multiplication(num1,num2)
elif operator == '/':
    division(num1,num2)
else:
    print("Please enter a valid operator!")
        
# prints a borderline
seprator()


