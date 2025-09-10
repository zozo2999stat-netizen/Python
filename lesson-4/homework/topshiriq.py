# 1. Lug‘atni qiymat bo‘yicha tartiblang (Lug'atni qiymat bo'yicha saralash (o'sish va pasayish) uchun Python skriptini yozing.)
oquvchi = {"Aziz": 15, "Akmal": 18, "Botir": 21, "Sardor": 16}
tartiblangan = dict(sorted(oquvchi.items(), key = lambda x: x[1]))
print(tartiblangan)

# 2. Lug'atga kalit qo'shing (Lug'atga kalit qo'shish uchun Python skriptini yozing.)
# Lug'at namunasi: {0: 10, 1: 20}
# Kutilayotgan natija: {0: 10, 1: 20, 2: 30}
lugat = {0: 10, 1: 20}
lugat[2] = 30
lugat

# 3. Bir nechta lug‘atlarni birlashtiring
# Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun Python skriptini yozing.

# Namuna lug'atlar:
dic1 = {1: 10, 2: 20}
dic2 = {3:30, 4:40}
dic3 = {5: 50, 6: 60}

# Lug'atlarni birlashitirish:
dic4 = dic1 | dic2 | dic3
dic4

# 4. Kvadratchalar bilan lug‘at yarating
# (x, x*x) ko'rinishida raqamni (1 va n oralig'ida) o'z ichiga olgan lug'at yaratish va chop etish uchun Python skriptini yozing.
# Lug‘at namunasi (n = 5):
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("n ga qiymat kiriting:"))
for i in range(1, n+1):  # 1-dan n-gacha
    lugat[i] = i*i
print(lugat)

# 5. Kvadratchalar lug'ati (1 dan 15 gacha)
# Lug'atni chop etish uchun Python skriptini yozing, bu erda kalitlar 1 dan 15 gacha bo'lgan raqamlar (ikkalasi ham kiritilgan) va qiymatlar kalitlarning kvadratidir.
# Kutilayotgan natija:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
n = int(input("n ga qiymat kiriting:"))
m = int(input("m ga qiymat kiriting:"))
for i in range(n, m+1):  # 1-dan n-gacha
    lugat[i] = i*i
print(lugat)

# 6. To'plam yarating
# To'plam yaratish uchun Python dasturini yozing.
a = "Olma"
b = "Uzum"
c = "Nok"
mevalar = {a, b, c}
print(mevalar)

# 7. To‘plam ustida takrorlash
# To'plamlarni takrorlash uchun Python dasturini yozing.
mevalar = {'Uzum', 'Olma', 'Nok'}
mevalar2 = list(mevalar) * 2
print(mevalar2)

# 8. To'plamga a'zo(lar)ni qo'shing
# To'plamga a'zo(lar)ni qo'shish uchun Python dasturini yozing.
toplam = {"Olma"}
toplam.add("Nok")
toplam.add("Uzum")
toplam.add("Behi")
toplam

# 9. To'plamdan element(lar)ni olib tashlang
# Berilgan toʻplamdan element(lar)ni olib tashlash uchun Python dasturini yozing.
toplam = {'Behi', 'Nok', 'Olma', 'Uzum'}
toplam.remove("Nok")
print(toplam)

# 10. To'plamda mavjud bo'lsa, elementni olib tashlang
# Agar to'plamda mavjud bo'lsa, to'plamdan elementni olib tashlash uchun Python dasturini yozing.
toplam = {'Behi', 'Nok', 'Olma', 'Uzum'}
a = input("Meva nomini kiriting:")
if a in toplam:
    toplam.remove(a)
    print(a, "o'chirildi qolgan mevalar:", toplam)
else:
    print("To'plamda bu meva yo'q")
