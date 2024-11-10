#include <iostream>

int main() {
    int number;
    std::cout << "Enter a number (n): ";
    std::cin >> number;

    int sum = 0;
    // cikls lidz tam number kuru izvelējas cilvēks, sum no 1 līdz n
    for (int i = 1; i <= number; i++) {
        sum += i;
    }

    std::cout << "The sum from 1 to " << number << " is: " << sum << std::endl;
    return 0;
}