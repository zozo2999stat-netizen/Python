# 1. Stringni pastki chiziq bilan o'zgartirish
# txt qatori berilgan bo'lsa, har uchinchi belgidan keyin pastki chiziq (_) qo'ying. Agar belgi unli bo'lsa 
# yoki undan keyin pastki chiziq bo'lsa, pastki chiziqni keyingi belgiga o'tkazing. Oxirida pastki chiziq qo'yilmasligi kerak.

# Misollar
# Kirish: hello Chiqish: h_lo

# Kirish: assalom Chiqish: ass_alom

# Kirish: abcabcabcdeabcdefabcdefg Chiqish: abc_abc_abcd_abcd_abcdef
unlilar = ['a','i','u','o','e','A','I','U','O','E']
ls = list(input("Biror so'z kiriting:"))
index = 0
yangi_ls = []
for i in ls:
    index += 1
    if i not in unlilar and i != '_':
        if index % 3 != 0:
            yangi_ls.append(i)
        else:
            yangi_ls.append(i)
            if index != len(ls):
                yangi_ls.append('_')
    else:
        yangi_ls.append(i)
print(''.join(yangi_ls),end='')

# 2. Butun kvadratlar mashqi
# Vazifa
# Taqdim etilgan kod stubkasi STDIN dan butun sonni, n ni o'qiydi. 0 <= i < n bo'lgan barcha manfiy bo'lmagan butun sonlar uchun i^2 ni chop eting.

# Misol kiritish 5
# Chiqish misoli 0 1 4 9 16
# Kirish formati
# Birinchi va yagona qator butun sonni o'z ichiga oladi, n.
# Cheklovlar 1 <= n <= 20
# Chiqish formati Har bir i^2 ga mos keladigan n qatorni chop eting, bunda 0 <= i < n.

n = int(input("n ni kiriting:"))
if 1 <= n <= 20:
    for i in range(n):
        print(i*i)
else:
    print("Iltimos 1 dan 20 gacha bo'lgan son kiriting!!!")

# 1-mashq: Birinchi 10 natural sonni while siklidan foydalanib chop eting
a = 0
while a < 10:
    a += 1
    print(a)

# 2-mashq: Quyidagi naqshni chop eting
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
a = int(input("a ga qiymat bering:"))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 3-mashq: 1 dan berilgan songacha bo‘lgan barcha sonlar yig‘indisini hisoblang
# Misol:
# 10 raqamini kiriting
# Yig'indi: 55

a = int(input("a ga qiymat bering:"))
yigindi = 0

for i in range(1,a+1):
    yigindi += i
print(yigindi)

# 4-mashq: Berilgan sonni ko‘paytirish jadvalini chop etish

a = int(input("a ni kiriting!"))
for num in range(1, 11):
    print(a * num)

# 5-mashq: Ro‘yxatdagi raqamlarni tsikl yordamida ko‘rsatish
numbers = [1, 2, 3, 4, 5, 10, 12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    print(i)

# 6-mashq: sondagi raqamlarning umumiy sonini hisoblang
son = list(input("Butun son kiriting:"))

for i in son:
    print(i)

# 7-mashq: teskari raqamlar naqshini chop etish

a = int(input("Son kiriting: "))

for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

# 8-mashq: Loop yordamida ro'yxatni teskari tartibda chop eting

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1,0,-1):
    print(list1[i], end="\n")
print(list1[0])

# 9-mashq: for tsikli yordamida -10 dan -1 gacha raqamlarni ko'rsatish

for i in range(-10,0,1):
    print(i, end='\n')

# Mashq 10: Muvaffaqiyatli tsikl bajarilgandan so'ng "Bajarildi" xabarini ko'rsatish
for i in range(10):
    pass
print('Bajarildi')

# 11-mashq: diapazondagi barcha tub sonlarni chop eting
a = int(input('a ni kiriting: '))
b = int(input('b ni kiriting: '))
for i in range(a,b+1):
    s = 0
    for j in range(1,i+1):
        if i%j==0:
            s += 1
    if s <= 2:
        print(i)
