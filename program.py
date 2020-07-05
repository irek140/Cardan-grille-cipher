# Program realizujący szyfrowanie i deszyfrowanie przy użyciu szyfru grilla Cardano
from math import ceil # funkcja odpowiedzialna za zaokrąglanie w górę


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
    try:
        print("Podaj rozmiar grilla/kraty (minimum 4, liczba musi być parzysta) ")
        n = int(input())
        if(n < 4 or n % 2 != 0):
            print("Wprowadzono nieprawidłowy rozmiar!")
            encryption()
    except ValueError:
        print("Wprowadzono nieprawidłowy rozmiar!")
        encryption()

    print("Wpisz wiadomość, która ma zostać zaszyfrowana szyfrem grilla Cardano: ")
    message = input()

    # Pozbycie się z tekstu zbędnych znaków
    message = message.replace(",", "")
    message = message.replace(";", "")
    message = message.replace(".", "")
    message = message.replace("?", "")
    message = message.replace("!", "")
    message = message.replace(":", "")
    message = message.replace(" ", "")

    message = message.upper() # Zamiana liter na duże
    message_char_list = list(message) # Zamiana wprowadzonego tekstu na listę znaków

    # Implementacja algorytmu szyfrującego

    number_of_grills = (ceil(len(message_char_list) / (int(n)*int(n)))) # Wyznaczenie liczby krat(grilli)
    print("Liczba grilli: " + str(number_of_grills))

    grills = []  # Tablica przechowująca fragmenty wiadomości mieszczące się na kratach
    for grille in range(number_of_grills):

        krypto_tab1 = [['X' for x in range(int(n))] for y in range(int(n))] # Tablica na kryptotekst
        krypto_tab2 = [['X' for x in range(int(n))] for y in range(int(n))]
        krypto_tab3 = [['X' for x in range(int(n))] for y in range(int(n))]
        krypto_tab4 = [['X' for x in range(int(n))] for y in range(int(n))]

        ij = int(int(n) / 2) # Wyznaczenie rozmiaru lewego górnego rogu będącego kluczem

        # Przeprowadzenie pierwszej iteracji z wstawieniem 1/4 znaków do kraty
        print("\nPrzeprowadzenie pierwszej iteracji z wstawieniem 1/4 znaków do kraty")
        for i in range(ij):
            for j in range(ij):
                if(message_char_list):
                    krypto_tab1[i][j] = message_char_list.pop(0)

        for i in range(len(krypto_tab1)):
            print(krypto_tab1[i])

        # Obrót kartki między pierwszą, a drugą iteracją
        print("\nObrót kartki między pierwszą, a drugą iteracją")
        for i in range(len(krypto_tab1)):
            for j in range(len(krypto_tab1[i])):
                krypto_tab2[i][j] = krypto_tab1[int(n) - 1 - j][i]

        for i in range(len(krypto_tab2)):
            print(krypto_tab2[i])

        # Przeprowadzenie drugiej iteracji z wstawieniem 2/4 znaków do kraty
        print("\nPrzeprowadzenie drugiej iteracji z wstawieniem 2/4 znaków do kraty")
        for i in range(ij):
            for j in range(ij):
                if(message_char_list):
                    krypto_tab2[i][j] = message_char_list.pop(0)

        for i in range(len(krypto_tab2)):
            print(krypto_tab2[i])

        # Obrót kartki między drugą, a trzecią iteracją
        print("\nObrót kartki między drugą, a trzecią iteracją")
        for i in range(len(krypto_tab2)):
            for j in range(len(krypto_tab2[i])):
                krypto_tab3[i][j] = krypto_tab2[int(n) - 1 - j][i]

        for i in range(len(krypto_tab3)):
            print(krypto_tab3[i])

        # Przeprowadzenie trzeciej iteracji z wstawieniem 3/4 znaków do kraty
        print("\nPrzeprowadzenie trzeciej iteracji z wstawieniem 3/4 znaków do kraty")
        for i in range(ij):
            for j in range(ij):
                if (message_char_list):
                    krypto_tab3[i][j] = message_char_list.pop(0)

        for i in range(len(krypto_tab3)):
            print(krypto_tab3[i])

        # Obrót kartki między trzecią, a czwartą iteracją
        print("\nObrót kartki między trzecią, a czwartą iteracją")
        for i in range(len(krypto_tab3)):
            for j in range(len(krypto_tab3[i])):
                krypto_tab4[i][j] = krypto_tab3[int(n) - 1 - j][i]

        for i in range(len(krypto_tab4)):
            print(krypto_tab4[i])

        # Przeprowadzenie czwartej iteracji z wstawieniem 4/4 znaków do kraty
        print("\nPrzeprowadzenie czwartej iteracji z wstawieniem 4/4 znaków do kraty")
        for i in range(ij):
            for j in range(ij):
                if (message_char_list):
                    krypto_tab4[i][j] = message_char_list.pop(0)

        for i in range(len(krypto_tab4)):
            print(krypto_tab4[i])

        krypto_text = ""

        for i in range(len(krypto_tab4)): # Wydobycie zaszyfrowanych znaków i utworzenie z nich kryptotekstu
            for j in range(len(krypto_tab4[i])):
                krypto_text += krypto_tab4[i][j]

        grills.append(krypto_text)

    encrypted_message = ""
    for i in range(len(grills)):
        for j in range(len(grills[i])):
            encrypted_message += grills[i][j]

    print("\nWyświetlenie kryptotekstu")
    print(grills)
    print(encrypted_message)
    print(message)

    try:
        file = open('kryptotekst.txt', 'w')
        file.write(encrypted_message) # Zapis zaszyfrowanej wiadomości do pliku
    finally:
        file.close()


# Funkcja odpowiadająca za deszyfrowanie
def decryption():
    try:
        plik = open('kryptotekst.txt') # Wczytujemy do programu plik z zaszyfrowaną wiadomością, czyli kryptotekst
        for linia in plik: # Odczytujemy i wyświetlamy linie z tego pliku
            print(linia)

        try:
            print("Deszyfrowanie pliku --- Podaj rozmiar grilla/kraty (minimum 4, liczba musi być parzysta) ")
            n = int(input())
            if (n < 4 or n % 2 != 0):
                print("Wprowadzono nieprawidłowy rozmiar!")
                decryption()


        except ValueError:
            print("Wprowadzono nieprawidłowy rozmiar!")
            decryption()

    finally: plik.close() # Zamykamy plik


# Uruchamiamy menu programu
print("Witaj użytkowniku!")
start_program()
