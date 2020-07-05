
tekst = "EPNASAIALMTOAAKA"


lista = list(tekst)

n = 4

encrypted = []

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


# # Przeprowadzenie pierwszej iteracji z wstawieniem 1/4 znaków do kraty
#         print("\nPrzeprowadzenie pierwszej iteracji z wstawieniem 1/4 znaków do kraty")
#         for i in range(ij):
#             for j in range(ij):
#                 if(message_char_list):
#                     krypto_tab1[i][j] = message_char_list.pop(0)
#
#         for i in range(len(krypto_tab1)):
#             print(krypto_tab1[i])
#
#         # Obrót kartki między pierwszą, a drugą iteracją
#         print("\nObrót kartki między pierwszą, a drugą iteracją")
#         for i in range(len(krypto_tab1)):
#             for j in range(len(krypto_tab1[i])):
#                 krypto_tab2[i][j] = krypto_tab1[int(n) - 1 - j][i]
#
#         for i in range(len(krypto_tab2)):
#             print(krypto_tab2[i])

obrot(krypto_tab1)

for x in range(4):
    encrypted.append(przekrecIOdczytajZcwiartki(krypto_tab1))

print(encrypted)