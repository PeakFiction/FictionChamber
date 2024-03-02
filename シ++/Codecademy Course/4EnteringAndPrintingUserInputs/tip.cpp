#include <iostream>

int main() 
{
    //Initialises the variable
    int tip = 0;
    
    //Prints out "Enter tip amount: "
    std::cout << "Enter tip amount: ";

    //Takes the user input and put it as tip variable
    std::cin >> tip;

    //Prints out "You paid [tip] dollars"
    std::cout << "You paid " << tip << " dollars.\n";
    
    
    
    
}