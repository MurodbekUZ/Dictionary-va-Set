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
# books = { "Alximik": "Paulo Koelyo",  "Shaytanat": "Tohir Malik",  "1984": "George Orwell"}
#
# # 1. Yangi kitob qo‘shish
# books.update({"O‘tkan kunlar": "Abdulla Qodiriy"})
# print("1-vazifa natijasi:", books)
#
# # 2. 'Alximik' muallifini o‘zgartirish
# books['Alximik'] = "Paulo Coelho"
# print("2-vazifa natijasi:", books)
#
# # 3. '1984' kitobini o‘chirish
# del books['1984']
# print("3-vazifa natijasi:", books)
#
# # 4. Kitoblar sonini topish
# result4 = len(books)
# print("4-vazifa natijasi:", result4)
#
# # 5. Mualliflar ro‘yxatini chop etish
# result5 = books.values()
# print("5-vazifa natijasi:", result5)
#
# # 6. Kitob nomlarini alifbo tartibida chop etish
# result6 = sorted(books.keys())
# print("6-vazifa natijasi:", result6)
#
# # 7. 'Shaytanat' muallifini chop etish
# result7 = books.get('Shaytanat')
# print("7-vazifa natijasi:", result7)
#
# # 8. Dictionary uzunligini topish
# result8 = len(books)
# print("8-vazifa natijasi:", result8)
#
# # 9. 'O‘tkan kunlar' mavjudligini tekshirish
# result9 = "O‘tkan kunlar" in books
# print("9-vazifa natijasi:", result9)
#
# # 10. Dictionary-ni tozalash
# books.clear()
# print("10-vazifa natijasi:", books)

# 5-Masala: Valyuta kurslari

# Boshlang‘ich dictionary
# currencies = {"USD": 12600, "EUR": 13500, "RUB": 140}
#
# # 1. "GBP" ni 16000 bilan qo‘shish
# currencies.update({"GBP": 16000})
# print("1-vazifa natijasi:", currencies)
#
# # 2. "USD" kursini 12700 ga o‘zgartirish
# currencies["USD"] = 12700
# print("2-vazifa natijasi:", currencies)
#
# # 3. "RUB" ni o‘chirish
# del currencies["RUB"]
# print("3-vazifa natijasi:", currencies)
#
# # 4. Kurslar yig‘indisini topish
# result4 = sum(currencies.values())
# print("4-vazifa natijasi:", result4)
#
# # 5. Eng yuqori kursni topish
# result5 = max(currencies, key=currencies.get)
# print("5-vazifa natijasi:", result5)
#
# # 6. Eng past kursni topish
# result6 = min(currencies, key=currencies.get)
# print("6-vazifa natijasi:", result6)
#
# # 7. Valyutalar ro‘yxatini chop etish
# result7 = currencies.keys()
# print("7-vazifa natijasi:", result7)
#
# # 8. Kurslar ro‘yxatini tartib bilan chop etish
# result8 = sorted(currencies.values())
# print("8-vazifa natijasi:", result8)
#
# # 9. "EUR" kursini chop etish
# result9 = currencies.get("EUR")
# print("9-vazifa natijasi:", result9)
#
# # 10. Dictionary bo‘sh yoki yo‘qligini tekshirish
# result10 = len(currencies) == 0
# print("10-vazifa natijasi:", result10)

