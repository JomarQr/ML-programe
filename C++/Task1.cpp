#include <iostream>

int main() {
    char text[100] = "Programmas ir jaraksta cilvekiem, kas tas lasis!";
    int choice;

    while (true) {
        // Attēlo izvēlni lietotājam
        std::cout << "\nIzvēlne:\n"
                  << "1: Ievadīt jaunu teksta virkni\n"
                  << "2: Izvada teksta virkni uz ekrāna\n"
                  << "3: Izvada summu no 1..n (kur n = teksta virknes garums)\n"
                  << "4: Izvada virkni no otrā gala (reversā)\n"
                  << "5: Saskaita un attēlo cik katrs simbols atkārtojas teksta virknē\n"
                  << "6: Beigt darbību\n";

        std::cout << "Ievadiet izvēles numuru (1-6): ";
        std::cin >> choice;

        // Pārbauda, vai ievade ir skaitlis
        if (std::cin.fail()) {
            std::cin.clear();  // Atiestatām ievades kļūdas stāvokli
            std::cin.ignore(10000, '\n');  // Ignorējam atlikušos simbolus rindā
            std::cout << "Lūdzu, ievadiet skaitli starp 1 un 6." << std::endl;
            continue;  
        }

        // Izpildām darbību atkarībā no lietotāja izvēlētās opcijas
        if (choice == 1) {
            // Opcija 1: Ievadīt jaunu tekstu
            std::cin.ignore();  // Notīrām jaunas rindas simbolu no ievades bufera
            std::cout << "Ievadiet jaunu teksta virkni: ";
            std::cin.getline(text, 100);  
        } 
        else if (choice == 2) {
            // Opcija 2: Parādīt pašreizējo tekstu
            std::cout << "Teksta virkne: " << text << std::endl;
        } 
        else if (choice == 3) {
            // Opcija 3: Izrēķina un parāda summu no 1 līdz teksta garumam
            int length = 0;
            while (text[length] != '\0') length++;  // Aprēķina teksta garumu

            int sum = length * (length + 1) / 2;  // Aprēķina summu no 1 līdz garumam
            std::cout << "Summa no 1 līdz " << length << " ir: " << sum << std::endl;
        } 
        else if (choice == 4) {
            // Opcija 4: Izvada tekstu reversā
            int length = 0;
            while (text[length] != '\0') length++;  // Aprēķina teksta garumu

            std::cout << "Teksta virkne reversā: ";
            for (int i = length - 1; i >= 0; i--) {
                std::cout << text[i];  // Izvada tekstu apgrieztā secībā
            }
            std::cout << std::endl;
        } 
        else if (choice == 5) {
            // Opcija 5: Saskaita un attēlo katra simbola biežumu 
            int counts[256] = {0};  // Masīvs katra simbola biežuma uzskaitīšanai 
            char order[256];  // Masīvs, lai saglabātu unikālo simbolu secību
            int orderIndex = 0;

            for (int i = 0; text[i] != '\0'; i++) {
                char ch = text[i];
                // Ja simbols parādās pirmo reizi, pievienojam to secības masīvam
                if (counts[ch] == 0) {
                    order[orderIndex++] = ch;
                }
                counts[ch]++;  // Palielinām simbola skaitu
            }

            // Attēlo simbolu biežumus pēc to parādīšanās secības
            std::cout << "Simbolu atkārtojumi:\n";
            for (int i = 0; i < orderIndex; i++) {
                char ch = order[i];
                std::cout << ch << " - " << counts[ch] << std::endl;
            }
        } 
        else if (choice == 6) {
            // Opcija 6: Apturēt programmu
            std::cout << "Programma beidzas." << std::endl;
            break; 
        } 
        else {
            // Ja ievadītā izvēle nav starp 1 un 6
            std::cout << "Nekorekta izvēle! Lūdzu, ievadiet skaitli starp 1 un 6." << std::endl;
        }
    }

    return 0;
}
