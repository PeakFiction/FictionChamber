#include <iostream>
int main()
{
    double dogYear;
    std::cout << "What is the age of the dog? ";
    std::cin >> dogYear;

    double extraLife = dogYear - 2;
    double extraYears = extraLife * 4;
    double humanYears;
    {
        if (dogYear == 1)
        {
            humanYears = 10.5;
        }

        else if (dogYear == 2)
        {
            humanYears = 21;
        }

        else
        {
            humanYears = 21 + extraYears;
        }

    }

    std::cout << "The dog's age in human years is " << humanYears << " years old";
}