# # 6-Masala: Do‘kon inventari
# inventory = {"suv": 50, "non": 100, "shokolad": 20}
#
# # 1. "cola" ni 30 ta bilan qo‘shish
# inventory["cola"] = 30
# # yoki: inventory.update({"cola": 30})
#
# # 2. "non" sonini 80 ga o‘zgartirish
# inventory["non"] = 80
#
# # 3. "shokolad" ni o‘chirish
# del inventory["shokolad"]
#
# # 4. Umumiy mahsulotlar sonini topish
# umumiy_son = sum(inventory.values())
#
# # 5. Eng ko‘p mahsulot
# eng_kop = max(inventory.keys(), key=inventory.get)
#
# # 6. Eng kam mahsulot
# eng_kam = min(inventory.keys(), key=inventory.get)
#
# # 7. Mahsulotlar ro‘yxati
# mahsulotlar = list(inventory.keys())
#
# # 8. Mahsulotlar sonini tartiblash
# tartiblangan_sonlar = sorted(inventory.values())
#
# # 9. "suv" sonini chop etish
# suv_soni = inventory.get("suv")
#
# # 10. Dictionary bo‘sh yoki yo‘qligini tekshirish
# boshlik = (len(inventory) == 0)
#
# # Natijalarni chiqarish
# print("Yangilangan inventar:", inventory)
# print("Umumiy son:", umumiy_son)
# print("Eng ko‘p mahsulot:", eng_kop)
# print("Eng kam mahsulot:", eng_kam)
# print("Mahsulotlar ro‘yxati:", mahsulotlar)
# print("Tartiblangan sonlar:", tartiblangan_sonlar)
# print('"Suv" soni:', suv_soni)
# print("Dictionary bo‘shmi?", boshlik)

# # 7-Masala: Sportchilar reytingi
# athletes = {"Ali": 150, "Vali": 120, "Sardor": 180}
#
# # 1. "Nodir"ni 130 ochko bilan qo‘shish
# athletes["Nodir"] = 130
# # yoki: athletes.update({"Nodir": 130})
#
# # 2. "Vali" ochkosini 140 ga o‘zgartirish
# athletes["Vali"] = 140
#
# # 3. "Sardor"ni o‘chirish
# del athletes["Sardor"]
#
# # 4. Umumiy ochkolar
# umumiy = sum(athletes.values())
#
# # 5. O‘rtacha ochko
# ortacha = umumiy / len(athletes)
#
# # 6. Eng yuqori ochkoga ega sportchi
# eng_yuqori = max(athletes.keys(), key=athletes.get)
#
# # 7. Eng past ochkoga ega sportchi
# eng_past = min(athletes.keys(), key=athletes.get)
#
# # 8. Sportchilar ro‘yxati
# sportchilar = list(athletes.keys())
#
# # 9. Tartiblangan ochkolar ro‘yxati
# tartib_ochkolar = sorted(athletes.values())
#
# # 10. Dictionary bo‘sh yoki yo‘qligi
# boshlik = (len(athletes) == 0)
#
# # Natijalarni chiqarish
# print("Yangilangan ro‘yxat:", athletes)
# print("Umumiy ochkolar:", umumiy)
# print("O‘rtacha ochko:", ortacha)
# print("Eng yuqori ochko:", eng_yuqori)
# print("Eng past ochko:", eng_past)
# print("Sportchilar:", sportchilar)
# print("Tartiblangan ochkolar:", tartib_ochkolar)
# print("Dictionary bo‘shmi?", boshlik)

# # 8-Masala: Restoran menyusi
# menu = {"osh": 25000, "shashlik": 30000, "somsa": 5000}
#
# # 1. "lag'mon"ni 20000 bilan qo‘shish
# menu["lag'mon"] = 20000
# # yoki: menu.update({"lag'mon": 20000})
#
# # 2. "somsa" narxini 6000 ga o‘zgartirish
# menu["somsa"] = 6000
#
# # 3. "shashlik"ni o‘chirish
# del menu["shashlik"]
#
# # 4. Menyu narxlari yig‘indisi
# yigindi = sum(menu.values())
#
# # 5. Eng qimmat taom
# eng_qimmat = max(menu.keys(), key=menu.get)
#
# # 6. Eng arzon taom
# eng_arzon = min(menu.keys(), key=menu.get)
#
# # 7. Taomlar ro‘yxati
# taomlar = list(menu.keys())
#
# # 8. Narxlarni tartiblash
# tartib_narxlar = sorted(menu.values())
#
# # 9. "osh" narxini chop etish
# osh_narxi = menu.get("osh")
#
# # 10. Dictionary bo‘sh yoki yo‘qligi
# boshlik = (len(menu) == 0)
#
# # Natijalar
# print("Yangilangan menyu:", menu)
# print("Narxlar yig‘indisi:", yigindi)
# print("Eng qimmat taom:", eng_qimmat)
# print("Eng arzon taom:", eng_arzon)
# print("Taomlar:", taomlar)
# print("Tartiblangan narxlar:", tartib_narxlar)
# print('"Osh" narxi:', osh_narxi)
# print("Dictionary bo‘shmi?", boshlik)

