#Zad 1
print("Zadanie 1 \n")
lorem_ipsum = " Czym jest Lorem Ipsum?" \
              "Lorem Ipsum jest tekstem stosowanym" \
              "jako przykładowy wypełniacz w przemyśle poligraficznym." \
              "Został po raz pierwszy użyty w XV w. " \
              "przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
              "Pięć wieków później zaczął być używany przemyśle elektronicznym," \
              "pozostając praktycznie niezmienionym. " \
              "Spopularyzował się w latach 60. XX w. wraz " \
              "z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
              "a ostatnio z zawierającym różne wersje " \
              "Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków " \
              "na komputerach osobistych, jak Aldus PageMaker"
#Zad 2
print("Zadanie 2 \n")
imie="Monika"
nazwisko="Nowakowska"


#Zad 3 w format_ciagow.py
print("Zadanie 3 w format_ciagow.py  \n")

#Zad 4
print("Zadanie 4 \n")
zmienna_typu_string=lorem_ipsum
print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize) #ctrl + prawy klawisz przenosi do kodu zrodlowego funckji

#Zad 5
print("Zadanie 5 \n")
i=imie[::-1]
n=nazwisko[::-1]

print(i.capitalize(), n.capitalize())

#Zad 6

print("Zadanie 6 \n")
lista=[1,2,3,4,5,6,7,8,9,10]

len=len(lista)
half=len//2
lista1 = lista[:half]
lista2 = lista[half:]
print(str(lista1), str(lista2))

#Zad 7
print("Zadanie 7  \n")
lista=lista1+lista2
lista.insert(0,0)
lista_copy=lista.copy()
lista_copy.sort(reverse=True)
print(lista_copy)

#Zad 8
print("Zadanie 8 \n")

osoba1=[147821, "Monika Nowakowska"]
osoba2=[235679, "Szymon Kowalski"]
osoba3=[142522, "Oskar Majewski"]
osoba4=[154677,"Mariusz Oklinski"]
lista_osob=[(osoba1+osoba2+osoba3+osoba4)]
print(lista_osob)

#Zad 9
print("Zadanie 9 \n")

slownik=dict([osoba1,osoba2,osoba3,osoba4])


# print(slownik.keys())
slownik[147821]={"telefon":"656567471", "adres":"Marszalkowska 33", "email" : "szymonk@example.com"}
slownik[235679] = {"telefon": "656567472", "adres": "Marszalkowska 35", "email": "oskrexk@example.com"}
slownik[142522] = {"telefon": "656567473", "adres": "Marszalkowska 37", "email": "szymonk@example.com"}
slownik[154677] = {"telefon": "656567474", "adres": "Marszalkowska 39", "email": "szymonk@example.com"}

print("Nowy slownik: ", slownik)

#Zadanie 10
print("Zadanie 10 \n")

lista_telefonow=['883-183-619', '883-183-619','515-456-289', '514-298-515', '789-234-762','515-456-289','514-298-515']
lista_bez_powtorzen=list(set(lista_telefonow))
print(lista_bez_powtorzen)

#Zadanie11

print("Zadanie 11 \n")

for i in range(1,11):
    print(i)

#Zadanie12

print("Zadanie 12 \n")

for i in range(100, -20, -5):
    print(i)

#Zadanie 13
print("Zadanie 13 \n")

lista13=[{"owoc": "kiwi", "zielony":"tak", "smaczny": "tak"}, {"imie:": "Monika", "nazwisko": "Nowakowska", "indeks" :"147821"},
{"pies":"samoyed", "marzenie":"tak"}]

x=""
for i in lista13:
    for k,v in i.items():
        x+=f"{k}:{v} \n"
    x+="\n"

print(x)
