# 1-mashq: Yivli bosh sonlarni tekshirish
# Berilgan sonlar diapazonida tub sonlar mavjudligini tekshiradigan Python dasturini yozing. 
# Asosiy tekshirish jarayonini parallellashtirish uchun diapazonni bir nechta iplar orasida taqsimlang. 
# Har bir mavzu diapazonning pastki to'plamini tekshirish uchun javobgar bo'lishi kerak va asosiy dastur topilgan tub raqamlar ro'yxatini chop etishi kerak.

import threading

# Tub sonni tekshirish funksiyasi
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Thread bajaradigan funksiya
def find_primes_in_range(start: int, end: int, result: list):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

# Asosiy dastur
if __name__ == "__main__":
    start, end = 1, 100   # diapazon
    num_threads = 4       # nechta ip ishlatamiz
    
    # Har bir ip uchun diapazonni bo‘lish
    step = (end - start) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i != num_threads - 1 else end
        t = threading.Thread(target=find_primes_in_range, args=(sub_start, sub_end, results))
        threads.append(t)
        t.start()

    # Barcha iplar tugashini kutish
    for t in threads:
        t.join()

    # Natijani chiqarish
    results.sort()
    print("Tub sonlar:", results)


# 2-mashq: Tishli fayllarni qayta ishlash
# Matn satrlarini o'z ichiga olgan katta matn faylini o'qiydigan dastur yozing. 
# Fayldagi har bir so'zning paydo bo'lishini hisoblash uchun tishli yechimni amalga oshiring. 
# Har bir mavzu faylning bir qismini qayta ishlashi kerak va asosiy dastur barcha mavzular bo'ylab so'zlarning qisqacha mazmunini ko'rsatishi kerak.

import threading
from collections import Counter

# Har bir ip bajaradigan funksiya
def count_words(lines, result_list):
    counter = Counter()
    for line in lines:
        words = line.strip().split()
        counter.update(words)
    result_list.append(counter)

# Asosiy dastur
if __name__ == "__main__":
    filename = "large_text.txt"   # katta matn fayl nomi
    num_threads = 4               # nechta ip ishlatamiz
    
    # Faylni o‘qish
    with open('employee_data.csv', "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Faylni bo‘laklarga bo‘lish
    step = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        sub_lines = lines[i * step : (i + 1) * step] if i != num_threads - 1 else lines[i * step :]
        t = threading.Thread(target=count_words, args=(sub_lines, results))
        threads.append(t)
        t.start()
    
    # Barcha iplar tugashini kutish
    for t in threads:
        t.join()

    # Natijalarni birlashtirish
    final_counter = Counter()
    for c in results:
        final_counter.update(c)

    # Eng ko‘p uchraydigan 10 ta so‘z
    print("Eng ko‘p uchraydigan so‘zlar:")
    for word, count in final_counter.most_common(10):
        print(f"{word}: {count}")

