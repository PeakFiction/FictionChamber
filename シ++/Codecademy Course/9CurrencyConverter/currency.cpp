#include <iostream>
// You just returned from a trip to South America. The countries you visited 
//were Colombia, Brazil, and Peru. 
//You arrived back in your country with some foreign currencies from these three countries.
//Calculate how much USD you have from all these three currencies. 
int main() 
{
    int pesos;
    int reais;
    int soles;
    int dollars;

    std::cout << "Enter number of Colombian Pesos: ";
    std::cin >> pesos;
    std::cout << "\n";

    std::cout << "Enter number of Brazilian Reais: ";
    std::cin >> reais;
    std::cout << "\n";

    std::cout << "Enter number of Peruvian Soles: ";
    std::cin >> soles;
    std::cout << "\n";

    //1 Colombian Pesos = 0.00024 USD
    //1 Brazilian Reais = 0.20 USD
    //1 Peruvian Soles = 0.27 USD

    dollars = (pesos * 0.0024) + (reais * 0.20) + (soles * 0.27);

    std::cout << "US Dollars = $" << dollars;

}