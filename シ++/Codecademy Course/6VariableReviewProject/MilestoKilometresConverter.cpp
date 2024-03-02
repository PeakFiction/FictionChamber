#include <iostream>

/*Create a program that asks for a distance in miles as input. The program will then output how much that distance is in kilometers.*/

int main()
{
    double miles;
    std::cout << "What is the distance in Miles? ";
    std::cin >> miles;

    double kilometres = miles * 1.6;

    std::cout << "The distance of " << miles << " miles, is " << kilometres << " km";

}