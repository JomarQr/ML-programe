# Lūdz lietotājam ievadīt skaitli
ievadītais_skaitlis = int(input("Ievadiet skaitli: ").strip())

# Aprēķina summu skaitļiem no 1 līdz ievadītajam skaitlim, kas dalās ar 7
summa = sum(i for i in range(1, ievadītais_skaitlis + 1) if i % 7 == 0)

print(f"Summa skaitļiem intervālā no 1 līdz {ievadītais_skaitlis}, kas dalās ar 7, ir {summa}")
