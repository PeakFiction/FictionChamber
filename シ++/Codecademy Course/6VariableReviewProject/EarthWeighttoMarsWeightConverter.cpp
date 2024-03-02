#include <iostream>

/*Create a program that takes in the weight of an item and then calculates how much that item would weigh on Mars.*/

int main()
{
    double EarthWeight;
    std::cout << "What is the weight of the item on Earth? ";
    std::cin >> EarthWeight;

    double MarsWeight = (EarthWeight/9.807) * 3.71;
    
    std::cout << "The weight of " << EarthWeight << " kg on Earth is " << MarsWeight << " kg on Mars.";
}