# test_kalkulator.py

from src_kalkulator import dodaj, odejmij, mnoz, dziel, poteguj

def test_dodaj():
    assert dodaj(2, 3) == 5

def test_odejmij():
    assert odejmij(5, 3) == 2

def test_mnoz():
    assert mnoz(3, 4) == 12

def test_dziel():
    assert dziel(10, 2) == 5
    assert dziel(10, 0) == "Błąd: Dzielenie przez zero"

def test_poteguj():
    assert poteguj(2, 3) == 8
