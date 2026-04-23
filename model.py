import random

# Symulacja bazy danych (w przyszłości tu będą Twoje dane)
dane = ["kot", "pies", "ptak"]
wiedza_ai = {}

def ucz_sie():
    print("AI rozpoczyna naukę...")
    # AI losuje 'wagę' dla każdego słowa - to uproszczony model uczenia
    for slowo in dane:
        wiedza_ai[slowo] = random.random()
    
    with open("wynik_nauki.txt", "w") as f:
        f.write(f"Stan wiedzy AI: {wiedza_ai}")
    print("Nauka zakończona. Wynik zapisany w wynik_nauki.txt")

if __name__ == "__main__":
    ucz_sie()
