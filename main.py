'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''

lista = []

def harommal_oszthatok(listacska):
    szamlalo = 0
    for i in listacska:
        if i % 3 == 0:
            szamlalo += 1
    return print(szamlalo) 


while True:
    bekeres = int(input("Írj egy számot: "))
    lista.append(bekeres)
    if bekeres < 0:
        harommal_oszthatok(lista)
        break
        