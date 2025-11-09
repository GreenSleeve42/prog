import pygame as p
import time as t
import random as r

barvp = (36, 200, 42)

polohax = 500

polohay = 700

rychlostx = 0

polomer = 30

rychlosty = -r.randint(10, 100)


cask = 0

dobasnimku = 1./60

sirka = 1000

vyska = 700

obr = p.display.set_mode((sirka, vyska),vsync = 1)
obr.fill(barvp)

cas = 0.

jedunaledu = True
while jedunaledu:

    
    cas = t.monotonic()

    p.display.flip()
    obr.fill(barvp)

    udalosti = p.event.get()

    if udalosti:
        print(udalosti)
        print(rychlostx)
        if udalosti[0].type == p.KEYUP and udalosti[0].dict["key"] == ord("d"):
            jedunaledu = False
    
    p.draw.circle(obr,(3, 67, 124),(polohax, polohay),30)
    if polohax >= 0:

        polohax = polohax + rychlostx
    rychlostx = rychlostx -0
    rychlosty = rychlosty -0.01

    if polohay >= 0:
    
        polohay = polohay + rychlosty
    else:
        polohay = 0
        rychlosty = -rychlosty + 100

    if polohay > vyska:
        polohay = vyska
        rychlosty = -rychlosty -100

    if polohay >= polomer:
        polohay = polohay + rychlosty
    else:
        polohay = polomer
        rychlosty = -rychlosty   

    if polohay > vyska - polomer:
        polohay = vyska - polomer
        rychlosty = - rychlosty






    cask = t.monotonic()
    t.sleep(dobasnimku - (cask - cas))
    cask = t.monotonic()

    print((cask - cas) * 1000)