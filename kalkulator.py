def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Błąd: Nie można dzielić przez zero!"
    else:
        return a / b

# Funkcja główna
def main():
    print("Prosty kalkulator")
    print("Dostępne operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    try:
        operacja = int(input("Wybierz numer operacji (1-4): "))
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if operacja == 1:
            wynik = dodawanie(liczba1, liczba2)
        elif operacja == 2:
            wynik = odejmowanie(liczba1, liczba2)
        elif operacja == 3:
            wynik = mnozenie(liczba1, liczba2)
        elif operacja == 4:
            wynik = dzielenie(liczba1, liczba2)
        else:
            print("Błąd: Wybrano nieprawidłową operację.")
            return

        print("Wynik: ", wynik)

    except ValueError:
        print("Błąd: Wprowadzone dane są nieprawidłowe.")

if __name__ == "__main__":
    main()
