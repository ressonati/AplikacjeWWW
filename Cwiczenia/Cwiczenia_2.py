#Zadanie 1

print("Zadanie 1 \n")


def zadanie1(lista, listb):
    parzyste=[]
    nieparzyste=[]
    for i in lista:
        if i%2==0:
            parzyste.append(i)
    for j in listb:
        if j % 2 == 1:
            nieparzyste.append(j)
    return parzyste+nieparzyste




a_list=[1,2,2,3,4,5,6,7,8]
b_list=[4,5,7,8,2,9,10]

print(zadanie1(a_list,b_list))

#Zadanie 2

print("Zadanie 2 \n")

def zadanie2(data_text):
    dict = {
        "lenght": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower(),
    }
    return dict

dict="doggo dog "
print(zadanie2(dict))

#Zadanie 3

print("Zadanie 3 \n")

def zadanie3(text, letter):
    return text.replace(letter, "")

print(zadanie3(dict, "dog"))

#Zadanie 4
print("\nZadanie 4 \n")

def zadanie4(temp, temp_type):
    if temp_type=="F":
        temp=temp*1.8+32
        return temp
    elif temp_type=="K":
        temp=temp+273
        return temp
    elif temp_type=="R":
        temp=(temp+273.15) *9 / 5
        return temp
print(zadanie4(25,"R"))

#Zadanie 5
print("\nZadanie 5 \n")

class Calculator:
    def add(x,y):
        return x+ y
    def diffrence(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        if y==0:
            return "nie dziel przez 0 cholero!"
        else:
            return x/y
print(Calculator.add(4,5),Calculator.diffrence(5,2))


#Zadanie 6
print("\nZadanie 6 \n")
class ScienceCalculator(Calculator):
    def power(x,y):
        return x**y

print(ScienceCalculator.power(4,5))


#Zadanie 7
print("\nZadanie 7 \n")
def zadanie7(text):
    return text[::-1]


print(zadanie7("kotel"))


#Zadanie 9
from file import Filemanager
print("\nZadanie 9 \n")

object=Filemanager("just_text.txt")
object.read_file()
object.update_file("\n text na koniec \n")
object.read_file()
