#include <iostream>
#include <cmath>

//Write a C++ program that solves the quadratic equation for the x's

int main() 
{
    double a;
    double b;
    double c;
    double root1;
    double root2;

    std::cout << "Enter a: ";
    std::cin >> a;

    std::cout << "Enter b: ";
    std::cin >> b;

    std::cout << "Enter c: ";
    std::cin >> c;

    root1 = (-b + std::sqrt(b*b - 4*a*c)) / (2*a);
    root2 = (-b - std::sqrt(b*b - 4*a*c)) / (2*a);

    //std::sqrt() is a built-in C++ function you gain access to 
    //by including the <cmath> library at the top of the file. 
    //For example, std::sqrt(9) would be 3.

    std::cout << "Root 1 is " << root1 << "\n";
    std::cout << "Root 2 is " << root2 << "\n";

    
    
}