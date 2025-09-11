# 1. O'zingizning virtual muhitingizni yarating va ba'zi python paketlarini o'rnating.

Python-da virtual muhit yaratish uchun eng ko‘p ishlatiladigan vosita bu venv modulidir.
python -m venv myenv
myenv\Scripts\activate
source myenv/bin/activate

pip 
install
requests
numpy

math_operations.py fayl tarkibi:
def add(a, b):
    """Ikki sonni qo‘shish"""
    return a + b

def subtract(a, b):
    """Ikki sondan ikkinchisini ayirish"""
    return a - b

def multiply(a, b):
    """Ikki sonni ko‘paytirish"""
    return a * b

def divide(a, b):
    """Ikki sonni bo‘lish (bo‘luvchi nol bo‘lmasligi kerak)"""
    if b == 0:
        return "Error: Bo‘luvchi nol bo‘lishi mumkin emas!"
    return a / b


# 2.string_utils.py fayli:
def to_uppercase(s):
    """Matnni katta harflarga aylantiradi"""
    return s.upper()

def to_lowercase(s):
    """Matnni kichik harflarga aylantiradi"""
    return s.lower()

def reverse_string(s):
    """Matnni teskari qilib qaytaradi"""
    return s[::-1]

def count_vowels(s):
    """Matndagi unli harflar sonini hisoblaydi"""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# 3. Geometriya paketini yaratish:
geometry/         
__init__.py   
    rectangle.py
    circle.py    
