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
    print("Wpisz wiadomość, która ma zostać zaszyfrowana szyfrem grilla Cardano: ")
    message = input()

    message_char_list = list(message) # Zamiana wprowadzonego tekstu na listę znaków

    # Implementacja algorytmu szyfrującego
    krypto_tab = []
    number_of_grills = (ceil(len(message_char_list) / 36)) # Wyznaczenie liczby krat(grilli)
    grills = [] # Tablica przechowująca fragmenty wiadomości mieszczące się na kratach
    for grille in range(number_of_grills): # Podział wiadomości na kraty zawierające 36 znaków
        grill = []
        for i in range(36):
            if(len(message_char_list) > 0):
                print("Iteracja: "); print(i)
                print("Grill: "); print(grill)
                print("Litera do grilla: "); print(message_char_list[0])
                grill.append(message_char_list[0])
                message_char_list.pop(0)
                print("Wiadomość: "); print(message_char_list)
                print("###################################################")
        grills.append(grill)
        print(grill)
    print(grills)



    try:
        file = open('kryptotekst.txt', 'w')
        file.write(message) # Zapis zaszyfrowanej wiadomości do pliku
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
