# Boshlang'ich o'zgaruvchi: "fruits" deb nomlangan set o'zgaruvchi yaratamiz
fruits = {"apple", "banana"}

# 1-vazifa: "cherry" mevasini qo'shish
# add() metodi: Setga yangi element qo'shadi, agar element allaqachon mavjud bo'lsa, hech narsa qilmaydi
# Misol: {"apple", "banana"} + "cherry" -> {"apple", "banana", "cherry"}
result1 = fruits.add("cherry")
print("1-vazifa natijasi:", fruits)  # Natija: {'apple', 'banana', 'cherry'}

# 2-vazifa: "banana" mevasini o'chirish
# remove() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato (KeyError) chiqaradi
# Misol: {"apple", "banana", "cherry"} - "banana" -> {"apple", "cherry"}
result2 = fruits.remove("banana")
print("2-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry'}

# 3-vazifa: "kiwi" mevasini qo'shish
# add() metodi: Setga yangi element qo'shadi
# Misol: {"apple", "cherry"} + "kiwi" -> {"apple", "cherry", "kiwi"}
result3 = fruits.add("kiwi")
print("3-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi'}

# 4-vazifa: "apple" setda mavjudligini tekshirish
# in operatori: Element setda mavjud bo'lsa True, aks holda False qaytaradi
# Misol: "apple" in {"apple", "cherry", "kiwi"} -> True
result4 = "apple" in fruits
print("4-vazifa natijasi:", "yes" if result4 else "no")  # Natija: yes

# 5-vazifa: "tropicals" setini yaratish va "fruits" ga qo'shish
# update() metodi: Setga boshqa iterable (masalan, boshqa set) elementlarini qo'shadi
# Misol: {"apple", "cherry", "kiwi"} + {"pineapple", "banana"} -> {"apple", "cherry", "kiwi", "pineapple", "banana"}
tropicals = {"pineapple", "banana"}
result5 = fruits.update(tropicals)
print("5-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple', 'banana'}

# 6-vazifa: "banana" ni o'chirish (xatolik bermasi uchun)
# discard() metodi: Setdan belgilangan elementni o'chiradi, agar element topilmasa xato chiqarmaydi
# Misol: {"apple", "cherry", "kiwi", "pineapple", "banana"} - "banana" -> {"apple", "cherry", "kiwi", "pineapple"}
result6 = fruits.discard("banana")
print("6-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}

# 7-vazifa: "fruits" va "tropicals" farqini topish
# difference() metodi: Birinchi setda bo'lib, ikkinchi setda bo'lmagan elementlarni qaytaradi
# Misol: {"apple", "cherry", "kiwi", "pineapple"} - {"pineapple", "banana"} -> {"apple", "cherry", "kiwi"}
result7 = fruits.difference(tropicals)
print("7-vazifa natijasi:", result7)  # Natija: {'apple', 'cherry', 'kiwi'}

# 8-vazifa: Yangi unique "fruits" nomli setga saqlash
# Setning o'zi elementlarni takrorlanmas qiladi, shuning uchun faqat yangi nom bilan saqlash kifoya
# Misol: {"apple", "cherry", "kiwi", "pineapple"} ni "unique_fruits" ga ko'chirish
unique_fruits = fruits
result8 = unique_fruits
print("8-vazifa natijasi:", result8)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}

# 9-vazifa: Barcha mevalarni alifbo bo'yicha tartiblash
# sorted() funksiyasi: Iterable (masalan, set) elementlarini alifbo tartibida ro'yxat sifatida qaytaradi
# Misol: {"apple", "cherry", "kiwi", "pineapple"} -> ['apple', 'cherry', 'kiwi', 'pineapple']
result9 = sorted(fruits)
print("9-vazifa natijasi:", result9)  # Natija: ['apple', 'cherry', 'kiwi', 'pineapple']

# 10-vazifa: Yakuniy holatni chop etish
# Faqat joriy setni chop qilish uchun hech qanday metod ishlatmaymiz
print("10-vazifa natijasi:", fruits)  # Natija: {'apple', 'cherry', 'kiwi', 'pineapple'}