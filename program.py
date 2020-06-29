# Program realizujący szyfrowanie i deszyfrowanie przy użyciu szyfru grilla Cardano


# Funkcja rozpoczynająca działanie menu programu
def start_program():
    print("Jeżeli chcesz zaszyfrować wiadomość wpisz S i naciśnij ENTER; jeżeli chcesz" +
              " odszyfrować wiadomość wpisz D i naciśnij ENTER")
    f = input() # Wczytujemy instrukcję, w której użytkownik decyduje której funkcji programu chce użyć
    if (f == "S"):
        encryption()
    elif (f == "D"):
        decryption()
    else:
        print("Wprowadź poprawną instrukcję!")
        start_program()


# Funkcja odpowiadająca za szyfrowanie
def encryption():
    print("Wpisz wiadomość, która ma zostać zaszyfrowana szyfrem grilla Cardano: ")
    message = input()
    try:
        file = open('kryptotekst.txt', 'w')
        file.write(message) # Zapis do pliku
    finally:
        file.close()


# Funkcja odpowiadająca za deszyfrowanie
def decryption():
    #print("Wybierz plik z zaszyfrowaną wiadomością, która ma zostać odszyfrowana: ")
    try:
        plik = open('kryptotekst.txt') # Wczytujemy do programu plik z zaszyfrowaną wiadomością, czyli kryptotekst
        for linia in plik: # Odczytujemy i wyświetlamy linie z tego pliku
            print(linia)

    finally: plik.close() # Zamykamy plik


# Uruchamiamy menu programu
print("Witaj użytkowniku!")
start_program()
