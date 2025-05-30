def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Błąd: Dzielenie przez zero"
    return a / b

if __name__ == "__main__":
    print("Prosty kalkulator")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == "+":
        print("Wynik:", dodaj(a, b))
    elif operacja == "-":
        print("Wynik:", odejmij(a, b))
    elif operacja == "*":
        print("Wynik:", mnoz(a, b))
    elif operacja == "/":
        print("Wynik:", dziel(a, b))
    elif operacja == "**":
        print("Wynik:", poteguj(a, b))
    else:
        print("Nieznana operacja.")

def poteguj(a, b):
    return a ** b
