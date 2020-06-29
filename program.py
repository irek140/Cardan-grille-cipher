# Program realizujący szyfrowanie i deszyfrowanie przy użyciu szyfru grilla Cardano


# Funkcja rozpoczynająca działanie menu programu
def start_program():
    print("Witaj użytkowniku! \nJeżeli chcesz zaszyfrować wiadomość wpisz S i naciśnij ENTER; jeżeli chcesz" +
              " odszyfrować wiadomość wpisz D i naciśnij ENTER")
    f = input()
    if (f == "S"):
        encryption()
    elif (f == "D"):
        decryption()
    else:
        start_program()


# Funkcja odpowiadająca za szyfrowanie
def encryption():
    print("Wpisz wiadomość, która ma zostać zaszyfrowana szyfrem grilla Cardano: ")


# Funkcja odpowiadająca za deszyfrowanie
def decryption():
    print("Wybierz plik z zaszyfrowaną wiadomością, która ma zostać odszyfrowana: ")


# Uruchamiamy menu programu
start_program()
