# 1. Vazifa sinfini aniqlang: Vazifa nomi, tavsifi, tugash sanasi va holati kabi atributlarga ega Vazifa sinfini yarating.
import datetime
class Vazifa:
    def __init__(self, nomi, tavsifi, tugashi, holati):
        self.nomi = nomi
        self.tavsifi = tavsifi
        self.tugashi = tugashi
        self.holati = holati
    def malumot(self):
        return f"10-{self.nomi}: {self.tavsifi};\nmuddati: {self.tugashi};\nholati: {self.holati}."
sinf = Vazifa("homework", "Vazifa sinfini aniqlash", "29.08.2025", "bajarilmoqda")
print(sinf.malumot())

# 2. ToDoList sinfini aniqlang:
# Vazifalar ro'yxatini boshqaradigan ToDoList sinfini yarating.
# Vazifa qo'shish, vazifani tugallangan deb belgilash, barcha vazifalarni sanab o'tish va tugallanmagan vazifalarni ko'rsatish usullarini qo'shing.
from datetime import date, time, datetime, timedelta, timezone

class ToDoList:
    def __init__(self):
        self.vazifalar = []
    def vazifa_qosh(self, nomi):
        self.nomi = nomi
        self.vazifalar.append(self.nomi)
        return f"'{self.nomi}' '{self.tugashi}' vazifalar ro'yxatiga qo'shildi ✅"
    def muddat(self, tugashi):
        # string → datetime
        tugash_sana = datetime.strptime(tugashi, "%d.%m.%Y").date()
        bugun = datetime.today().date()
        if bugun > tugash_sana:
            return f"❌ {self.nomi} vazifa muddati o'tib ketgan! (tugashi: {tugashi})"
        elif bugun == tugash_sana:
            return f"⚠️ Bugun {self.nomi} vazifasining oxirgi kuni!"
        else:
            qoldi = (tugash_sana - bugun).days
            return f"✅ {self.nomi} vazifasiga {qoldi} kun qoldi. (muddat: {tugashi})"
    def barcha_vazifalar(self):
        return f"Barcha vazifalar ro'yxati: {self.vazifalar}"
    
sinf = ToDoList()
print(sinf.vazifa_qosh("Kitob o'qish"))
print(sinf.vazifa_qosh("Python amaliyot"))
print(sinf.vazifa_qosh("STATA amaliyot"))
print(sinf.vazifalar, sinf.muddat("28.08.2025"))

# 3. Asosiy dastur yaratish:
# ToDoList bilan ishlash uchun oddiy CLI-ni ishlab chiqing.
# Vazifalarni qo'shish, vazifalarni tugallangan deb belgilash, barcha vazifalarni sanab o'tish va 
# faqat to'liq bo'lmagan vazifalarni ko'rsatish variantlarini qo'shing.
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.vazifalar = []   # barcha vazifalar list ichida saqlanadi

    def vazifa_qosh(self, nomi, tugashi):
        vazifa = {
            "nomi": nomi,
            "tugashi": tugashi,
            "tugallangan": False
        }
        self.vazifalar.append(vazifa)
        return f"'{nomi}' ({tugashi}) vazifalar ro'yxatiga qo'shildi ✅"

    def vazifa_tugallandi(self, nomi):
        for vazifa in self.vazifalar:
            if vazifa["nomi"] == nomi:
                vazifa["tugallangan"] = True
                return f"'{nomi}' vazifasi tugallandi ✅"
        return f"'{nomi}' vazifasi topilmadi ❌"

    def barcha_vazifalar(self):
        if not self.vazifalar:
            return "📂 Vazifalar yo'q"
        matn = "📋 Barcha vazifalar:\n"
        for v in self.vazifalar:
            holat = "✅ Tugallangan" if v["tugallangan"] else "⏳ Kutilmoqda"
            matn += f"- {v['nomi']} (muddat: {v['tugashi']}) → {holat}\n"
        return matn
    def tugallanmagan_vazifalar(self):
        tugallanmagan = [v for v in self.vazifalar if not v["tugallangan"]]
        if not tugallanmagan:
            return "🎉 Barcha vazifalar tugallangan!"
        matn = "⏳ Tugallanmagan vazifalar:\n"
        for v in tugallanmagan:
            matn += f"- {v['nomi']} (muddat: {v['tugashi']})\n"
        return matn
    def muddat_tekshir(self, nomi):
        for v in self.vazifalar:
            if v["nomi"] == nomi:
                tugash_sana = datetime.strptime(v["tugashi"], "%d.%m.%Y").date()
                bugun = datetime.today().date()
                if bugun > tugash_sana:
                    return f"❌ '{nomi}' vazifa muddati o'tib ketgan! ({v['tugashi']})"
                elif bugun == tugash_sana:
                    return f"⚠️ Bugun '{nomi}' vazifasining oxirgi kuni!"
                else:
                    qoldi = (tugash_sana - bugun).days
                    return f"✅ '{nomi}' vazifasiga {qoldi} kun qoldi. (muddat: {v['tugashi']})"
        return f"'{nomi}' vazifasi topilmadi ❌"

# Test
sinf = ToDoList()
sinf.vazifa_qosh("Kitob o'qish", "26.08.2025")
sinf.vazifa_qosh("Python amaliyot", "01.09.2025")
sinf.vazifa_qosh("STATA amaliyot", "02.09.2025")

print()
sinf.barcha_vazifalar()

print()
sinf.muddat_tekshir("Kitob o'qish")

print()
print(sinf.tugallanmagan_vazifalar())

# 4. Post sinfini aniqlang:
# Sarlavha, tarkib va ​​muallif kabi atributlarga ega Post sinfini yarating.

