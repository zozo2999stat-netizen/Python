# 1. def is_leap(year): """ Berilgan yil kabisa yili ekanligini aniqlaydi.
yil = int(input("Yilni kiriting:"))

if yil%4 == 0:
    if yil%100 == 0:
        if yil%400 == 0:
            print("Kabisa yili!")
        else:
            print("Kabisa yili emas!")
    else:
        print("Kabisa yili!")
else:
    print("Kabisa yili emas!")

# 2. Shartli gaplar mashqi
# Butun son berilgan n, quyidagi shartli amallarni bajaring:
# Agar n g'alati bo'lsa, Weird deb chop eting
# Agar n juft boʻlsa va 2 dan 5 gacha boʻlgan oraliqda boʻlsa, Not Weird deb chop eting
# Agar n juft boʻlsa va 6 dan 20 gacha boʻlgan oraliqda boʻlsa, Weird deb chop eting
# Agar n juft va 20 dan katta boʻlsa, Not Weird deb chop eting

n = int(input('n ga qiymat kiriting:'))

if 1 <= n <= 100: # Cheklovlar
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("G'alati emas")
        elif 6 <= n <= 20:
            print("G'alati")
        elif n > 20:
            print("G'alati emas")
    else:
        print("G'alati")
else:
    print("Iltimos 1 dan 100 gacha bo'lgan son kiriting!!!")

# A va b ikkita butun son berilgan. Bu raqamlar orasidagi juft sonlarni toping. a va b o'z ichiga oladi. Loop ishlatmang.
# Ikkita yechim bering.

# 1-yechim if-else ifodasi bilan.
a = int(input("a ni kiriting:"))
b = int(input("b ni kiriting:"))
if a < b:
    if a % 2 != 0:
        a = a + 1
        print(*range(a, b + 1, 2))
else:
    print("a < b bo'lishi kerak!!!")

# 2-yechim if-else ifodasisiz.
a = int(input("a ni kiriting:"))
b = int(input("b ni kiriting:"))
print(*range(a + a % 2, b + 1, 2))


