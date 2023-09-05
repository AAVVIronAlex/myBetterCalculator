import math

def sin_function(a):
    radian_a = (3.141592653589793 / 180) * a

    for turn in range(1, 6):
        turn_multiplier = turn * 2 + 1
        radian_a = radian_a + math.pow(radian_a, turn_multiplier) / math.factorial(turn_multiplier) * math.pow(-1, turn)

    answer = round(radian_a, 3)

    return answer

print ("Hello, welcome to my Calculator")

question_1 = input ("Input either of these sum, difference, squareeq, multiply, division, root, power, percentage, squareofthesum, squareofthedifference, differenceofsquares, sin and there are more coming soon: ")

if (question_1 == "sum"):
    a = int (input ("Input a, for the a + b formula: "))
    b = int (input ("Input b, for the a + b formula: "))
    print (a, "+", b, "=", a + b)

elif (question_1 == "difference"):
    a = int (input ("Input a, for the a - b formula: "))
    b = int (input ("Input b, for the a - b formula: "))
    print ("a + b =", a, "-", b, "=", a - b)

elif (question_1 == "multiply"):
    a = int (input ("Input a, for the a * b formula: "))
    b = int (input ("Input b, for the a * b formula: "))
    print ("a - b =", a, "*", b, "=", a * b)

elif (question_1 == "division"):
    a = int (input ("Input a, for the a / b formula: "))
    b = int (input ("Input b, for the a / b formula: "))
    print ("a / b =", a, "/", b, "=", a / b)

elif (question_1 == "power"):
    a = int (input ("Input a, for the a ^ b formula: "))
    b = int (input ("Input b (power), for the a ^ b formula: "))
    print ("a ^ b =", a, "^", b, "=", math.pow (a, b))

elif (question_1 == "root"):
    a = int (input ("Input a, for the a ^ 1 / b formula: "))
    b = int (input ("Input b, for the a ^ 1 / b formula: "))
    print("a ^ 1 / b =", a, "^ 1 /", b, "=", math.pow(a, 1 / b))

elif (question_1 == "factorial"):
    a = int (input ("Input a(for the a! or a factorial formula): "))
    factorialalex = 1
    if (a == 0):
        print("0! = 1")
    else:
        for i in range(1, a + 1) :
            factorialalex = factorialalex * i
        print(a, "! = ", factorialalex)
    
elif (question_1 == "percentage"):
    a = int (input ("Input a(for the a %% b formula): "))
    b = int (input ("Input b(for the a %% b formula): "))
    percentage = a * b / 100
    print("a %% b =", "%s%%"% percentage)

elif (question_1 == "squareofthesum"):
    a = int (input ("Input a(for the (a + b)^2 formula): "))
    b = int (input ("Input b(for the (a + b)^2 formula): "))
    print("(a + b)^2 = a^2 + 2 * a * b + b^2 =", a * a + 2 * a * b + b * b)

elif (question_1 == "squareofthedifference"):
    a = int (input ("Input a(for the (a - b)^2 formula): "))
    b = int (input ("Input b(for the (a - b)^2 formula): "))
    print("(a - b)^2 = a^2 - 2 * a * b + b^2 =", a * a - 2 * a * b + b * b)

elif (question_1 == "differenceofsquares"):
    a = int (input ("Input a(for the a^2 - b^2 formula): "))
    b = int (input ("Input b(for the a^2 - b^2 formula): "))
    print("a^2 - b^2 = (a - b) * (a + b) =", (a - b) * (a + b))

elif (question_1 == "sin"):
    a = int (input ("Input the angle in degrees for the sin(angle) formula: "))
    print("Your answer is:", sin_function(a))

elif (question_1 == "cos"):
    a = int (input ("Input the angle in degrees for the cos(angle) formula: "))
    radian_a = (3.141592653589793 / 180) * a
    print("cos(", a, ") = ", 
    round(1 - math.pow(radian_a, 2) / math.factorial(2) + 
    math.pow(radian_a, 4) / math.factorial(4) - 
    math.pow(radian_a, 6) / math.factorial(6) + 
    math.pow(radian_a, 8) / math.factorial(8) - 
    math.pow(radian_a, 10) / math.factorial(10) + 
    math.pow(radian_a, 12) / math.factorial(12) - 
    math.pow(radian_a, 14) / math.factorial(14) + 
    math.pow(radian_a, 16) / math.factorial(16) - 
    math.pow(radian_a, 18) / math.factorial(18), 3))

elif (question_1 == "tan"):
    a = int (input ("Input the angle in degrees for the tan(angle) formula(0, 30, 45, 60, 90, 120, 135, 150, 180): "))
    if (a == 0):
        print("tan(0) = 0")
    elif (a == 30):
        print("tan(30) = 3 / sqrt(3)")
    elif (a == 45):
        print("tan(45) = 1")
    elif (a == 60):
        print("tan(60) = sqrt(3)")
    elif (a == 90):
        print("tan(90) = Not Defined")
    elif (a == 120):
        print("tan(120) = - sqrt(3)")
    elif (a == 135):
        print("tan(135) = - 1")
    elif (a == 150):
        print("tan(135) = - sqrt(3) / 3")
    elif (a == 180):
        print("tan(180) == 0")

elif (question_1 == "cot"):
    a = int (input ("Input the angle in degrees for the cot(angle) formula(0, 30, 45, 60, 90, 120, 135, 150, 180): "))
    if (a == 0):
        print("cot(0) = Not Defined")
    elif (a == 30):
        print("cot(30) = sqrt(3)")
    elif (a == 45):
        print("cot(45) = 1")
    elif (a == 60):
        print("cot(60) = sqrt(3) / 3")
    elif (a == 90):
        print("cot(90) = 0")
    elif (a == 120):
        print("cot(120) = - sqrt(3) / 3")
    elif (a == 135):
        print("cot(135) = - 1")
    elif (a == 150):
        print("cot(135) = - sqrt(3)")
    elif (a == 180):
        print("cot(180) == Not Defined")

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
        print("X can't be any number from the Real Numbers.")
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

elif (question_1 == "help"):
    print("Welcome to the help menu of this program.\n\nHere are some of the options you should consider using:\nsum - Calculating the sum of two numbers.\ndifference - Calculating the difference of the two numbers.\nmultiply - Calculating the product of the two numbers.\ndivision - Calculating the quotient of the two inputed numbers.")

else:
    print ("Try again.")