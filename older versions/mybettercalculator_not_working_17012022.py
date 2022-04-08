#Does not work yet will be working in a week.
import math

a = 0
b = 0
c = 0

#work on this part
def sum ():
    a = input ("Input a:")
    b = input ("Input b:")
    sum = a + b
    return sum

def difference (a, b):
    difference = a - b

def multiply (a, b):
    multiply = a * b

def division (a, b):
    division = a / b

def square_equasion(a, b, c):
    print ('Input a, for the ax2 + bx + c formula: ')
    a = int (input ())
    print ('Input b, for the ax2 + bx + c formula: ')
    b = int (input ())
    print ('Input c, for the ax2 + bx + c formula: ')
    c = int (input ())
    b2 = b ** 2
    ac = 4 * a * c
    x1 = (b - math.sqrt (b2 + ac)) / 2 * a
    x2 = b + math.sqrt (b2 + ac) / 2 * a

    #print(a, 'x2' + ' + ', b, 'x' + ' + ', c, + ' = ' + '0')

    if (b2 - ac < 0):
        print ("X can be any number")
    elif (b2 - ac > 0):
        print ('D = b * b - 4ac =', b2 - ac, "sqrt (", b2 - ac, ") =", math.sqrt (b2 + ac))
        print ('x1 = (b - sqrt (D)) / 2a =', x1)
        print ('x2 = (b - sqrt (D)) / 2a =', x2)
    else:
        print ('D = b * b + 4ac =', b2 - ac, "sqrt (", b2 - ac, ") =", math.sqrt (b2 + ac))
        print ("x = (b - sqrt (0)) / 2a =", x1)


    print ("Hello, Welcome to my Calculator")

question_1 = input ("Input either of these (sum, difference, square equation, multiply, division(more coming soon)): ")
if (question_1 == "sum"):
    print (sum)
