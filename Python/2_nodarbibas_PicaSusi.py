ediens = ["Pica", "Suši", "Pasta"]

while True:

  print("Izvēlne:")
  print("1 - Pievienot vienumu sarakstam")
  print("2 - Noņemt vienumu no saraksta")
  print("3 - Parādīt saraksta garumu")
  print("4 - Parādīt saraksta vienumus")
  print("5 - Beigt programmu")

  choice = input("Ievadi opciju: ")

  # Pievienot edienu
  if choice == "1":
    while True:
        
        item = input("Ievadiet ēdiena nosaukumu, ko pievienot: ").strip()

        if item == "":
              print("Darbība atcelta. Atgriežamies pie izvelnes")
              break
        
        # Checking lai ievads būtu str and nebūtu tukšs
        if item.isalpha() and len(item) > 0:
            ediens.append(item)
            print(f'"{item}" ir pievienots sarakstam')
            break
        else:
            print("Lūdzu, ievadiet derīgu ēdiena nosaukumu (tikai burtus)")


  elif choice == "2":
    # Noņemt vienumu
    if ediens:
        print("Pašreizējie saraksta vienumi:")
        for i in range(len(ediens)):
            print(f"{i + 1}. {ediens[i]}")
        
        while True:
            index = input("Ievadiet noņemamā vienuma numuru vai 0, lai atceltu: ")
            if index.isdigit():  # Parbaudam lai butu ievaditi tikai cipari
                index = int(index) - 1
                if index == -1:  # Ja lietotājs ievada 0, atceliet dzēšanu
                    print("Darbība atcelta")
                    break
                elif 0 <= index < len(ediens):
                    removed_item = ediens.pop(index)
                    print(f'"{removed_item}" ir noņemts no saraksta')
                    break
                else:
                    print("Nekorekts numurs. Mēģiniet vēlreiz")
            else:
                print("Lūdzu, ievadiet derīgu numuru")
    else:
        print("Saraksts ir tukšs. Nav ko noņemt")

  elif choice == "3":
        # Saraksta garums
        print(f"Sarakstā ir {len(ediens)} vienumi")

  
  elif choice == "4":
    # Parādīt visus vienumus sarakstā ar numuriem
    if len(ediens) > 0:
        print("Pašreizējie saraksta vienumi:")
        for i in range(len(ediens)):
            print(f"{i + 1}. {ediens[i]}")  # Izvedam numuru (i + 1 jo saraksts saksies ar 0) un edienu
    else:
        print("Saraksts ir tukšs")


  elif choice == "5":
        # Beigt programmu
        print("Programma beidzas")
        break
  
  else:
        print("Nekorekta izvēle. Lūdzu mēģiniet vēlreiz")



    