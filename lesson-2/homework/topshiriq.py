# 1.
txt = 'MsaatmiazD'
print(txt[::2], "va", txt[9:0:-2])
# 2.
txt = "I'm John. I am from London"
print(txt[9:])
# 3.
txt = input("Iltimos matn kiriting: ")
print(txt[::-1])
# 4.
soz = input("Iltimos so'z kiriting: ")
if soz.lower() == soz.lower()[::-1]:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")
# 5.
royxat = ["Olma", "O'rik", "Shaftoli", "Nok", "Behi"]
print(royxat[2])
# 6.
ls1 = [1, 3, 5, 7, 9]
ls2 = [2, 4, 6, 8, 10]
ls1.extend(ls2)
ls1

# 7. 
ls = [1, "salom", 2, "dunyo", 3, "!", 4]
ortasi = len(ls) // 2
oxirgi = len(ls) - 1
print("Birinchi element: ", ls[0], "O'rtadagi element: ", ls[ortasi], "Oxirgi element: ", ls[oxirgi])

# 8.
shaharlar = ["Toshkent", "London", "New York", "parij"]
shahar = "Parij"
for i in shaharlar:
    if i.lower() == shahar.lower():
        print("Ro'yxatda Parij bor.")
        break
else:
    print("Ro'yxatda Parij yo'q.")

# 9.
ls = [1, 2, 3, 4, 5, 6]
ls.extend(ls)
ls

# 10.
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls[0], ls[-1] = ls[-1], ls[0]
print(ls)

