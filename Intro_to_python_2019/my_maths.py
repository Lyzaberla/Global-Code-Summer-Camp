#simple calculator to sum two integers and accept one string
print('Welcome to the simple calculator')

print('select any of the operations below:')
#print('Add','Subtract','Multiply','Divide')
def Add(num1, num2):
    return num1 + num2
def Subtract(num1, num2):
    return num1 - num2
def Multiply(num1, num2):
    return num1 * num2
def Divide(num1, num2):
    return num1 / num2
choice =input('enter choice(Add/Subtract/Multiply/Divide)')

num1 =int(input('enter a number...'))
num2 =int(input('enter another number...'))
if choice=='Add':
    print('Ans: ', Add(num1, num2))
elif choice=='Subtract':
    print('Ans: ', Subtract(num1, num2))
elif choice=='Multiply':
    print('Ans: ', Multiply(num1, num2))
elif choice=='Divide':
     print('Ans: ', Divide(num1, num2))

else: print('WRONG INPUT!')






