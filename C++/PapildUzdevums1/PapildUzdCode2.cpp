#include <iostream> 

int main() {
    int number;  
    std::cout << "Enter a number (n): ";  
    std::cin >> number;  

    int sum = 0;  

    // Cikls no 1 līdz lietotaja number lai pārbaudītu katru skaitli šaja intervālā
    for (int i = 1; i <= number; i++) {
        // Pārbaudam, vai skaitlis i dalās ar 3 vai 5
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;  
        }
    }

    
    std::cout << "The sum of numbers divisible by 3 or 5 from 1 to " << number << " is: " << sum << std::endl;

    return 0;  
}