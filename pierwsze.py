
def dluga_nazwa_funkcji():
    """parametry: ... """ #tzw. docstring
    print ("hello world!")
# dlugaNazwaFunkcji
# pep8 pep0008
# Guido van Rossum
# Ctrl + /   = komentuj/odkomentuj
# shift + alt + strzalka gora/dol
# łańcuch znaków ====================================================
imie = "Ala"
imie = 'Ala ma kota'
imie = """Ala ma
kota a
kot jest glodny."""

print(type(imie))
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isinstance() sprawdzam czy zmienna jest danego typu
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print("Ala" + "ma kota.")
# print("ala "+ "ma" + 5 + "kotów.") błąd
print ("Ala" + "ma" + str(5) + "kotów.")
int(5)
ilosc_kotow = 5
print("Ala " + "ma {} kotów.".format(ilosc_kotow))
print("Ala " + f"ma {ilosc_kotow} kotów.")
print("Ala ma {1}{0}{2} kotów".format (4,5,7))
liczba = 6.85985498504
print(f"liczba {liczba: .2f}") # 2 miejsca dziesiętne
#http://pyformat.info

print(imie[0])
#imie[0] = "0 nie jest mutowalny"
imie = imie.lower()
print(imie)
# liczby
liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print (1 + 2)
print (1 - 2)
print (1 / 2)
print (1 * 2)
print (1 // 2)  #dzielenie bez reszty
print (1 ** 2)  # podniesienie do potegi
print (1 % 2) #dzielenie modulo (reszta)

print (0.1 + 0.2 == 0.3)
print (f"{0.1: .30f}")

#listy==================

lista = []
lista2 =[1, 2, 3]
lista3 =[1, "Ala", 3.4, True, None]


final_list = lista + lista2 + lista3
lista2[2] # wartosc 3,indeks 2

lista4 = [
        [1, 2, 3],
        [3, 5, 6],
        [7, 8, 9]
 ]

 lista4[1][1] #5

 # słownik

 slownik= {}
 slownik2 ={"klucz": "wartość"}
 slownik3 ={0: "Adam"}
 slownik2 ["klucz"]
 slownik2 [0]

 slownik2.keys()
 slownik2.values()