# # 9-Masala: Universitet fakultetlari
# # Boshlang'ich dictionary
# faculties = {"IT": 120, "Matematika": 80, "Filologiya": 60}
#
# # 1. "Fizika"ni 90 talaba bilan qo‘shish
# faculties["Fizika"] = 90
# # yoki: faculties.update({"Fizika": 90})
#
# # 2. "IT" talabalar sonini 130 ga o‘zgartirish
# faculties["IT"] = 130
#
# # 3. "Filologiya"ni o‘chirish
# del faculties["Filologiya"]
#
# # 4. Umumiy talabalar soni
# umumiy = sum(faculties.values())
#
# # 5. O‘rtacha talabalar soni
# ortacha = umumiy / len(faculties)
#
# # 6. Eng ko‘p talaba bor fakultet
# eng_kop = max(faculties.keys(), key=faculties.get)
#
# # 7. Eng kam talaba bor fakultet
# eng_kam = min(faculties.keys(), key=faculties.get)
#
# # 8. Fakultetlar ro‘yxati
# fakultetlar = list(faculties.keys())
#
# # 9. Talabalar sonini tartiblash
# tartib_talabalar = sorted(faculties.values())
#
# # 10. Dictionary bo‘sh yoki yo‘qligi
# boshlik = (len(faculties) == 0)
#
# # Natijalar
# print("Yangilangan fakultetlar:", faculties)
# print("Umumiy talabalar:", umumiy)
# print("O‘rtacha talabalar:", ortacha)
# print("Eng ko‘p talaba:", eng_kop)
# print("Eng kam talaba:", eng_kam)
# print("Fakultetlar:", fakultetlar)
# print("Tartiblangan talabalar soni:", tartib_talabalar)
# print("Dictionary bo‘shmi?", boshlik)

# # 10-Masala: Sayohat joylari
# # Boshlang'ich dictionary
# destinations = {"Parij": 500, "Dubay": 300, "Istanbul": 200}
#
# # 1. "London"ni 450 bilan qo‘shish
# destinations["London"] = 450
# # yoki: destinations.update({"London": 450})
#
# # 2. "Istanbul" narxini 250 ga o‘zgartirish
# destinations["Istanbul"] = 250
#
# # 3. "Dubay"ni o‘chirish
# del destinations["Dubay"]
#
# # 4. Narxlar yig‘indisi
# yigindi = sum(destinations.values())
#
# # 5. Eng qimmat sayohat
# eng_qimmat = max(destinations.keys(), key=destinations.get)
#
# # 6. Eng arzon sayohat
# eng_arzon = min(destinations.keys(), key=destinations.get)
#
# # 7. Joylar ro‘yxati
# joylar = list(destinations.keys())
#
# # 8. Narxlarni tartiblash
# tartib_narxlar = sorted(destinations.values())
#
# # 9. "Parij" narxini chop etish
# parij_narxi = destinations.get("Parij")
#
# # 10. Dictionary bo‘sh yoki yo‘qligi
# boshlik = (len(destinations) == 0)
#
# # Natijalar
# print("Yangilangan joylar:", destinations)
# print("Narxlar yig‘indisi:", yigindi)
# print("Eng qimmat sayohat:", eng_qimmat)
# print("Eng arzon sayohat:", eng_arzon)
# print("Joylar ro‘yxati:", joylar)
# print("Tartiblangan narxlar:", tartib_narxlar)
# print('"Parij" narxi:', parij_narxi)
# print("Dictionary bo‘shmi?", boshlik)

