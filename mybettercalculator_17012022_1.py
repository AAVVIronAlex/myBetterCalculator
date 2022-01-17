import math

print ("Hello, Welcome to my Calculator")

question_1 = input ("Input either of these (sum, difference, square equation, multiply, division(more coming soon)): ")

if (question_1 == "sum"):
    a = int (input ("Input a:"))
    b = int (input ("Input b:"))
    print (a + b)

elif (question_1 == "difference"):
    a = int (input ("Input a:"))
    b = int (input ("Input b:"))
    print (a - b)

elif (question_1 == "multiply"):
    a = int (input ("Input a:"))
    b = int (input ("Input b:"))
    print (a * b)

elif (question_1 == "division"):
    a = int (input ("Input a:"))
    b = int (input ("Input b:"))
    print (a / b)

elif (question_1 == "square_equasion"):
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
