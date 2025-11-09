import pygame as p
import time as t
import random as r

barvp = (36, 200, 42)

polohax = 500

polohay = 100

rychlostx = 10

polomer = 30

rychlosty =  r.randint(3, 10)
zrychlenix = 0 #r.randint(1, 5) 

zrychleniy = r.randint(1, 5)

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

    if polohay >= 0:
        polohay = polohay + rychlosty
    else:
        polohay = 0
        rychlosty = -rychlosty 

    if polohay > vyska - polomer:
        polohay = vyska - polomer
        rychlosty = -rychlosty
        rn = (r.random() - 0.5) * rychlosty   
        rychlostx = rn 
        print(rn)

    if polohax >= polomer:
        polohax = polohax + rychlostx
    else:
        polohax = polomer
        rychlostx = -rychlostx  

    if polohax > sirka - polomer:
        polohax = sirka - polomer
        rychlostx = -rychlostx

    rychlosty = rychlosty + zrychleniy
    rychlostx = rychlostx + zrychlenix

    if rychlostx >= 10:
        p.draw.circle

    cask = t.monotonic()
    t.sleep(max(0., dobasnimku - (cask - cas)))
    cask = t.monotonic()

    #print((cask - cas) * 1000)