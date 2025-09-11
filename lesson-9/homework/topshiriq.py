# 1. Doira sinfi. Doirani ifodalovchi sinf yaratish uchun Python dasturini yozing. Uning maydoni va perimetrini hisoblash usullarini kiriting.
import math

class Doira:
    def __init__(self,radius):
        self.radius = radius
    def yuza(self):
        return math.pi * math.pow(self.radius,2)
    def uzunlik(self):
        return math.pi * self.radius * 2
    
a = Doira(9)
s = a.yuza()
c = a.uzunlik()

print(f"Doiraning yuzi: {s} ga, uzunligi {c} ga teng")

# 2. Person sinfini yaratish uchun Python dasturini yozing. Ism, mamlakat va tug'ilgan sana kabi atributlarni qo'shing. Shaxsning yoshini aniqlash usulini qo'llang.
from datetime import datetime 

class Person:

    def __init__(self, ism, mamlakat, tugilgan_kun):
        self.ism = ism
        self.mamlakat = mamlakat
        self.tugilgan_kun = datetime.strptime(tugilgan_kun, "%d.%m.%Y")  # string → datetime

    def yosh(self):
        bugun = datetime.now()
        yosh = bugun.year - self.tugilgan_kun.year
        if (bugun.month, bugun.day) < (self.tugilgan_kun.month, self.tugilgan_kun.day):
            yosh -= 1
        return yosh
    
a = Person("Akmal", "UZB", "01.10.1990")
yoshi = a.yosh()

print(f"{a.ism}ning yoshi: {yoshi} yosh")

# 3. Kalkulyator sinfi. Kalkulyator sinfini yaratish uchun Python dasturini yozing. Asosiy arifmetik amallar uchun usullarni kiriting.
class Kalkulyator:
    def __init__(self, qoshish, ayirish, kopaytirish, bolish):
        self.qoshish = qoshish
        self.ayirish = ayirish
        self.kopaytirish = kopaytirish
        self.bolish = bolish
    def amal():
        
a = Kalkulyator('+', '-', '*', '/')
natija = a.amal()
print(a)

# 4. Shakl va kichik sinflar
# Shaklni ifodalovchi sinf yaratish uchun Python dasturini yozing. Uning maydoni va perimetrini hisoblash usullarini kiriting. 
# Doira, uchburchak va kvadrat kabi turli xil shakllar uchun kichik sinflarni amalga oshiring.
import math
class Doira:
    def __init__(self, radius, a, b):
        self.radius = radius
        self.a = a
        self.b = b
    def doira(self):
        uzunlik = 2 * math.pi * self.radius
        yuza = math.pi * math.pow(self.radius,2)
        return f"Doira uzunligi = {uzunlik} \nDoira yuzasi = {yuza}"
    def uchburchak(self):
        perimetr = 3 * self.a
        yuza = math.pow(self.a,2) * math.sqrt(3) / 4
        return f"\nUchburchak perimetr = {perimetr} \nUchburchak yuzasi = {yuza}"
    def kvadrat(self):
        perimetr = 4 * self.b
        yuza = math.pow(self.b,2)
        return f"\nKvadrat perimetr = {perimetr} \nKvadrat yuzasi = {yuza}"
    
a = Doira(16,4,5)
doira = a.doira()
uchburchak = a.uchburchak()
kvadrat = a.kvadrat()
print(doira, uchburchak, kvadrat

  +++++++++++++++++++++++++++++++++++++++++++++++++++++    
import math

# Umumiy Shakl sinfi
class Shakl:
    def yuza(self):
        raise NotImplementedError("Yuza hisoblash hali aniqlanmagan")
    
    def perimetr(self):
        raise NotImplementedError("Perimetr hisoblash hali aniqlanmagan")

# Doira sinfi
class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return math.pi * self.radius ** 2
    
    def perimetr(self):
        return 2 * math.pi * self.radius

# Uchburchak sinfi (teng tomonli deb olamiz)
class Uchburchak(Shakl):
    def __init__(self, a):
        self.a = a

    def yuza(self):
        return (math.sqrt(3) / 4) * self.a ** 2
    
    def perimetr(self):
        return 3 * self.a

# Kvadrat sinfi
class Kvadrat(Shakl):
    def __init__(self, a):
        self.a = a

    def yuza(self):
        return self.a ** 2
    
    def perimetr(self):
        return 4 * self.a


# Natijalarni formatlash uchun funksiya
def natijani_chiqar(shakl, nomi):
    print(f"{nomi}:")
    print(f"  Yuza = {shakl.yuza():.1f}")
    print(f"  Perimetr = {shakl.perimetr():.1f}\n")


# Sinov
shakl1 = Doira(10)
shakl2 = Uchburchak(6)
shakl3 = Kvadrat(5)

natijani_chiqar(shakl1, "Doira")
natijani_chiqar(shakl2, "Uchburchak")
natijani_chiqar(shakl3, "Kvadrat")

      
