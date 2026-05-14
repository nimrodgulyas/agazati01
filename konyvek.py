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

legtobb = 0
legtobb_oldalu_konyv = None
for konyvek in konyv:
    if konyvek.oldalszam > legtobb:
        legtobb = konyvek.oldalszam
        legtobb_oldalu_konyv = konyvek.cim
print(f"A legtöbb oldalas könyv: {legtobb_oldalu_konyv}")

keres = str(input("3.4 feladat: Írjon be egy szerzőnevet: "))
van = False
konyvei = []
neve = []
for konyvek in konyv:
    if konyvek.nev == keres:
        konyvei.append(konyvek.cim)
        neve.append(konyvek.nev)
        van = True
if van == True:
    print(f"{neve} könyvei: \n {konyvei}")

if van == False:
    print("Nem található a szerző!")