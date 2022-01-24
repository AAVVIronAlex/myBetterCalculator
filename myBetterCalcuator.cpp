#include <iostream>
#include <cmath>
#include <cstring>

long sum(long long a, long long b)
{
	std::cout << "a + b = " << a + b;
	return 0;
}

long difference(long long a, long long b)
{
	std::cout << "a - b = " << a - b;
	return 0;
}

long multiplication(long long a, long long b)
{
	std::cout << "a * b = " << a * b;
	return 0;
}

long division(long long a, long long b)
{
	std::cout << "a / b = " << a / b;
	return 0;
}

long power(long long a, long long b)
{
	std::cout << "a ^ b = " << pow(a, b);
	return 0;
}

long root(long long a, long long b)
{
	std::cout << "a ^ 1 / b = " << pow(a, 1 / b);
	return 0;
}

long square_equation(double a, double b, double c)
{
	int b2;
	int ac;
	double x1;
	double x2;

	b2 = b * b;
	ac = 4 * a * c;

	if (b2 - ac < 0)
	{
		std::cout << "X can't be any number from the Real Numbers";
	}

	else if (b2 - ac > 0)
	{
		x1 = (-b - sqrt((b2 - ac))) / (2 * a);
		x2 = (-b + sqrt((b2 - ac))) / (2 * a);
		std::cout << "D = b * b - 4ac = " << b2 - ac << "sqrt (" << b2 - ac << ") =" << sqrt(b2 - ac);
		std::cout << "x1 = (-b - sqrt(D)) / 2a = " << x1;
		std::cout << "x2 = (- b + sqrt (D)) / 2a =" << x2;
	}

	else
	{
		x1 = (-b - sqrt((b2 - ac))) / (2 * a);
		std::cout << "D = b * b - 4ac = " << b2 - ac << "sqrt (" << b2 - ac << ") =" << sqrt(b2 - ac);
		std::cout << "x = (-b - sqrt(D)) / 2a = " << x1;
	}

	return 0;
}

long main()
{
	long a, b, c;

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
		std::cout << "Input a, for the a * b formula: ";
		std::cin >> b;
		multiplication(a, b);
	}

	else if (question1 == "divide")
	{
		std::cout << "Input a, for the a / b formula: ";
		std::cin >> a;
		std::cout << "Input a, for the a / b formula: ";
		std::cin >> b;
		division(a, b);
	}

	else if (question1 == "power")
	{
		std::cout << "Input a, for the a ^ b formula: ";
		std::cin >> a;
		std::cout << "Input a, for the a ^ b formula: ";
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
}