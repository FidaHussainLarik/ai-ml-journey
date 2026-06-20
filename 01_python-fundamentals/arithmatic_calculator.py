print("==============================================================")
print("__________________________Calculator__________________________")

num1= int(input("Enter first number: "))
operator = input("Enter the opeartion you want to perfrom?: ")
num2 = int(input("Enter second number: "))


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
        

print("==============================================================")


