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

    krypto_tab = []
    number_of_grills = (ceil(len(message_char_list) / 36)) # Wyznaczenie liczby krat(grilli)
    grills = [] # Tablica przechowująca fragmenty wiadomości mieszczące się na kratach
    for grille in range(number_of_grills): # Podział wiadomości na kraty zawierające 36 znaków
        grille = []
        for i in range(36):
            if(len(message_char_list) > 0):
                print("Iteracja: "); print(i)
                print("Grill: "); print(grille)
                print("Litera do grilla: "); print(message_char_list[0])
                grille.append(message_char_list[0])
                message_char_list.pop(0)
                print("Wiadomość: "); print(message_char_list)
                print("###################################################")
        grills.append(grille)
        print(grille)
    print(grills)

    for grille in range(number_of_grills): # Obsługa szyfrowania każdej kraty
        print("Szyfrowanie - krata: "); print(grille)
        krypto_grille = [] # Utworzenie listy z zaszyfrowaną kratą
        for i in range(36):
            krypto_grille.append('x')
        # Przeprowadzenie szyfrowania transpozycyjnego
        if(len(grills[grille]) >= 1): krypto_grille[4] = grills[grille][0]
        if(len(grills[grille]) >= 2): krypto_grille[5] = grills[grille][1]
        if(len(grills[grille]) >= 3): krypto_grille[9] = grills[grille][2]
        if(len(grills[grille]) >= 4): krypto_grille[11] = grills[grille][3]
        if(len(grills[grille]) >= 5): krypto_grille[15] = grills[grille][4]
        if(len(grills[grille]) >= 6): krypto_grille[16] = grills[grille][5]
        if(len(grills[grille]) >= 7): krypto_grille[18] = grills[grille][6]
        if(len(grills[grille]) >= 8): krypto_grille[25] = grills[grille][7]
        if(len(grills[grille]) >= 9): krypto_grille[32] = grills[grille][8]
        if(len(grills[grille]) >= 10): krypto_grille[2] = grills[grille][9]
        if(len(grills[grille]) >= 11): krypto_grille[7] = grills[grille][10]
        if(len(grills[grille]) >= 12): krypto_grille[12] = grills[grille][11]
        if(len(grills[grille]) >= 13): krypto_grille[21] = grills[grille][12]
        if(len(grills[grille]) >= 14): krypto_grille[22] = grills[grille][13]
        if(len(grills[grille]) >= 15): krypto_grille[27] = grills[grille][14]
        if(len(grills[grille]) >= 16): krypto_grille[29] = grills[grille][15]
        if(len(grills[grille]) >= 17): krypto_grille[34] = grills[grille][16]
        if(len(grills[grille]) >= 18): krypto_grille[35] = grills[grille][17]
        if(len(grills[grille]) >= 19): krypto_grille[3] = grills[grille][18]
        if(len(grills[grille]) >= 20): krypto_grille[10] = grills[grille][19]
        if(len(grills[grille]) >= 21): krypto_grille[17] = grills[grille][20]
        if(len(grills[grille]) >= 22): krypto_grille[19] = grills[grille][21]
        if(len(grills[grille]) >= 23): krypto_grille[20] = grills[grille][22]
        if(len(grills[grille]) >= 24): krypto_grille[24] = grills[grille][23]
        if(len(grills[grille]) >= 25): krypto_grille[26] = grills[grille][24]
        if(len(grills[grille]) >= 26): krypto_grille[30] = grills[grille][25]
        if(len(grills[grille]) >= 27): krypto_grille[31] = grills[grille][26]
        if(len(grills[grille]) >= 28): krypto_grille[0] = grills[grille][27]
        if(len(grills[grille]) >= 29): krypto_grille[1] = grills[grille][28]
        if(len(grills[grille]) >= 30): krypto_grille[6] = grills[grille][29]
        if(len(grills[grille]) >= 31): krypto_grille[8] = grills[grille][30]
        if(len(grills[grille]) >= 32): krypto_grille[13] = grills[grille][31]
        if(len(grills[grille]) >= 33): krypto_grille[14] = grills[grille][32]
        if(len(grills[grille]) >= 34): krypto_grille[23] = grills[grille][33]
        if(len(grills[grille]) >= 35): krypto_grille[28] = grills[grille][34]
        if(len(grills[grille]) >= 36): krypto_grille[33] = grills[grille][35]
        print(krypto_grille) # Wyswietlenie zaszyfrowanej kraty
        krypto_tab.append(krypto_grille) # Dodanie zaczyfrowanej kraty do wynikowej listy zaszyfrowanych znaków

    print(message)
    print(krypto_tab) # Wyświetlenie listy z zaszyfrowaną wiadomością
    krypto_text = ""

    for i in range(len(krypto_tab)): # Wydobycie zaszyfrowanych znaków i utworzenie z nich kryptotekstu
        for j in range(len(krypto_tab[i])):
            krypto_text += krypto_tab[i][j]

    print(krypto_text)

    try:
        file = open('kryptotekst.txt', 'w')
        file.write(krypto_text) # Zapis zaszyfrowanej wiadomości do pliku
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
