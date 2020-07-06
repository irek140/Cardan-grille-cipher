from math import ceil # funkcja odpowiedzialna za zaokrąglanie w górę


def getLista(): # Odczytanie znaków z zaszyfrowanego pliku
    try:
        global lista
        lista = []
        plik = open('kryptotekst.txt') # Wczytujemy do programu plik z zaszyfrowaną wiadomością, czyli kryptotekst
        for linia in plik: # Odczytujemy i wyświetlamy linie z tego pliku
            lista += list(linia);

    finally: plik.close() # Zamykamy plik


n = 4

decrypted = []

def pop(lista):
    return lista.pop(0)


global krypto_tab1

ij = int(int(n) / 2) #rozmiar ćwiartki

def obrot(tab):
    tab2 = [['X' for x in range(int(n))] for y in range(int(n))]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab2[i][j] = tab[int(n) - 1 - j][i]
    global krypto_tab1
    krypto_tab1 = tab2
    return tab2

#key = [0 for i in range(ij) for j in range(ij)]

def Next(i, j, k):
    if k == 0:
        return[i, j]
    else:
        Next(i, j, k-1)
    return [n-j-1, i]

def decodeKey(key):
    tab = [0 for i in range(n) for j in range(n)]
    for i in range(ij):
        for j in range(ij):
            nx = Next(i, j, key[i*ij+j])
            tab[ n*nx[0] + nx[1] ] = 1
    return tab

def przekrecIOdczytajZcwiartki(tab, key):
    obrot(tab)
    encryptedText = [] # 4x4 (1,1,0,0 ; 1,1,0,0 ; 0,0,0,0 ; 0,0,0,0)
    for i in range(ij):
        for j in range(ij):
            encryptedText.append(tab[i][j])
    return encryptedText


def makeString(table):
    string = ""
    for x in table:
        for y in x:
            string += y
    return string


def wpiszRozmiar():
    try:
        print("Podaj rozmiar grilla/kraty (minimum 4, liczba musi być parzysta) ")
        global n
        n = int(input())
        if(n < 4 or n % 2 != 0):
            print("Wprowadzono nieprawidłowy rozmiar!")
            wpiszRozmiar()
    except ValueError:
        print("Wprowadzono nieprawidłowy rozmiar!")
        wpiszRozmiar()
    return n


def wykonajDecrypt():
    global n
    n = wpiszRozmiar()
    global ij

    ij = int(int(n) / 2)
    global krypto_tab1 # Tablica do przechowywania odszyfrowywanego tekstu
    global lista # Lista ze znakami zaszyfrowanej wiadomości
    getLista()
    if (len(lista) == n*n):
            krypto_tab1 = [[pop(lista) for x in range(int(n))] for y in range(int(n))]
            obrot(krypto_tab1)
            makeEncryptedText()
    elif (len(lista) < n * n):
        print('Wprowadzono za duży rozmiar tablicy.')
        wykonajDecrypt()
    else:
        numberOfGrills = (ceil(len(lista) / (int(n) * int(n))))
        for grill in range(numberOfGrills):
            try:
                krypto_tab1 = [[pop(lista) for x in range(int(n))] for y in range(int(n))]
                obrot(krypto_tab1)
                makeEncryptedText()
                krypto_tab1.clear()
            except IndexError:
                decrypted.clear()
                print("Wprowadzono za mały rozmiar tablicy.")
                wykonajDecrypt()
    print(makeString(decrypted))


def makeEncryptedText():
    for x in range(4):
        decrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1))



print(makeString(decrypted))
