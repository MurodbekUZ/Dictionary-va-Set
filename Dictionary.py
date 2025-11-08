# 1-Masala: Talaba baholari
# student_grades = {"Matematika": 90, "Fizika": 85, "Informatika": 95}
#
# # Boshlang'ich dictionary: student_grades
# student_grades = {"Matematika": 90, "Fizika": 85, "Informatika": 95}
#
# # 1-vazifa: Yangi fan ("Kimyo", 88) qo‘shish
# # Kalit orqali qo‘shish: Dictionaryga yangi kalit-qiymat juftligini qo‘shish uchun kalitni to‘g‘ridan-to‘g‘ri ishlatamiz
# # Nima uchun ishlatildi: Dictionaryga yangi fan va uning bahosini qo‘shish uchun
# student_grades["Kimyo"] = 88
# result1 = student_grades
# print("1-vazifa natijasi:", result1)  # Natija: {'Matematika': 90, 'Fizika': 85, 'Informatika': 95, 'Kimyo': 88}
#
# # 2-vazifa: "Fizika" bahosini 87 ga o‘zgartirish
# # Kalit orqali o‘zgartirish: Mavjud kalitning qiymatini yangi qiymat bilan almashtirish
# # Nima uchun ishlatildi: "Fizika" fanining bahosini yangilash uchun
# student_grades["Fizika"] = 87
# result2 = student_grades
# print("2-vazifa natijasi:", result2)  # Natija: {'Matematika': 90, 'Fizika': 87, 'Informatika': 95, 'Kimyo': 88}
#
# # 3-vazifa: "Informatika" fanini o‘chirish
# # del operatori: Dictionarydan kalit-qiymat juftligini o‘chirish uchun ishlatiladi
# # Nima uchun ishlatildi: "Informatika" fanini dictionarydan olib tashlash uchun
# del student_grades["Informatika"]
# result3 = student_grades
# print("3-vazifa natijasi:", result3)  # Natija: {'Matematika': 90, 'Fizika': 87, 'Kimyo': 88}
#
# # 4-vazifa: Barcha baholar yig‘indisini topish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # sum() funksiyasi: Iterable (masalan, ro‘yxat) elementlarining yig‘indisini hisoblaydi
# # Nima uchun ishlatildi: Barcha baholarni yig‘ish uchun
# result4 = sum(student_grades.values())
# print("4-vazifa natijasi:", result4)  # Natija: 265
#
# # 5-vazifa: Baholar o‘rtachasini hisoblash
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # sum() funksiyasi: Qiymatlar yig‘indisini hisoblash uchun
# # len() funksiyasi: Dictionaryning uzunligini (elementlar sonini) qaytaradi
# # Nima uchun ishlatildi: Baholar o‘rtachasini hisoblash uchun (yig‘indi / elementlar soni)
# result5 = sum(student_grades.values()) / len(student_grades)
# print("5-vazifa natijasi:", result5)  # Natija: 88.333...
#
# # 6-vazifa: Eng yuqori bahoni topish
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # max() funksiyasi: Iterable ichidagi eng katta elementni qaytaradi
# # Nima uchun ishlatildi: Eng yuqori bahoni aniqlash uchun
# result6 = max(student_grades.values())
# print("6-vazifa natijasi:", result6)  # Natija: 90
#
# # 7-vazifa: Eng past bahoni topish
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # min() funksiyasi: Iterable ichidagi eng kichik elementni qaytaradi
# # Nima uchun ishlatildi: Eng past bahoni aniqlash uchun
# result7 = min(student_grades.values())
# print("7-vazifa natijasi:", result7)  # Natija: 87
#
# # 8-vazifa: Fanlar ro‘yxatini chop etish
# # keys() metodi: Dictionaryning faqat kalitlarini ro‘yxat sifatida qaytaradi
# # list() funksiyasi: keys() natijasini ro‘yxatga aylantirish uchun
# # Nima uchun ishlatildi: Faqat fanlar nomini ro‘yxat sifatida olish uchun
# result8 = list(student_grades.keys())
# print("8-vazifa natijasi:", result8)  # Natija: ['Matematika', 'Fizika', 'Kimyo']
#
# # 9-vazifa: Baholar ro‘yxatini chop etish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # list() funksiyasi: values() natijasini ro‘yxatga aylantirish uchun
# # Nima uchun ishlatildi: Faqat baholarni ro‘yxat sifatida olish uchun
# result9 = list(student_grades.values())
# print("9-vazifa natijasi:", result9)  # Natija: [90, 87, 88]
#
# # 10-vazifa: Dictionary bo‘sh yoki yo‘qligini tekshirish
# # len() funksiyasi: Dictionaryning uzunligini (elementlar sonini) qaytaradi
# # == 0: Uzunlik 0 ga teng bo‘lsa, dictionary bo‘sh deb hisoblanadi
# # Nima uchun ishlatildi: Dictionaryda element bor yoki yo‘qligini tekshirish uchun
# result10 = len(student_grades) == 0
# print("10-vazifa natijasi:", result10)  # Natija: False

