# 1. Students fayldagi ismlarni sanash
from collections import Counter
# Faylni o'qish
with open("Students.txt", "r", encoding="utf-8") as f:
    data = f.read().split()
chastota = Counter(data)
# Natijani chiqarish
for soz,soni in chastota.items():
    print(f"'{soz}': {soni} marta")

# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    return sum(int(i) for i in str(k))
print(digit_sum(502))

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def daraja(n):
    i = 0
    while 2**i <= n:
        print(2**i)
        i += 1
daraja(32)


  
