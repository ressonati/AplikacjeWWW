#Zad 1

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

imie="Monika"
nazwisko="Nowakowska"
#o co chodzi #TODO dowiedziedz sie o co chodzi

#Zad 3 w format_ciagow.py


#Zad 4
zmienna_typu_string=lorem_ipsum
print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize) #ctrl + prawy klawisz przenosi do kodu zrodlowego funckji

#Zad 5

i=imie[::-1]
n=nazwisko[::-1]

print(i.capitalize(), n.capitalize())

#Zad 6

lista=[1,2,3,4,5,6,7,8,9,10]

lista1=[i[1] for i in lista]
lista2=[i[2]for i in lista]
print(str(lista1), str(lista2))