class Post:
    def __init__(self):
        self.postlar = []
    def post_qoshish(self, sarlavha, tarkib, muallif):
        post = {
            "sarlavha": sarlavha,
            "tarkib": tarkib,
            "muallif": muallif
        }
        self.postlar.append(post)
        return f"'{muallif}' ({sarlavha}) postlar ro'yxatiga qo'shildi ✅"
  sinf = Post()
sinf.post_qoshish("Tabrik", "Muvoffaqiyat bilan tabriklayman", "Kamolbek Jumanazarov")
sinf.post_qoshish("E'tiroz", "Bundanam yaxshi bo'lishi mumkin edi", "Akmal Davletov")
print(sinf.postlar)

class Post:
    def __init__(self, sarlavha, tarkib, muallif):
        self.sarlavha = sarlavha
        self.tarkib = tarkib
        self.muallif = muallif
    def __str__(self):
        return f"{self.sarlavha} | {self.muallif}\n{self.tarkib}"


# Post obyektlari yaratamiz
post1 = Post("Tabrik", "Muvoffaqiyat bilan tabriklayman", "Kamolbek Jumanazarov")
post2 = Post("E'tiroz", "Bundanam yaxshi bo'lishi mumkin edi", "Akmal Davletov")

# Konsolga chiqaramiz
print(post1)
print()
print(post2)

# 5. Bank sinfini aniqlang:
# Hisoblar ro'yxatini boshqaradigan Bank sinfini yarating.
# Hisob qo'shish, balansni tekshirish, pul o'tkazish va pul yechib olish usullarini qo'shing.

class Bank:
    def __init__(self):
        self.hisoblar = []
    def hisob_qoshish(self, hisob_nomi, balans):
        hisob = {
            "hisob_nomi": hisob_nomi,
            "balans": balans
            }
        self.hisoblar.append(hisob)
        return f"{hisob} bank hisoblariga qo'shildi"
    def pul_otkazish(self, hisob, otkazma):
        if self.balans >= otkazma:
            return f"{hisob}-hisobingizdan {otkazma} $ o'tkazama muvaffaqtiyatli amalga oshirildi"
        else:
            return f"Hisobingizda mablag' yetarli emas"
    def pel_yechish(self, hisob, balans, yechish):
        if balans >= yechish:
            return f"Siz {hisob}-hisobingizdan {yechish} $ yechib oldingiz.\nHisobingizdagi qoldiq: {balans - yechish} $"
        else:
            return f"Hisobingizda mablag' yetarli emas"
            def balans_tekshirish(self, hisob, balans):
        return f"{hisob} hisob raqamingizdagi qoldiq: {balans} $"    
sinf = Bank()
print(sinf.hisob_qoshish("hisob1", 10000))
print(sinf.hisob_qoshish("hisob2", 11000))
print(sinf.pul_otkazish("hisob1"))
print(sinf.balans_tekshirish("hisob1"))

# 6. Blog sinfini aniqlang:
# Xabarlar ro'yxatini boshqaradigan Blog sinfini yarating.
# Xabar qo'shish, barcha xabarlarni sanab o'tish va ma'lum bir muallifning xabarlarini ko'rsatish usullarini qo'shing

class Blog:
    def __init__(self):
        self.xabarlar = []   # barcha xabarlar list ichida saqlanadi
    def xabar_qosh(self, muallif, matni):
        xabar = {
            "muallif": muallif,
            "matni": matni,
        }
        self.xabarlar.append(xabar)
        return f"'{muallif}' ({matni}) xabarlar ro'yxatiga qo'shildi ✅"
   def barcha_xabarlar(self):
        return f"{self.xabarlar}"

# Test
sinf = Blog()
sinf.xabar_qosh("K.Jumanazarov", "Xabarlar ro'yxatini boshqaradigan Blog sinfini yarating")
sinf.xabar_qosh("P.Bahodirov", "Xabar qo'shish, barcha xabarlarni sanab o'tish")
# print()
sinf.barcha_xabarlar()

# 7. Bank tizimini takomillashtirish:
# Hisoblar o'rtasida pul o'tkazish, hisob ma'lumotlarini ko'rsatish va hisob overdraftlarini boshqarish funksiyalarini qo'shing.
class Bank:
    def __init__(self):
        self.hisoblar = {}
    def hisob_qoshish(self, hisob_raqami, egasi, balans):
        self.hisoblar[hisob_raqami] = balans
        return f"Egasi: {egasi};\nh/r: {hisob_raqami};\nbalans: {balans} $ bank hisobi ochildi ✅"
    def hisob_malumotlari(self):
        if self.egasi in self.hisoblar:
            return f"{self.egasi}, {self.hisob_raqami} hisobidagi qoldiq: {self.hisoblar[self.hisob_raqami]} $"
        else:
            return "Bunday hisob mavjud emas ❌"
    def pul_otkazish(self, kimdan, kimga, miqdor):
        if kimdan not in self.hisoblar or kimga not in self.hisoblar:
            return "Hisob topilmadi ❌"
        if self.hisoblar[kimdan] >= miqdor:
            self.hisoblar[kimdan] -= miqdor
            self.hisoblar[kimga] += miqdor
            return f"{miqdor} $ {kimdan} hisobidan {kimga} hisobiga o'tkazildi ✅"
        else:
            return "Hisobda mablag' yetarli emas ❌"
# Sinov
bank = Bank()
print(bank.hisob_qoshish(1232156456, "Kamolbek Jumanazarov", 10000))
print(bank.hisob_qoshish(8465465413, "Akmal Burxonov", 11000))
# print(bank.hisob_malumotlari("Kamolbek Jumanazarov"))
print(bank.pul_otkazish("hisob1", "hisob2", 3000))
print(bank.hisob_malumotlari("hisob1"))
print(bank.hisob_malumotlari("hisob2"))

