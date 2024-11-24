#include <iostream> 
#include <set>      
#include <cstdlib>  // Bibliotēka nejaušu skaitļu ģenerēšanai
using namespace std;

int main() {
    const int rows = 5; //  rindu skaits
    const int cols = 5; // kolonnu skaits
    int a[rows][cols]; // Divdimensiju masīvs
    set<int> unique_values; 


    cout << "Divdimensiju masīvs:" << endl;
    for (int i = 0; i < rows; i++) { // Iterējam pa masīva rindām
        for (int j = 0; j < cols; j++) { // Iterējam pa masīva kolonnām
            a[i][j] = rand() % 100; // Ģenerējam nejaušu skaitli diapazonā 0-99
            unique_values.insert(a[i][j]); // Pievienojam šo skaitli 'set' konteinerī
            cout << a[i][j] << "\t"; 
        }
        cout << endl; 
    }

    
    cout << "Unikālās vērtības augošā secībā:" << endl;
    for (const int &val : unique_values) { // Iterējam caur visām 'set' vērtībām
        cout << val << " "; 
    }
    cout << endl;

    return 0; 
}

