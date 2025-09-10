## 1 Roʻyxat elementlarini yaratish va ularga kirish (Besh xil mevadan iborat roʻyxatni yarating va uchinchi mevani chop eting.)
ls = ["Olma", "Nok", "Banan", "Behi", "Uzum"]
print(ls[3])

## 2. Ikki roʻyxatni birlashtirish (Ikki raqamlar roʻyxatini yarating va ularni bitta roʻyxatga birlashtiring.)
ls1 = [1, 2, 3, 4]
ls2 = [6, 5, 4, 3]
ls1.extend(ls2)
ls1

## 3. Roʻyxatdagi elementlarni ajratib oling (Raqamlar roʻyxatini hisobga olgan holda, birinchi, oʻrta va oxirgi elementlarni ajratib oling va ularni yangi roʻyxatda saqlang.)
ls = ["Salom", 3, "men", 88, "dasturchiman"]
ls2 = [ls[0], ls[len(ls)//2], ls[len(ls)-1]]
ls2

## 4. Roʻyxatni toʻplamga oʻzgartiring (Beshta sevimli filmingiz roʻyxatini yarating va uni toʻplamga aylantiring.)
# Ro'yxat yaratish
films = ["Spider Man", "The Great battle", "The Dark Knight", "Gladiator", "Avatar", "Avatar"]

# Tuplega aylantirish
films_tuple = tuple(films)

print(films_tuple)

## 5. Ro'yxatdagi elementni tekshiring (Shaharlar ro'yxatini hisobga olgan holda, ro'yxatda "Parij" mavjudligini tekshiring va natijani chop eting.)
ls_city = ["Toshkent", "Ostona","Anqara", "parij", "Tokio"]
for i in ls_city:
    if i.lower() == "parij":
        print("Ro'yxatda Parij bor")
        break
else:
    print("Bu ro'yxatda Parij yo'q")

## 6. Looplardan foydalanmasdan ro'yxatni ko'paytirish (Raqamlar ro'yxatini tuzing va uni ko'chadan foydalanmasdan takrorlang.)
ls = [2, 3, 5, 6, 8, 9, 10]

# Ro'yxatni 3 marta takrorlash
new_ls = ls[0] * 2

print(new_ls)

## 7. Ro'yxatning birinchi va oxirgi elementlarini almashtirish (raqamlar ro'yxatini hisobga olgan holda, birinchi va oxirgi elementlarni almashtiring.)
ls = [2, 3, 5, 6, 8, 9, 10, 88, 99]
ls[len(ls)-1],ls[0] = ls[0],ls[len(ls)-1]
print(ls)

## 8. Tupleni kesib oling (1 dan 10 gacha raqamlar to'plamini yarating va 3 dan 7 gacha bo'lgan bo'lakni chop eting.)
sonlar = (1, 3, 5, 8, 9, 10, 2, 4, 7, 6)

# 3-chi indeksdan 7-chi indeksgacha
bolak = sonlar[2:7]
# 3 dan 7 gacha
yangi_sonlar = tuple(i for i in sonlar if 3 <= i <= 7)
saralangan = tuple(sorted(yangi_sonlar))
print("Turplening 3-elementdan 7-elementgacha bo'lgan qismi:", bolak)
print("Turpledagi 3 dan 7 gacha bo'lgan sonlar:", saralangan)

## 9. Ro‘yxatdagi hodisalarni sanash (Ranglar ro'yxatini tuzing va ro'yxatda "ko'k" necha marta paydo bo'lishini hisoblang.)
ranglar = ["oq", "qizil", "sariq", "ko'k", "moviy", "ko'k"]
soni = ranglar.count("ko'k")
print("Ro'yxatdagi ko'k ranglar soni:", soni, "ta")

## 10. Tupledagi element indeksini toping (hayvonlar toʻplami berilgan boʻlsa, “sher” indeksini toping.)
royxat = ("Maymun", "Sher", "Jirafa", "Yo'lbars", "Sirtlon", "Qoplon")
indeks = royxat.index("Sher")
print(indeks)

## 11. Ikki kortejni birlashtiring (Ikkita sonlar korteji yarating va ularni bitta kortejga birlashtiring.)
ls = [2, 3, 5, 4, 6, 10]
ls2 = [4, 5, 3, 11, 12]
# ls.append(ls2)
ls.extend(ls2)
ls

## 12. Ro‘yxat va to‘plam uzunligini toping (Roʻyxat va kortej berilgan boʻlsa, ularning uzunligini toping va chop eting.)
ls = [2, 3, 5, 4, 6, 10, 4, 5, 3, 11, 12, "Yo'lbars", "Sirtlon", "Qoplon"]
kartej = (2, 3, 5, 4, 6, 10, 4, "Maymun", "Sher", "Jirafa",)
ls_uzunligi = len(ls)
kartej_uzunligi = len(kartej)
print("Ro'yxat uzunligi:", ls_uzunligi, "\nKartej uzunligi:", kartej_uzunligi)

## 13. Tupleni ro'yxatga aylantirish (Beshta raqamdan iborat kortej yarating va uni ro'yxatga aylantiring.)
kartej = (4, 5, 3, 11, 12)
royxat  = list(kartej)
print(royxat)

## 14. Tupledagi maksimal va minimal qiymatlarni toping (Raqamlar majmuasi berilgan, maksimal va minimal qiymatlarni toping va chop eting.)
kartej = (2, 3, 5, 8, 10, 12, 22, 32, 44)
print("min:", min(kartej), "\nmax:", max(kartej))

## 15. Tupleni teskari o'zgartirish (So'zlar to'plamini yarating va uni teskari tartibda chop eting.)
kartej = ("Sardor", "Temur", "Bilol")
teskari = tuple(reversed(kartej))
print(teskari)
