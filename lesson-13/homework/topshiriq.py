# 1. Yosh kalkulyatori: foydalanuvchidan tug'ilgan sanasini kiritishni so'rang. Ularning yoshini yillar, oylar va kunlarda hisoblang va chop eting.
from datetime import date, datetime, timedelta

# Foydalanuvchidan sana olish
tugilgan_kun_str = input("Tug'ilgan kuningizni (kun.oy.yil, masalan 02.02.2000) kiriting: ")

# String -> datetime
tugilgan_kun = datetime.strptime(tugilgan_kun_str, "%d.%m.%Y").date()

# Bugungi sana
hozir = date.today()

# Farqni hisoblash
yillar = hozir.year - tugilgan_kun.year
oylar = hozir.month - tugilgan_kun.month
kunlar = hozir.day - tugilgan_kun.day

# Agar kun manfiy chiqsa
if kunlar < 0:
    oylar -= 1
    oldingi_oy = (hozir.replace(day=1) - timedelta(days=1)).day
    kunlar += oldingi_oy

# Agar oy manfiy chiqsa
if oylar < 0:
    yillar -= 1
    oylar += 12

print(f"Sizning yoshingiz: {yillar} yil, {oylar} oy, {kunlar} kun.")


# 2. Keyingi tug'ilgan kungacha bo'lgan kunlar: 
# Birinchi mashqga o'xshash, ammo bu safar foydalanuvchining keyingi tug'ilgan kuniga qadar qolgan kunlar sonini hisoblang va chop eting.
from datetime import date, datetime, timedelta

# Foydalanuvchidan sana olish
tugilgan_kun_str = input("Tug'ilgan kuningizni (kun.oy.yil, masalan 02.02.2000) kiriting: ")

# String -> datetime
tugilgan_kun = datetime.strptime(tugilgan_kun_str, "%d.%m.%Y").date()

# Bugungi sana
hozir = date.today()

# Farqni hisoblash
yillar = hozir.year + 1

print(yillar)
