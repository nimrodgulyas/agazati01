class Konyvek:
    def __init__(self, nev, cim, ev, oldalszam, ekonyv):
        self.nev = nev
        self.cim = cim
        self.ev = int(ev)
        self.oldalszam = int(oldalszam)
        self.ekonyv = int(ekonyv)
        
fajl = open("202__1/konyvek.txt" , "r", encoding="utf-8")

konyv = []
for sor in fajl:
    adatok = sor.strip().split(";")
    hozzaad = Konyvek(
        adatok[0],
        adatok[1],
        adatok[2],
        adatok[3],
        adatok[4]
    )
    konyv.append(hozzaad)
fajl.close

#3.2

print(f"3.2 feladat: Az állományban {len(konyv)} db könyv adatai szerepelnek.")

legtobb = konyv[0]
for konyvek in konyv:
    if konyvek.oldalszam > legtobb.oldalszam:
        legtobb = konyvek
        print(f"3.3. feladat: A legtöbb oldalas könyv: \n Szerző: {legtobb.nev}\n\t Cím: {legtobb.cim}\n\t Kiadás éve: {legtobb.ev}")


keres = str(input("3.4 feladat: Írjon be egy szerzőnevet: "))
van = False
for konyvek in konyv:
    if konyvek.nev == keres:
        van = True
        print(f"{keres} könyvei: \n {konyvek.cim}")
        

if van == False:
    print("Nem található a szerző!")
    
    
osszes = 0
darab = 0
for konyvek in konyv:
    if konyvek.ekonyv == 0:
        osszes += konyvek.oldalszam
        darab += 1
print(f"A nyomtatott kötetek átlagos oldalszáma: {round(osszes / darab, 2)} lap.")