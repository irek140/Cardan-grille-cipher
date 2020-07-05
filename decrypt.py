
tekst = "EPNASAIALMTOAAKA"


lista = list(tekst)

n = 4

decrypted = []

def pop(lista):
    return lista.pop(0)


def wypelnij_tablice(lista):
    return [[pop(lista) for x in range(int(n))] for y in range(int(n))]

krypto_tab1 = wypelnij_tablice(lista)

ij = int(int(n) / 2) #rozmiar ćwiartki


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
    for i in range(ij):
        for j in range(ij):
            encryptedText.append(tab[i][j])
    return encryptedText



obrot(krypto_tab1)

for x in range(4):
    decrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1))

print(decrypted)