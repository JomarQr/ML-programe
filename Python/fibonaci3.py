def fibonacci(n):
    # Rekursīva funkcija, lai aprēķinātu Fibonači skaitļa vērtību
    if n < 0:
        raise ValueError("Fibonači secība definēta tikai pozitīvajā virzienā.")  # Nodrošinām, ka n ir pozitīvs
    if n == 0:
        return 0  
    elif n == 1:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 


n = int(input("Ievadiet Fibonači skaitļa indeksu (pozitīvs vesels skaitlis):\n"))
try:
    result = fibonacci(n)
    print(f"Fibonači skaitlis ar indeksu {n} ir {result}.")
except ValueError as e:
    print(e)
