import random

while True:
    print("Laipni lūdzam skaitļu minēšanas spēlē!")
    print("Es esmu izvēlējies skaitli no 1 līdz 100. Mēģiniet to uzminēt!")

    # Izvēlies random skaitli
    pareizais_skaitlis = random.randint(1, 100)
    mēģinājumi = 0
    norāde_sniedza = False

    while True:
        lietotāja_ievade = input("Ievadiet skaitli (vai rakstiet 'beigt', lai izietu): ").strip()

        # Checking vai lietotājs vēlas iziet
        if lietotāja_ievade.lower() == "beigt":
            print("Paldies par spēli! Uz redzēšanos")
            exit() #shut down the program lai nestradātu 2nd while

        # Checking vai ievade ir derīgs skaitlis
        if not lietotāja_ievade.isdigit():
            print("Lūdzu, ievadiet derīgu veselu skaitli")
            continue

        # Change ievadi uz veselu skaitli
        minējums = int(lietotāja_ievade)
        mēģinājumi += 1

        # Pārbauda minējumu
        if minējums < 1 or minējums > 100:
            print("Lūdzu, ievadiet skaitli diapazonā no 1 līdz 100")
        elif minējums < pareizais_skaitlis:
            print("Pārāk mazs! Mēģiniet vēlreiz")
        elif minējums > pareizais_skaitlis:
            print("Pārāk liels! Mēģiniet vēlreiz")
        else:
            print(f"Apsveicu! Jūs uzminējāt pareizo skaitli {pareizais_skaitlis}!")
            print(f"Jums bija nepieciešami {mēģinājumi} mēģinājumi")
            break

        # Sniedz norādi pēc 5 mēģinājumiem
        if mēģinājumi == 5 and not norāde_sniedza:
            norāde_sniedza = True
            if pareizais_skaitlis <= 50:
                print("Norāde: Skaitlis atrodas diapazonā no 1 līdz 50.")
            else:
                print("Norāde: Skaitlis atrodas diapazonā no 51 līdz 100.")

    while True:
          vēlreiz = input("Vai vēlaties spēlēt vēlreiz? (jā/nē): ").strip().lower()
          if vēlreiz == "jā":
              break
          elif vēlreiz == "nē":
              print("Paldies par spēli. Uz redzēšanos!")
              exit()
          else:
              print("Lūdzu, ievadiet 'jā' vai 'nē'.")
