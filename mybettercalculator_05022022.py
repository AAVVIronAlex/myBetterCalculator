import math

print ("Hello, Welcome to my Calculator")

question_1 = input ("Input either of these (sum, difference, squareeq, multiply, division, root, power(more coming soon)): ")

if (question_1 == "sum"):
    a = int (input ("Input a: "))
    b = int (input ("Input b: "))
    print (a, "+", b, "=", a + b)

elif (question_1 == "difference"):
    a = int (input ("Input a: "))
    b = int (input ("Input b: "))
    print ("a + b =", a, "-", b, "=", a - b)

elif (question_1 == "multiply"):
    a = int (input ("Input a: "))
    b = int (input ("Input b: "))
    print ("a - b =", a, "*", b, "=", a * b)

elif (question_1 == "division"):
    a = int (input ("Input a: "))
    b = int (input ("Input b: "))
    print ("a / b =", a, "/", b, "=", a / b)

elif (question_1 == "power"):
    a = int (input ("Input a: "))
    b = int (input ("Input b(power): "))
    print ("a ^ b =", a, "^", b, "=", math.pow (a, b))

elif (question_1 == "root"):
    a = int (input ("Input a: "))
    b = int (input ("Input b(power): "))
    print("a ^ 1 / b =", a, "^ 1 /", b, "=", math.pow(a, 1 / b))

elif (question_1 == "factorial"):
    a = int (input ("Input a(for the a! or a factorial formula): "))
    factorialalex = 1
    if (a == 0):
        print("0! = 1")
    else:
        for i in range(1, a + 1):
            factorial = factorialalex * i 
        print(a, "! = ", factorialalex)

    #add the a^2 + b^2 formula family...

elif (question_1 == "squareeq"):
    print ('Input a, for the ax2 + bx + c formula: ')
    a = int (input ())
    print ('Input b, for the ax2 + bx + c formula: ')
    b = int (input ())
    print ('Input c, for the ax2 + bx + c formula: ')
    c = int (input ())
    b2 = b ** 2
    ac = 4 * a * c
    #x1 = (- b - math.sqrt ((b2 - ac))) / (2 * a)
    #x2 = (- b + math.sqrt ((b2 - ac))) / (2 * a)
    #print(a, 'x2' + ' + ', b, 'x' + ' + ', c, + ' = ' + '0')

    if (b2 - ac < 0):
        #x1 = (- b - ( - math.sqrt ((- b2 + ac)))) / (2 * a)
        #x2 = (- b + ( - math.sqrt ((- b2 + ac)))) / (2 * a)
        #print ('D = b * b - 4ac =', b2 - ac, "sqrt (", b2 - ac, ") =", - math.sqrt (- b2 + ac))
        #print ('x1 = (- b - sqrt (D)) / 2a =', x1, "+ i")
        #print ('x2 = (- b + sqrt (D)) / 2a =', x2, "+ i")
        print("X can't be any number from the Real Numbers")
        #make irreal number support

    elif (b2 - ac > 0):
        x1 = (- b - math.sqrt ((b2 - ac))) / (2 * a)
        x2 = (- b + math.sqrt ((b2 - ac))) / (2 * a)
        print ('D = b * b - 4ac =', b2 - ac, "sqrt (", b2 - ac, ") =", math.sqrt (b2 - ac))
        print ('x1 = (- b - sqrt (D)) / 2a =', x1)
        print ('x2 = (- b + sqrt (D)) / 2a =', x2)

    else:
        x1 = (- b - math.sqrt ((b2 - ac))) / (2 * a)
        print ('D = b * b + 4ac =', b2 - ac, "sqrt (", b2 - ac, ") =", math.sqrt (b2 - ac))
        print ("x = (- b - sqrt (0)) / 2a =", x1)

else:
    print ("Try again.")
