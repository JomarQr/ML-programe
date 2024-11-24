#include <iostream> 
using namespace std; 

int main() {
    // Massivs ar 10 elementiem
    int arr[10] = {5, 8, 3, 12, 1, 9, 4, 7, 6, 2};

    // Pieņemam, ka mazākais skaitlis sākotnēji ir masīva pirmais elements
    int min = arr[0];

    // Atradam mazako elementu
    for (int i = 1; i < 10; ++i) { // Sākam no 1, jo pirmais elements jau ir iekļauts
        if (arr[i] < min) { // Ja pašreizejais elements ir < par min
            min = arr[i]; // Atjaunam min vertību
        }
    }

    
    cout << "Mazākais skaitlis masīvā ir: " << min << endl;

    return 0; 
}
