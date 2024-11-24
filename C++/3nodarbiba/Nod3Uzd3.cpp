#include <iostream>  
#include <cstring>   // Iekļaujam bibliotēku virkņu apstrādes funkcijām, piemēram, strlen()
using namespace std;

int main() {
    const int MAX_LENGTH = 10000; // Maksimālais simbolu skaits, ko var ievadīt lietotājs
    char input[MAX_LENGTH];     // Masīvs, kurā tiks saglabāta lietotāja ievadītā virkne

    
    cout << "Ievadiet simbolu virkni: ";
    cin.getline(input, MAX_LENGTH); 

    // Aprēķinām virknes garumu
    int length = strlen(input);

    
    cout << "Simboli un to pozīcijas:" << endl;
    for (int i = 0; i < length; ++i) { // Iterējam cauri virknei pa vienam simbolam
        cout << "Simbols: " << input[i] << ", Pozīcija: " << i << endl;
        
    }

    return 0; 
}