# 2-Masala: Meva narxlari
# fruits = {"olma": 5000, "banan": 12000, "uzum": 8000}
#
# # Boshlang'ich dictionary: fruits
# fruits = {"olma": 5000, "banan": 12000, "uzum": 8000}
#
# # 1-vazifa: "anor" mevani 10000 so‘m bilan qo‘shish
# # Kalit orqali qo‘shish: Dictionaryga yangi kalit-qiymat juftligini qo‘shish
# # Nima uchun ishlatildi: Yangi meva va narxini qo‘shish uchun
# fruits["anor"] = 10000
# result1 = fruits
# print("1-vazifa natijasi:", result1)  # Natija: {'olma': 5000, 'banan': 12000, 'uzum': 8000, 'anor': 10000}
#
# # 2-vazifa: "banan" narxini 15000 ga o‘zgartirish
# # Kalit orqali o‘zgartirish: Mavjud kalitning qiymatini yangi qiymat bilan almashtirish
# # Nima uchun ishlatildi: "banan" narxini yangilash uchun
# fruits["banan"] = 15000
# result2 = fruits
# print("2-vazifa natijasi:", result2)  # Natija: {'olma': 5000, 'banan': 15000, 'uzum': 8000, 'anor': 10000}
#
# # 3-vazifa: "uzum" ni o‘chirish
# # del operatori: Dictionarydan kalit-qiymat juftligini o‘chirish uchun ishlatiladi
# # Nima uchun ishlatildi: "uzum" mevani dictionarydan olib tashlash uchun
# del fruits["uzum"]
# result3 = fruits
# print("3-vazifa natijasi:", result3)  # Natija: {'olma': 5000, 'banan': 15000, 'anor': 10000}
#
# # 4-vazifa: Narxlarning umumiy summasini topish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # sum() funksiyasi: Iterable elementlarining yig‘indisini hisoblaydi
# # Nima uchun ishlatildi: Barcha mevalar narxlarini yig‘ish uchun
# result4 = sum(fruits.values())
# print("4-vazifa natijasi:", result4)  # Natija: 30000
#
# # 5-vazifa: Eng qimmat mevani topish
# # max() funksiyasi: Iterable ichidagi eng katta elementni qaytaradi
# # key=fruits.get: max() funksiyasiga dictionary qiymatlari bo‘yicha taqqoslashni ko‘rsatadi
# # Nima uchun ishlatildi: Eng yuqori narxga ega mevani aniqlash uchun
# result5 = max(fruits, key=fruits.get)
# print("5-vazifa natijasi:", result5)  # Natija: banan
#
# # 6-vazifa: Eng arzon mevani topish
# # min() funksiyasi: Iterable ichidagi eng kichik elementni qaytaradi
# # key=fruits.get: min() funksiyasiga dictionary qiymatlari bo‘yicha taqqoslashni ko‘rsatadi
# # Nima uchun ishlatildi: Eng past narxga ega mevani aniqlash uchun
# result6 = min(fruits, key=fruits.get)
# print("6-vazifa natijasi:", result6)  # Natija: olma
#
# # 7-vazifa: Narxlar ro‘yxatini tartiblang
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # sorted() funksiyasi: Iterable elementlarini tartiblab ro‘yxat sifatida qaytaradi (o‘sish tartibida)
# # Nima uchun ishlatildi: Narxlarni kichikdan kattaga tartiblash uchun
# result7 = sorted(fruits.values())
# print("7-vazifa natijasi:", result7)  # Natija: [5000, 10000, 15000]
#
# # 8-vazifa: Dictionary uzunligini topish
# # len() funksiyasi: Dictionaryning elementlar sonini qaytaradi
# # Nima uchun ishlatildi: Dictionaryda nechta meva borligini aniqlash uchun
# result8 = len(fruits)
# print("8-vazifa natijasi:", result8)  # Natija: 3
#
# # 9-vazifa: "olma" narxini chop etish
# # get() metodi: Dictionarydan kalit bo‘yicha qiymatni olish uchun ishlatiladi
# # Nima uchun ishlatildi: "olma" ning narxini xavfsiz tarzda olish uchun
# result9 = fruits.get("olma")
# print("9-vazifa natijasi:", result9)  # Natija: 5000
#
# # 10-vazifa: Barcha mevalarni alifbo tartibida chop etish
# # keys() metodi: Dictionaryning kalitlarini ro‘yxat sifatida qaytaradi
# # sorted() funksiyasi: Kalitlarni alifbo tartibida tartiblash uchun
# # Nima uchun ishlatildi: Mevalar nomini alifbo tartibida ko‘rish uchun
# result10 = sorted(fruits.keys())
# print("10-vazifa natijasi:", result10)  # Natija: ['anor', 'banan', 'olma']

