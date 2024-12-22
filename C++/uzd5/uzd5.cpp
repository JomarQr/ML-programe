#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;
// Save user input
void saveUniqueCharacters(const string& input) {
    set<char> uniqueChars; // izmantoju setu lai iegutu unikalu simbolus
    for (char c : input) {
        uniqueChars.insert(c);
    }

    // Atver failu un ieraksta unikālos simbolus
    ofstream outFile("textUnique.txt");
    if (outFile.is_open()) {
        for (char c : uniqueChars) {
            outFile << c;
        }
        outFile.close();
        cout << "Unikālie simboli veiksmīgi saglabāti failā textUnique.txt\n";
    } else {
        cerr << "Kļūda, atverot failu textUnique.txt\n";
    }
}

// Function to analyze the file and print statistics
void analyzeFileContent() {
    ifstream inFile("fileText.txt");
    if (!inFile.is_open()) {
        cerr << "Kļūda, atverot failu fileText.txt\n";
        return;
    }

    string word;
    int uppercaseCount = 0;
    int digitCount = 0;
    int threeLetterWordCount = 0;

    // Process each word in the file
    while (inFile >> word) {
        for (char c : word) {
            if (isupper(c)) uppercaseCount++;
            if (isdigit(c)) digitCount++;
        }
        if (word.length() == 3) threeLetterWordCount++;
    }

    inFile.close();

    // Display the results
    cout << "Lielo burtu skaits: " << uppercaseCount << endl;
    cout << "Ciparu skaits: " << digitCount << endl;
    cout << "Vārdu skaits, kas ir 3 burtu gari: " << threeLetterWordCount << endl;
}

void divideLargeNumberBy2(const string& number) {
    string result = ""; 
    int carry = 0;

    for (char digit : number) {
        // Mēs aprēķinām pašreizējo skaitli, ņemot vērā atlikušo daļu
        int current = carry * 10 + (digit - '0');
        result += (current / 2) + '0'; 
        carry = current % 2;           // Atlikums tiek pārsūtīts uz nākamo ciparu
    }

  
    if (result[0] == '0' && result.length() > 1) {
    result.erase(0, 1); // Ja pirmais cipars mūsu rezultata ir 0 tad mēs to delete
    }
    // Ierakstam faiā
    ofstream outFile("bigNumber.txt");
    if (outFile.is_open()) {
        outFile << result;
        outFile.close();
        cout << "Результат сохранён в файл bigNumber.txt\n";
    } else {
        cerr << "Ошибка открытия файла bigNumber.txt\n";
    }
}

int main() {
    // Pieprasa lietotāja ievadi
    string userInput;
    cout << "Ievadiet simbolu virkni: ";
    getline(cin, userInput);

    // Saglabā unikālos simbolus
    saveUniqueCharacters(userInput);

    // Task 2: Analyze file content
    cout << "fileText.txt analysis: \n";
    analyzeFileContent();
    // Task 3: BigNumber devide by 2
    string bigNumber = "12345678912345678912345678911234567891234567891234567891123456789123456789";
    divideLargeNumberBy2(bigNumber);

    return 0;
}
