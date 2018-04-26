zvirata_1 = ["pes", "kočka", "králík", "had", "andulka"]

def porovnej(zvirata_1):
    return zvirata_1[1]

zvirata_1.sort(key=porovnej)

print("Seznam zvířat podle druhého písmena:", zvirata_1)