# # 11-Masala: Smartfon xususiyatlari
# # Boshlang'ich dictionary
# phones = {"iPhone 15": 12000000, "Samsung S24": 9000000, "Xiaomi 14": 6000000}
#
# # 1. "Redmi Note 13" ni 4500000 bilan qo‘shish
# phones["Redmi Note 13"] = 4500000
# # yoki: phones.update({"Redmi Note 13": 4500000})
#
# # 2. "Samsung S24" narxini 8500000 ga o‘zgartirish
# phones["Samsung S24"] = 8500000
#
# # 3. "Xiaomi 14" ni o‘chirish
# del phones["Xiaomi 14"]
#
# # 4. Narxlar yig‘indisi
# yigindi = sum(phones.values())
#
# # 5. O‘rtacha telefon narxi
# ortacha = yigindi / len(phones)
#
# # 6. Eng qimmat telefon
# eng_qimmat = max(phones.keys(), key=phones.get)
#
# # 7. Eng arzon telefon
# eng_arzon = min(phones.keys(), key=phones.get)
#
# # 8. Telefon modellarini alifbo tartibida chiqarish
# alfabo_modellar = sorted(phones.keys())
#
# # 9. "iPhone 15" narxini chop etish
# iphone_narxi = phones.get("iPhone 15")
#
# # 10. Narxlarni kamayish tartibida saralash
# kamayish_narxlar = sorted(phones.values(), reverse=True)
#
# # Natijalar
# print("Yangilangan telefonlar:", phones)
# print("Narxlar yig‘indisi:", yigindi)
# print("O‘rtacha narx:", ortacha)
# print("Eng qimmat telefon:", eng_qimmat)
# print("Eng arzon telefon:", eng_arzon)
# print("Alifbo tartibidagi modellar:", alfabo_modellar)
# print('"iPhone 15" narxi:', iphone_narxi)
# print("Narxlar (katta → kichik):", kamayish_narxlar)

# # 12-Masala: Kompaniya xodimlari
# # Boshlang'ich dictionary
# employees = {"Anvar": 8000000, "Malika": 12000000, "Javohir": 10000000}
#
# # 1. "Dilnoza"ni 9000000 maosh bilan qo‘shish
# employees["Dilnoza"] = 9000000
# # yoki: employees.update({"Dilnoza": 9000000})
#
# # 2. "Anvar" maoshini 8500000 ga oshirish
# employees["Anvar"] = 8500000
#
# # 3. "Javohir"ni o‘chirish
# del employees["Javohir"]
#
# # 4. Umumiy maosh fondi
# yigindi = sum(employees.values())
#
# # 5. O‘rtacha maosh
# ortacha = yigindi / len(employees)
#
# # 6. Eng yuqori maoshli xodim
# eng_yuqori = max(employees.keys(), key=employees.get)
#
# # 7. Eng past maoshli xodim
# eng_past = min(employees.keys(), key=employees.get)
#
# # 8. Xodimlar ro‘yxati (alifbo tartibida)
# alfabo_royxat = sorted(employees.keys())
#
# # 9. 10 000 000 dan yuqori maoshli xodimlar soni
# yuqori_maosh_soni = sum(1 for v in employees.values() if v > 10_000_000)
#
# # 10. Dictionary nusxasi
# employees_copy = employees.copy()
#
# # Natijalar
# print("Yangilangan xodimlar:", employees)
# print("Umumiy maosh fondi:", yigindi)
# print("O‘rtacha maosh:", ortacha)
# print("Eng yuqori maosh:", eng_yuqori)
# print("Eng past maosh:", eng_past)
# print("Alifbo bo‘yicha ro‘yxat:", alfabo_royxat)
# print("10 mln.dan yuqori maoshli xodimlar soni:", yuqori_maosh_soni)
# print("Nusxa:", employees_copy)

