import sys 

# Helper function to create border. Border are helpfull in visualization of entire console output.
def seprator():
    return (58 * '=')

# prints a borderline
print(seprator())

print("__________________________Calculator______________________\n")



def get_float_input(prompt):
    num1 = input()
    try:
        num1 = float(num1)
    except ValueError:
        print("Invalid input!")


num1 = get_float_input('Enter number: ')
operator = input("Enter the opeartion you want to perfrom?: ")
num2 = input("Enter second number: ")

# Error handling
while True:
    if operator not in ['+','-','/','*']:
        operator = input("Enter valid opeartor: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        break
    except:
        print('Enter valid numbers ⚠')
        continue





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
print(seprator())


