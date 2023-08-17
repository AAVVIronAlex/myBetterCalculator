#include <iostream>
#include <cmath>
#include <cstring>

void sum(long double a, long double b)
{
	std::cout << "a + b = " << a + b << std::endl;
}

void difference(long double a, long double b)
{
	std::cout << "a - b = " << a - b << std::endl;
}

void multiplication(long double a, long double b)
{
	std::cout << "a * b = " << a * b << std::endl;
}

void division(long double a, long double b)
{
	std::cout << "a / b = " << a / b << std::endl;
}

void power(long double a, long double b)
{
	std::cout << "a ^ b = " << pow(a, b) << std::endl;
}

void root(long double a, long double b)
{
	std::cout << "a ^ 1 / b = " << pow(a, 1 / b) << std::endl;
}

void factorial(long double a)
{
	long double factorialalex = 1;
	if (a == 0)
	{
		std::cout << "0! = 1";
	}
	else
	{
		for (long double i = 1; i <= a; i++)
		{
			factorialalex = factorialalex * i;
		}
		std::cout << a << "! = " << factorialalex << std::endl;
 	}
}

void percentage(long double a, long double b)
{
	long double percentage = a * b / 100;
	std::cout << "a %% b = " << percentage << "%" << std::endl;
}

void square_of_the_sum(long double a, long double b)
{
	std::cout << "(a + b)^2 = a^2 + 2 * a * b + b^2 = " << a * a + 2 * a * b + b * b << std::endl;
}

void square_of_the_difference(long double a, long double b)
{
	std::cout << "(a - b)^2 = a^2 - 2 * a * b + b^2 = " << a * a - 2 * a * b + b * b << std::endl;
}

void difference_of_squares(long double a, long double b)
{
	std::cout << "a^2 - b^2 = (a - b) * (a + b) = " << (a - b) * (a + b) << std::endl;
}

void square_equation(long double a, long double b, long double c)
{
	int b2;
	int ac;
	double x1;
	double x2;

	b2 = b * b;
	ac = 4 * a * c;

	if (b2 - ac < 0)
	{
		std::cout << "X can't be any number from the Real Numbers." << std::endl;
	}

	else if (b2 - ac > 0)
	{
		x1 = (-b - sqrt((b2 - ac))) / (2 * a);
		x2 = (-b + sqrt((b2 - ac))) / (2 * a);
		std::cout << "D = b * b - 4ac = " << b2 - ac << "sqrt (" << b2 - ac << ") =" << sqrt(b2 - ac) << std::endl;
		std::cout << "x1 = (-b - sqrt(D)) / 2a = " << x1 << std::endl;
		std::cout << "x2 = (- b + sqrt (D)) / 2a =" << x2 << std::endl;
	}

	else
	{
		x1 = (-b - sqrt((b2 - ac))) / (2 * a);
		std::cout << "D = b * b - 4ac = " << b2 - ac << "sqrt (" << b2 - ac << ") =" << sqrt(b2 - ac) << std::endl;
		std::cout << "x = (-b - sqrt(D)) / 2a = " << x1 << std::endl;
	}
}

int main()
{
	long double a, b, c;

	std::cout << "Hello, Welcome to my Calculator" << std::endl;
	std::cout << "Input either of these sum, difference, squareeq, multiply, division, root, power, percentage, squareofthesum, squareofthedifference, differenceofsquares (more coming soon): ";
	std::string question1;
	std::cin >> question1;

	if (question1 == "sum")
	{
		std::cout << "Input a, for the a + b formula: ";
		std::cin >> a;
		std::cout << "Input b, for the a + b formula: ";
		std::cin >> b;
		sum(a, b);
	}

	else if (question1 == "difference")
	{
		std::cout << "Input a, for the a - b formula: ";
		std::cin >> a;
		std::cout << "Input b, for the a - b formula: ";
		std::cin >> b;
		difference(a, b);
	}

	else if (question1 == "multiply")
	{
		std::cout << "Input a, for the a * b formula: ";
		std::cin >> a;
		std::cout << "Input b, for the a * b formula: ";
		std::cin >> b;
		multiplication(a, b);
	}

	else if (question1 == "division")
	{
		std::cout << "Input a, for the a / b formula: ";
		std::cin >> a;
		std::cout << "Input b, for the a / b formula: ";
		std::cin >> b;
		division(a, b);
	}

	else if (question1 == "power")
	{
		std::cout << "Input a, for the a ^ b formula: ";
		std::cin >> a;
		std::cout << "Input b (power), for the a ^ b formula: ";
		std::cin >> b;
		power(a, b);
	}

	else if (question1 == "root")
	{
		std::cout << "Input a, for the a ^ 1 / b formula: ";
		std::cin >> a;
		std::cout << "Input a, for the a ^ 1 / b formula: ";
		std::cin >> b;
		root(a, b);
	}

	else if (question1 == "squareeq")
	{
		std::cout << "Input a, for the ax2 + bx + c formula: ";
		std::cin >> a;
		std::cout << "Input b, for the ax2 + bx + c formula: ";
		std::cin >> b;
		std::cout << "Input c, for the ax2 + bx + c formula: ";
		std::cin >> c;
		square_equation(a, b, c);
	}

	else if (question1 == "factorial")
	{
		std::cout << "Input a(for the a! or a factorial formula): ";
		std::cin >> a;
		factorial(a);
	}

	else if (question1 == "percentage")
	{
		std::cout << "Input a(for the a %% b formula): ";
		std::cin >> a;
		std::cout << "Input b(for the a %% b formula): ";
		std::cin >> b;
		percentage(a, b);
	}

	else if (question1 == "squareofthesum")
	{
		std::cout << "Input a(for the (a + b)^2 formula): ";
		std::cin >> a;
		std::cout << "Input b(for the (a + b)^2 formula): ";
		std::cin >> b;
		square_of_the_sum(a, b);
	}

	else if (question1 == "squareofthedifference")
	{
		std::cout << "Input a(for the (a - b)^2 formula): ";
		std::cin >> a;
		std::cout << "Input b(for the (a - b)^2 formula): ";
		std::cin >> b;
		square_of_the_difference(a, b);
	}

	else if (question1 == "differenceofsquares")
	{
		std::cout << "Input a(for the (a - b)^2 formula): ";
		std::cin >> a; 
		std::cout << "Input b(for the (a - b)^2 formula): ";
		std::cin >> b;
		difference_of_squares(a, b);
	}

	else
	{
		std::cout << "Try again." << std::endl;
	}
}