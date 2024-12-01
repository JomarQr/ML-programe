alphabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_lat = ['ā', 'č', 'ē', 'ģ', 'ī', 'ķ', 'ļ', 'ņ', 'š', 'ū', 'ž']
alphabet = alphabet_lat + alphabet_eng  
special_chars = "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "  # Speciālie simboli

def caesar_cipher(text, shift, direction):
    output_text = ""
    shift = shift % len(alphabet)  # Nobīdē lielu skaitli
    if direction == "decode":
        shift = -shift  # Dekodējot, nobīde pretējā virzienā
    for char in text:
        if char in special_chars:  # Speciālie simboli nemainās
            output_text += char
        elif char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)  
            output_text += alphabet[new_position]
        else:
            output_text += char  # Ja simbols nav alfabētā, to nemainām
    return output_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()  # Programma ari darbojas, ja lietotājs raksta ar lielajiem burtiem
    if direction == "exit":
        print("Exiting program. Goodbye!")
        break
    elif direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()  # Ziņa tiek pārveidota uz mazajiem burtiem
        try:
            shift = int(input("Type the shift number:\n"))  # Nobīdes skaitlis
        except ValueError:  # Paziņojums, ja ievadīts nepareizs "int" vērtības formāts
            print("Please enter a valid number for the shift.")
            continue
        result = caesar_cipher(text, shift, direction)
        print(f"The {direction}d text is '{result}'")  # Atgriež šifrēto vai dešifrēto tekstu
    else:
        print("Invalid choice. Please choose 'encode', 'decode', or 'exit'.")  # Paziņojums par nepareizu izvēli
