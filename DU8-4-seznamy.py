zvirata_1 = "pes", "kočka", "králík", "had"
zvirata_2 = "koala", "lev", "had", "pes"

print("1. seznam zvířat:", zvirata_1)
print("2. seznam zvířat:", zvirata_2)
print()



""" zvířata jsou v obou seznamech:"""
v_obou_seznamech=("")       # n-tice

for x in zvirata_1:
    for y in zvirata_2:
        if x == y:
            v_obou_seznamech += x + ", "
print("V obou seznamech jsou: ", v_obou_seznamech)



""" zvířata jsou jen v 1. seznamu:"""
v_seznamu_1 =[]   #seznam

for x in zvirata_1:
    if x in zvirata_2:
        pass
    else:
        v_seznamu_1.append(x)
print("Jen v seznamu 1 jsou: ", v_seznamu_1)



""" zvířata jsou jen v 2. seznamu:"""
v_seznamu_2 =[]     #seznam

for x in zvirata_2:
    if x in zvirata_1:
        pass
    else:
        v_seznamu_2.append(x)
print("Jen v seznamu 2 jsou: ", v_seznamu_2)