# # 13-Masala: Maktab darslari
# # Boshlang'ich dictionary
# schedule = {"Matematika": 5, "Ona tili": 4, "Tarix": 3, "Fizika": 4}
#
# # 1. "Ingliz tili"ni 3 soat bilan qo‘shish
# schedule["Ingliz tili"] = 3
# # yoki: schedule.update({"Ingliz tili": 3})
#
# # 2. "Matematika" soatini 6 ga o‘zgartirish
# schedule["Matematika"] = 6
#
# # 3. "Tarix"ni o‘chirish
# del schedule["Tarix"]
#
# # 4. Haftalik umumiy dars soatlari
# umumiy = sum(schedule.values())
#
# # 5. O‘rtacha soat
# ortacha = umumiy / len(schedule)
#
# # 6. Eng ko‘p soatli fan
# eng_kop = max(schedule.keys(), key=schedule.get)
#
# # 7. Eng kam soatli fan
# eng_kam = min(schedule.keys(), key=schedule.get)
#
# # 8. Barcha fanlar ro‘yxati
# fanlar = list(schedule.keys())
#
# # 9. Darslar (fanlar) soni
# fanlar_soni = len(schedule)
#
# # 10. Soatlarni o‘sish tartibida saralash
# tartib_soatlar = sorted(schedule.values())
#
# # Natijalar
# print("Yangilangan dars jadvali:", schedule)
# print("Umumiy soatlar:", umumiy)
# print("O‘rtacha soat:", ortacha)
# print("Eng ko‘p soatli fan:", eng_kop)
# print("Eng kam soatli fan:", eng_kam)
# print("Fanlar ro‘yxati:", fanlar)
# print("Fanlar soni:", fanlar_soni)
# print("Saralangan soatlar:", tartib_soatlar)

# # 14-Masala: Avtomobil brendlari
# # Boshlang'ich dictionary
# car_sales = {"Toyota": 150000, "Chevrolet": 80000, "BMW": 45000, "Mercedes": 50000}
#
# # 1. "Tesla"ni 60000 bilan qo‘shish
# car_sales["Tesla"] = 60000
# # yoki: car_sales.update({"Tesla": 60000})
#
# # 2. "Chevrolet" savdosini 90000 ga oshirish
# car_sales["Chevrolet"] = 90000
#
# # 3. "BMW"ni o‘chirish
# del car_sales["BMW"]
#
# # 4. Umumiy savdo hajmi
# umumiy = sum(car_sales.values())
#
# # 5. Eng ko‘p sotilgan brend
# eng_kop = max(car_sales.keys(), key=car_sales.get)
#
# # 6. Eng kam sotilgan brend
# eng_kam = min(car_sales.keys(), key=car_sales.get)
#
# # 7. Brendlar ro‘yxati
# brendlar = list(car_sales.keys())
#
# # 8. 100000 dan ko‘p sotilgan brendlar soni
# yuzmingdan_kop = sum(1 for v in car_sales.values() if v > 100000)
#
# # 9. Savdo hajmlarini kamayish tartibida saralash
# tartib_savdo = sorted(car_sales.values(), reverse=True)
#
# # 10. "Toyota" savdo hajmi
# toyota_savdo = car_sales.get("Toyota")
#
# # Natijalar
# print("Yangilangan ro‘yxat:", car_sales)
# print("Umumiy savdo hajmi:", umumiy)
# print("Eng ko‘p sotilgan brend:", eng_kop)
# print("Eng kam sotilgan brend:", eng_kam)
# print("Brendlar:", brendlar)
# print("100k+ brendlar soni:", yuzmingdan_kop)
# print("Kamayish tartibi:", tartib_savdo)
# print('"Toyota" savdosi:', toyota_savdo)

# 15-Masala: Kinolar reytingi


















