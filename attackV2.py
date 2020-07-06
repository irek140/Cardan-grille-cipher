from math import ceil # funkcja odpowiedzialna za zaokrąglanie w górę
from ngram import Ngram_score
import random

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
    print("Jestem w obrocie")
    tab2 = [['X' for x in range(int(n))] for y in range(int(n))]
    for i in range(len(tab2)):
        for j in range(len(tab2[i])):
            tab2[i][j] = tab[int(n) - 1 - j][i]
            print("Jestem w " + str(i) + str(j) + str(tab[int(n) - 1 - j][i]))
    global krypto_tab1
    krypto_tab1 = tab2
    return tab2



def Next(i, j, k):
    if k == 0:
        return[i, j]
    else:
        Next(i, j, k-1)
    return [n-j-1, i]



def decodeKey(key): #[3, 2, 3, 0]
    tab_key = [0 for i in range(n) for j in range(n)] # n na n
    ij = int(int(n) / 2)
    for i in range(ij):
        for j in range(ij):
            nx = Next(i, j, key[i*ij+j])
            tab_key[ n*nx[0] + nx[1] ] = 1

    tab_key2 = [[0 for x in range(int(n))] for y in range(int(n))]
    for i in range(0, int(n)):
        for j in range(0, int(n)):
            tab_key2[int(i)][int(j)] = tab_key.pop(0)
    return tab_key2



def przekrecIOdczytajZcwiartki(tab, tab_key):
    print("przekrecIOdczytajZcwiartki")
    obrot(tab)
    print(tab)
    encryptedText = []
    tab_key = tab_key
    for i in range(0, n):
        print("Jestem w i")
        for j in range(0, n):
            print("Jestem w j")
            if tab_key[i][j] == 1:
                print("Jestem w if")
                encryptedText.append(tab[i][j])
                print(tab[i][j])
    print(encryptedText)
    return encryptedText

def makeString(table):
    string = ""
    for x in table:
        for y in x:
            string += y
    return string

tab_key = []
def wpiszRozmiar():
    try:
        print("Podaj rozmiar grilla/kraty (minimum 4, liczba musi być parzysta) ")
        global n
        n = int(input())

        keyDecoder = losujKlucz(n)
        print(keyDecoder)

        global tab_key
        tab_key = decodeKey(keyDecoder)
        print(tab_key)

        if(n < 4 or n % 2 != 0):
            print("Wprowadzono nieprawidłowy rozmiar!")
            decrypt(tab_key)
    except ValueError:
        print("Wprowadzono nieprawidłowy rozmiar!")
        decrypt(tab_key)
    return n


def losujKlucz(n):
    key = [0 for y in range(int(n))]
    for j in range(0, n):
        key[j] = random.randint(0, n-1)
        print(key[j])
    return key


def decrypt(krypto_tab1, tab_key2):
    decrypted.clear()
    obrot(krypto_tab1)
    for x in range(4):
        decrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1, tab_key2))

    print(makeString(decrypted))
    print("ngram score:")
    liczNGRAM(makeString(decrypted))

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
            print("krypto_tab1" + str(krypto_tab1))
            decrypt(krypto_tab1, tab_key)

            #decrypt(0, ij, ij, n)

            #decrypt(ij, n, 0, ij)

            #decrypt(ij, n, ij, n)

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



def liczNGRAM(argument):
    try:
        mojObiekt = Ngram_score("english_quadgrams.txt")
        liczba = mojObiekt.score(argument)
        print(liczba)
    except:
        print("")

#wpiszRozmiar()