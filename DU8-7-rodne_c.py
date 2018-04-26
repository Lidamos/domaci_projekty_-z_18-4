""" rodné číslo - zadání"""
rodne_cislo = input("Zadej rodné číslo i s lomítkem: ")



""" kontrola správného formátu rod. čísla"""
while len(rodne_cislo) != 11:
    print("Chybný počet znaků.")
    rodne_cislo = input("Zadej znovu r.č. s lomítkem: ")
    while "/" != rodne_cislo[6]:
        print("Číslo není správně napsané!")
        rodne_cislo = input("Zadej znovu r.č. s lomítkem: ")
print("Lomítko je na svém místě.")
print("Číslo je ve správném formátu.")
print()



""" kontrola dělitelnosti 11"""
datumove_cislo = rodne_cislo[:6]
rok = int(datumove_cislo[:2])
mesic = int(datumove_cislo[2:4])
den = int(datumove_cislo[4:6])

datum_1 = int(datumove_cislo[0])
datum_2 = int(datumove_cislo[1])
datum_3 = int(datumove_cislo[2])
datum_4 = int(datumove_cislo[3])
datum_5 = int(datumove_cislo[4])
datum_6 = int(datumove_cislo[5])
datum_soucet = datum_1 + datum_2 + datum_3 + datum_4 + datum_5 + datum_6
print("datumová část:", datumove_cislo)
print("mezisoučet", datum_soucet)

kontrolni_cislo =rodne_cislo[7:]
kontrolni_1 = int(kontrolni_cislo[0])
kontrolni_2 = int(kontrolni_cislo[1])
kontrolni_3 = int(kontrolni_cislo[2])
kontrolni_4 = int(kontrolni_cislo[3])
kontrolni_soucet = kontrolni_1 + kontrolni_2 + kontrolni_3 + kontrolni_4
print("kontrolní část:", kontrolni_cislo)
print("mezisoučet:", kontrolni_soucet)

soucet_vsech_cislic = datum_soucet + kontrolni_soucet
print("součet obou mezisoučtů:", soucet_vsech_cislic)
print()

konecny_soucet = str(soucet_vsech_cislic)
konecne_cislo_1a =konecny_soucet[0]
konecne_cislo_2a =konecny_soucet[1]
vysledek = int(konecne_cislo_1a) + int(konecne_cislo_2a)
print("konečný součet všech číslic je:", vysledek)

if vysledek == 11:
     print("Rodné číslo je dělitelné 11.")
else:
     print("CHYBA - rodné číslo není dělitelné 11.")
print()



""" dekódování datumu """
letopocet = "19"

if mesic > 50:
    mz = mesic - 50
    print("Rodné číslo patří ženě, narozené v", ("{0}.".format(mz))," měsíci.")
    print("Dekódované datum narozeni: den", ("{0}.".format(den)),"    měsíc", ("{0}.".format(mz)), "   rok", ("{}{}".format(letopocet, rok)))
elif mesic < 50:
    print ("Rodné číslo patří muži, narozenému v",("{0}.".format(mesic)),"měsíci.")
    print("Dekódované datum narozeni: den", ("{0}.".format(den)),"    měsíc", ("{0}.".format(mesic)), "   rok", ("{}{}".format(letopocet, rok)))
