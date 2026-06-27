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
    return power


def addition(para1,para2):
    sum_numbers = para1+para2
    return sum_numbers

def subtraction(para1,para2):
    sub_numbers = (para1 - para2)
    return sub_numbers

def multiplication(para1,para2):
    multi_numbers = (para1 * para2)
    return multi_numbers

def division(para1,para2):
    division_numbers = (para1 / para2)
    return division_numbers


if operator == '+':
    sum = addition(num1,num2)
    print(f"Addition of {num1} and {num2} is: {sum}")
elif operator == '-':
    sub = subtraction(num1,num2)
    print(f"Subtraction of {num1} and {num2} is: {sub}")
elif operator == '*':
    product = multiplication(num1,num2)
    print(f"Product of {num1} and {num2} is: {product}")
elif operator == '/':
    division = division(num1,num2)
    print(f"Division of {num1} and {num2} is: {division}")

        
# prints a borderline
seprator()


