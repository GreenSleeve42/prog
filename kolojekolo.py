import random as r

import time as t

cislo = r.randint(1, 1000000)

mojecislo = int(input('zadej cislo: '))

pok = 0

mocpoc = 0

malopoc = 0

cas = t.monotonic()

print(f"{type(mocpoc)}")

cask = 0

while mojecislo != cislo:
    if mojecislo < cislo:
        print("malo")
        malopoc = malopoc + 1
    elif mojecislo > cislo:
        print("moc")
        mocpoc += 1
    
    pok = pok + 1

    mojecislo = int(input('zadej cislo znova: '))

cask = t.monotonic()

print(f"no huraaa, cislo je opravdu {cislo}")
print(f"tvuj pocet pokusu je {pok}. tvuj pocet moc velkych odhadu byl {mocpoc} a tvuj pocet moc malych obhadu byl {pok - mocpoc}.")
print(f'tvuj cas byl {cask - cas:4.3f} sekund')