# 3-Masala: Shahar aholisi
# cities = {"Toshkent": 2500000, "Samarqand": 550000, "Buxoro": 280000}
#
# cities["Andijon"] = 600000
# andijon = cities
# print("1-vazifa natijasi:", andijon)
#
# cities["Toshkent"] = 2600000
# toshkent = cities
# print("2-vazifa natijasi:", toshkent)
#
# del cities["Buxoro"]
# buxoro = cities
# print("3-vazifa natijasi:", buxoro)
#
# result4 = sum(cities.values())
# print("4-vazifa natijasi:", result4)
#
# result5 = sum(cities.values()) / len(cities)
# print("5-vazifa natijasi:", result5)
#
# result6 = max(cities, key=cities.get)
# print("6-vazifa natijasi:", result6)
#
# result7 = min(cities, key=cities.get)
# print("7-vazifa natijasi:", result7)
#
# cities.keys()
# print("8-vazifa natijasi:", cities)
#
# result9 = sorted(cities.values())
# print("9-vazifa natijasi:", result9 )
#
# len(cities) == 0
# print("10-vazifa natijasi:", cities)

# 4-Masala: Kitoblar va mualliflar
books = {"Alximik": "Paulo Koelyo", "Shaytanat": "Tohir Malik", "1984": "George Orwell"}

books.update({"O‘tkan kunlar": "Abdulla Qodiriy"})
print("1-vazifa natijasi:", books)

books['Alximik'] = "Paulo Coelho"
result2 = books
print("2-vazifa natijasi:", result2)

del books['1984']
print("3-vazifa natijasi:", books)

result4 = len(books)
print("4-vazifa natijasi:", result4)

result5 = books.values()
print("5-vazifa natijasi:", result5)

result6 = sorted(books.keys())
print("6-vazifa natijasi:", result6)

result7 = books.get('Shaytanat')
print("7-vazifa natijasi:", result7)

result8 = len(books)
print("8-vazifa natijasi:", result8)

"O‘tkan kunlar" in books







































































