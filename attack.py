from math import ceil # funkcja odpowiedzialna za zaokrąglanie w górę
from ngram import Ngram_score
global lista
def getLista():
    try:
        global lista
        lista = []
        plik = open('kryptotekst.txt') # Wczytujemy do programu plik z zaszyfrowaną wiadomością, czyli kryptotekst
        for linia in plik: # Odczytujemy i wyświetlamy linie z tego pliku
            lista += list(linia)

    finally: plik.close() # Zamykamy plik

global n
global krypto_tab1
decrypted = []

def pop(lista):
        return lista.pop(0)


def wypelnij_tablice(lista):
    return [[pop(lista) for x in range(int(n))] for y in range(int(n))]

global ij

ws = 0
wk = 0
ks = 0
kk = 0
def obrot(tab):
    tab2 = [['X' for x in range(int(n))] for y in range(int(n))]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab2[i][j] = tab[int(n) - 1 - j][i]
    global krypto_tab1
    krypto_tab1 = tab2
    return tab2

def przekrecIOdczytajZcwiartki(tab):
    obrot(tab)
    encryptedText = []
    for i in range(ws,wk):
        for j in range(ks, kk):
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
            decrypt()
    except ValueError:
        print("Wprowadzono nieprawidłowy rozmiar!")
        decrypt()
    return n



def decrypt(wierszstart, wierszkoniec, kolumnastart, kolumnakoniec):
    global ws
    global wk
    global ks
    global kk
    ws = wierszstart
    wk = wierszkoniec
    ks = kolumnastart
    kk = kolumnakoniec
    decrypted.clear()
    obrot(krypto_tab1)
    for x in range(4):
        decrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1))

    print(makeString(decrypted))

def decryptMore(wierszstart, wierszkoniec, kolumnastart, kolumnakoniec):
    global ws
    global wk
    global ks
    global kk
    global krypto_tab1
    ws = wierszstart
    wk = wierszkoniec
    ks = kolumnastart
    kk = kolumnakoniec
    decrypted.clear()
    getLista()
    numberOfGrills = (ceil(len(lista) / (int(n) * int(n))))
    for grill in range(numberOfGrills):

        krypto_tab1 = [[pop(lista) for x in range(int(n))] for y in range(int(n))]
        obrot(krypto_tab1)
        for x in range(4):
            decrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1))
        krypto_tab1.clear()

    print(makeString(decrypted))

def wykonajAtak():
    global n
    global ij
    global lista
    global krypto_tab1
    getLista()
    n = wpiszRozmiar()
    ij = int(int(n) / 2)  # rozmiar ćwiartki
    if (len(lista) == n * n):
            krypto_tab1 = [[pop(lista) for x in range(int(n))] for y in range(int(n))]
            decrypt(0, ij, 0, ij)
            decrypt(0, ij, ij, n)
            decrypt(ij, n, 0, ij)
            decrypt(ij, n, ij, n)
    elif (len(lista) < n * n):
        print('Wprowadzono za duży rozmiar tablicy.')
        wykonajAtak()
    else:
        print('cw1\n')
        decryptMore(0, ij, 0, ij)
        print('cw2\n')
        decryptMore(0, ij, ij, n)
        print('cw3\n')
        decryptMore(ij, n, 0, ij)
        print('cw4\n')
        decryptMore(ij, n, ij, n)

    mojObiekt = Ngram_score("english_quadgrams.txt")
    liczba = mojObiekt.score(str(decrypted))
    print(liczba)


