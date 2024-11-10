#include <iostream>
#include <iomanip>

int main() {
    int multiplier;
    int range;
    
    std::cout << "Enter the multiplier: ";
    std::cin >> multiplier;
    std::cout << "Enter the range: ";
    std::cin >> range;
    
    std::cout << "Multiplication table for " << multiplier << " up to range " << range << ":\n";
    
    // cikls, lai izveidotu reizināšanas tabulu līdz norādītajam intervālam
    for (int i = 1; i <= range; i++) {
        std::cout << std::setw(2) << multiplier   // Platums 2, lai reizinātājs būtu vienādi izlīdzināts
                  << " * " 
                  << std::setw(2) << i            // Platums 2, lai reizināmais skaitlis būtu vienādi izlīdzināts
                  << " = " 
                  << std::setw(3) << multiplier * i  // Platums 3, lai rezultāts būtu vienādi izlīdzināts
                  << std::endl;  
    }

    return 0;  
}