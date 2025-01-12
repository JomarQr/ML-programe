import os
import json

file_name = "ediens.json"

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        try:
            ediens = json.load(file)
            print("Fails atrasts")
        except json.JSONDecodeError:
            ediens = []
            print("Fails ir tukšs vai bojāts")
else:
    ediens = []
    print("Fails netika atrasts, sākam ar tukšu sarakstu")

while True:
    print("\nIzvēlne:")
    print("1 - Pievienot vienumu sarakstam")
    print("2 - Noņemt vienumu no saraksta")
    print("3 - Parādīt saraksta garumu")
    print("4 - Parādīt saraksta vienumus")
    print("5 - Beigt programmu")

    choice = input("Ievadi opciju: ")

    # Pievienot ēdienu
    if choice == "1":
        while True:
            item = input("Ievadiet ēdiena nosaukumu, ko pievienot: ").strip()

            if item == "":
                print("Darbība atcelta. Atgriežamies pie izvēlnes")
                break

            if item.isalpha() and len(item) > 0:
                ediens.append(item)
                print(f'\"{item}\" ir pievienots sarakstam')
                break
            else:
                print("Lūdzu, ievadiet derīgu ēdiena nosaukumu (tikai burtus)")

    # Noņemt vienumu
    elif choice == "2":
        if ediens:
            print("Pašreizējie saraksta vienumi:")
            for i in range(len(ediens)):
                print(f"{i + 1}. {ediens[i]}")

            while True:
                index = input("Ievadiet noņemamā vienuma numuru vai 0, lai atceltu: ")
                if index.isdigit():
                    index = int(index) - 1
                    if index == -1:
                        print("Darbība atcelta")
                        break
                    elif 0 <= index < len(ediens):
                        removed_item = ediens.pop(index)
                        print(f'\"{removed_item}\" ir noņemts no saraksta')
                        break
                    else:
                        print("Nekorekts numurs, mēģiniet vēlreiz")
                else:
                    print("Lūdzu, ievadiet derīgu numuru")
        else:
            print("Saraksts ir tukšs. Nav ko noņemt")

    # Saraksta garums
    elif choice == "3":
        print(f"Sarakstā ir {len(ediens)} vienumi")

    # Parādīt visus vienumus sarakstā
    elif choice == "4":
        if len(ediens) > 0:
            print("Pašreizējie saraksta vienumi:")
            for i, item in enumerate(ediens, start=1):
                print(f"{i}. {item}")
        else:
            print("Saraksts ir tukšs")

    # Beigt programmu
    elif choice == "5":
        while True:
            
          save_choice = input("Vai vēlaties saglabāt sarakstu pirms iziešanas? (ja/ne): ").strip().lower()
          if save_choice == "ja":
              with open(file_name, "w", encoding="utf-8") as file:
                  json.dump(ediens, file, ensure_ascii=False, indent=4)
              print("Saraksts ir saglabāts, programma beidzas.")
              break
          elif save_choice == "ne":
              print("Saraksts netika saglabāts, programma beidzas.")
              break
          else: 
              print("Nekorekta izvēle. Lūdzu, ievadiet \"ja\" vai \"ne\".")
        break

    else:
        print("Nekorekta izvēle. Lūdzu mēģiniet vēlreiz")
