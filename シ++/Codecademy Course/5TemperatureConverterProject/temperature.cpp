#include <iostream>

int main()
{   
    double tempf; //Declare Variable for Fahrenheit Temperature
    double tempc; //Declare Variable for Celsius Temperature

    std::cout << "What is the temperature in Fahrenheit? "; //Prints, asks user
    std::cin >> tempf; //Gets input from user, puts it as tempf
    
    tempc = (tempf - 32)/1.8; //Formula to convert

    std::cout << "The temperature is " << tempc << " degrees Celsius.\n";
		//Prints out result.


}