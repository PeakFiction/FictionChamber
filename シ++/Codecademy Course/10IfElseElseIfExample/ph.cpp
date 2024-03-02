#include <iostream>
//Program that asks user for PH level
//if PH level is above 7, print Basic
//if PH level is below 7, print Acidic
//If neither (exactly 7), print Neutral

int main()
{
    int ph;

    std::cout << "What is the ph level? ";
    //Prints, asks the user what the ph level is
    std::cin >> ph;
    //Takes input from user, puts it in ph
    
    {
        if (ph > 7) //if ph is over 7
        {
            std::cout << "Basic\n"; //print Basic
        }

        else if (ph < 7) //if ph is below 7
        {
            std::cout << "Acidic\n"; //print Acidic
        }

        else //otherwise, (ph level is 7)
        {
            std::cout << "Neutral"; //print Neutral
        }
    }

}