""" 
1. __str__:
Bu metod ob'ektni foydalanuvchi uchun yoqimli, oson o'qiladigan shaklda ifodalash uchun ishlatiladi. str() funksiyasi yoki print() chaqirilganda ishlaydi.

Foydalanish maqsadi:
Ob'ektni foydalanuvchi uchun oson tushuniladigan ko'rinishda taqdim etish.

__add__: Qo'shish (+) operatori uchun ishlatiladi.
__mul__: Ko'paytirish (*) operatori uchun ishlatiladi.
__sub__: Ayirish (-) operatori uchun ishlatiladi.
__truediv__: Bo'lish (/) operatori uchun ishlatiladi.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.name)

person = Person("Alice", 30)
p2=Person('ali',12)
print(p2)
print(person)

# Eslatma:
# Foydalanuvchi uchun mo'ljallangan.
# Agar __str__ metodini aniqlamasangiz, print() chaqirilganda ob'ektning __repr__ natijasi yoki default object ko'rinishi (masalan, <Person object at 0x...>) qaytadi.

"""2. __repr__:
Bu metod ob'ektni rivojlantiruvchi (developer) uchun aniqroq ifodalash uchun ishlatiladi. repr() funksiyasi chaqirilganda yoki ob'ekt interaktiv shell'da yozilganda avtomatik ravishda chaqiriladi.

Foydalanish maqsadi:
Ob'ektni dastur kodida qayta yaratish imkonini beruvchi ifoda shaklida taqdim etish.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}'s age is {self.age}"

    def __repr__(self):
        return str(self.age)

person = Person("Alice", 30)
print(person)
print(repr(person))  # Person('Alice', 30)

"""3. __len__:
Bu metod ob'ektning uzunligini aniqlash uchun ishlatiladi. len() funksiyasi chaqirilganda avtomatik ishga tushadi.

Foydalanish maqsadi:
Ob'ektning elementlar sonini qaytarish.
"""



class Team:
    def __init__(self, members):
        self.members = members
        # self.guruh=['ali','vali','vali','vali']

    # def __len__(self):
    #     return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
team2=Team(['ali','vali','vali','vali','jobir','bobur'])
print(len(team2))

"""4. __abs__:
Bu metod ob'ektning mutlaq qiymatini aniqlash uchun ishlatiladi. abs() funksiyasi chaqirilganda ishga tushadi.

Foydalanish maqsadi:
Ob'ektni matematik mutlaq qiymatini qaytarish.
"""

class Temperature:
    def __init__(self, value):
        self.value = value

    def __abs__(self):
        return abs(self.value)

temp = Temperature(-42)
print(abs(temp))

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vectorlar({self.x}, {self.y})"

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)  # Vector uzunligi

    def __abs__(self):
        return int((self.x**2 + self.y**2)**0.5 ) # Mutlaq uzunlik

vector = Vector(3, -5)
print(vector)        # Vector(3, 4)
print(repr(vector))  # Vector(3, 4)
print(len(vector))   # 5 (3-4-5 uchburchagi)
print(abs(vector))   # 5.0

"""# Новый раздел

# Новый раздел

__add__:
Bu metod qo'shish (+) operatori uchun ishlatiladi. Ob'ektlarni + operatori orqali qo'shganingizda ishga tushadi.

Foydalanish maqsadi:
Ob'ektlarni matematik qo'shish yoki ular orasida boshqa ma'noli birlashuvni amalga oshirish.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
      if isinstance(other, Vector):
        return Vector(self.x + other.x, self.y + other.y)
      elif type(other)==int:
        return Vector(self.x + other, self.y + other)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3=Vector(1,2)
v4=Vector(5,6)
result = v1 + v2 + v3+v4+10
print(result)
v2 = v2+v1
# print(v2)

"""2. __mul__:
Bu metod ko'paytirish (*) operatori uchun ishlatiladi. Ob'ektlarni * orqali ko'paytirganingizda ishga tushadi.

Foydalanish maqsadi:
Ob'ektlarni matematik ko'paytirish yoki ular orasidagi boshqa ko'payish ma'nosini aniqlash.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Vector(self.x * scalar.x, self.y * scalar.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(2, 3)
v2=Vector(4,5)
result = v * v2
print(result)

"""__sub__:
Bu metod ayirish (-) operatori uchun ishlatiladi. Ob'ektlarni - orqali ayirganingizda ishga tushadi.

Foydalanish maqsadi:
Ob'ektlar orasidagi farqni aniqlash yoki boshqa ayirish xatti-harakatini belgilash.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(5, 7)
v2 = Vector(2, 3)
result = v2-v1
print(result)

"""__truediv__:
Bu metod bo'lish (/) operatori uchun ishlatiladi. Ob'ektlarni / orqali bo'lganingizda ishga tushadi.

Foydalanish maqsadi:
Ob'ektlarni matematik bo'lish yoki boshqa bo'linish xatti-harakatini belgilash.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f})"

v = Vector(6, 9)
result = v / 3
print(result)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1 / 2)

"""__eq__: Tenglikni (==) tekshirish.
__ne__: Teng emasligini (!=) tekshirish.
__lt__: Kichikligini (<) tekshirish.
__le__: Kichik yoki tengligini (<=) tekshirish.
__gt__: Kattaligini (>) tekshirish.
__ge__: Katta yoki tengligini (>=) tekshirish.

__eq__: Tenglik operatori (==)
Bu metod ikkita ob'ektning tengligini tekshirish uchun ishlatiladi. Agar a == b deb yozsangiz, Python __eq__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

s1 = Student("Ali", 85)
# print(s1)
s2 = Student("Ali", 85)
# print(s2)
print(s1 == s2)  # True (ularning `grade` qiymatlari teng)

"""__ne__: Teng emas (!=)
Bu metod ikkita ob'ekt teng emasligini tekshirish uchun ishlatiladi. Agar a != b deb yozsangiz, Python __ne__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __ne__(self, other):
        return self.grade != other.grade

s1 = Student("Ali", 85)
s2 = Student("Vali", 90)
print(s1 != s2)  # True (ularning `grade` qiymatlari farq qiladi)

"""__lt__: Kichikroq (<)
Bu metod ob'ektning boshqa ob'ektdan kichikligini tekshirish uchun ishlatiladi. Agar a < b deb yozsangiz, Python __lt__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student("Ali", 85)
s2 = Student("Vali", 90)
print(s1 < s2)  # True (85 < 90)

"""__le__: Kichik yoki teng (<=)
Bu metod ob'ektning boshqa ob'ektdan kichik yoki teng ekanligini tekshirish uchun ishlatiladi. Agar a <= b deb yozsangiz, Python __le__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __le__(self, other):
        return self.grade <= other.grade

s1 = Student("Ali", 85)
s2 = Student("Vali", 85)
print(s1 <= s2)  # True (85 <= 85)

"""__gt__: Kattaroq (>)
Bu metod ob'ektning boshqa ob'ektdan kattaligini tekshirish uchun ishlatiladi. Agar a > b deb yozsangiz, Python __gt__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __gt__(self, other):
        return self.grade > other.grade

s1 = Student("Ali", 90)
s2 = Student("Vali", 85)
print(s1 > s2)  # True (90 > 85)

"""__ge__: Katta yoki teng (>=)
Bu metod ob'ektning boshqa ob'ektdan katta yoki teng ekanligini tekshirish uchun ishlatiladi. Agar a >= b deb yozsangiz, Python __ge__ metodini chaqiradi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __ge__(self, other):
        return self.grade >= other.grade

s1 = Student("Ali", 85)
s2 = Student("Vali", 85)
print(s1 >= s2)  # True (85 >= 85)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __ne__(self, other):
        return self.grade != other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __le__(self, other):
        return self.grade <= other.grade

    def __gt__(self, other):
        return self.grade > other.grade

    def __ge__(self, other):
        return self.grade >= other.grade

s1 = Student("Ali", 85)
s2 = Student("Vali", 90)

print(s1 == s2)
print(s1 != s2)
print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)

"""Python'da __eq__ va __hash__ maxsus metodlari ob'ektlarning tenglikni tekshirish va hashlash (hash function) qobiliyatlarini belgilash uchun ishlatiladi. Ular bir-biri bilan bog‘liq va to‘g‘ri ishlashi uchun birgalikda sozlanishi kerak, ayniqsa agar ob'ektlar hashable (masalan, set yoki dict ichida ishlatiladigan kalit) sifatida ishlatilsa.

__eq__: Tenglikni tekshirish
__eq__ operatori ob'ektlarning qiymat asosida tengligini aniqlash uchun ishlatiladi.

Agar a == b yozsangiz, Python __eq__ metodini chaqiradi.
Standart xatti-harakat: Agar __eq__ metodini o'zingiz belgilamasangiz, Python id() (xotira manzili) bo'yicha taqqoslaydi.
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.grade == other.grade
        return False

s1 = Student("Ali", 85)
s2 = Student("Ali", 85)
s3 = Student("Vali", 90)

print(s1 == s2)  # True (qiymatlar teng)
print(s1 == s3)  # False (qiymatlar farq qiladi)
print(s1 == "Ali")  # False (tur mos emas)

"""__hash__: Hash qiymati
__hash__ metodi ob'ektning hash qiymatini qaytaradi. Hash qiymatlari Python'da ma'lumotlar tuzilmalari (masalan, set va dict) uchun ishlatiladi.

Agar ob'ekt hashable bo‘lsa, uning hash qiymati o‘zgarmas bo‘lishi kerak.
Muhim: Agar __eq__ qayta aniqlangan bo‘lsa va ob'ektlar teng deb topilgan bo‘lsa, ular bir xil hash qiymatiga ega bo‘lishi kerak.
Misol:
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.grade == other.grade
        return False

    def __hash__(self):
        return hash((self.name, self.grade))

s1 = Student("Ali", 85)
s2 = Student("Ali", 85)
s3 = Student("Vali", 90)

# Hashable object as keys in a dictionary
students = {s1: "Excellent", s3: "Good",s2:'Salomlar'}
print(students)  # Excellent (s1 va s2 teng, shuning uchun bir xil hash)

"""Tenglik va Hash o‘rtasidagi bog‘liqlik
Agar __eq__ qayta aniqlangan bo‘lsa:

Python ob'ektlarni qiymatga asoslangan taqqoslashga harakat qiladi.
Agar a == b bo‘lsa, ular bir xil hash qiymatga ega bo‘lishi kerak (aks holda xatoliklar yuzaga keladi).
Agar __hash__ aniqlanmagan bo‘lsa, __eq__ qayta aniqlanganda ob'ektlar hashable bo‘lmaydi.

Qoidalar:
a == b → hash(a) == hash(b) (ular teng bo‘lsa, hashlar ham teng bo‘lishi kerak).
a != b → Hash qiymatlari bir xil yoki farq qilishi mumkin.

Xatolarga misol
Agar __eq__ va __hash__ noto‘g‘ri sozlansa, Python ob'ektlar bilan ishlashda kutilmagan xatoliklar yuzaga keladi.

Xato holat:
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.name == other.name

# __hash__ aniqlanmagan, lekin __eq__ qayta yozilgan
s1 = Student("Ali", 85)
s2 = Student("Ali", 90)

students = {s1: "Excellent"}
print(students[s2])  # KeyError (garchi s1 == s2 bo'lsa-da, hash qiymati mos kelmaydi)

# To‘g‘ri holat:
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.grade == other.grade
        return False

    def __hash__(self):
        return hash((self.name, self.grade))

s1 = Student("Ali", 85)
s2 = Student("Ali", 85)

students = {s1: "Excellent"}
print(students[s2])  # Excellent (hash qiymatlari teng)

"""Xulosa
__eq__:

Ob'ektlarning qiymatga asoslangan tengligini aniqlaydi.
== operatorining xatti-harakatini sozlash uchun ishlatiladi.
__hash__:

Ob'ektni hashable qilish imkonini beradi.
Hash qiymati o‘zgarmas bo‘lishi kerak.
Agar ob'ektlar teng deb topilsa, ularning hash qiymatlari ham teng bo‘lishi kerak.
O'zaro bog'liqlik:

Agar __eq__ qayta aniqlansa va ob'ekt hashable bo'lishi kerak bo'lsa, __hash__ ham qayta aniqlanishi kerak.
Tavsiya: Hash qiymatini hisoblashda tuple yoki boshqa o'zgarmas ma'lumot tuzilmalaridan foydalaning.

Misol: Nima uchun hash kerak?
Faraz qiling, sizda Person degan klass bor, va ushbu klassning obyektlarini Python'ning set yoki dict tuzilmalarida saqlamoqchisiz.

set va dict ishlaganda, obyektlarning qiymatlari o‘zaro taqqoslanadi va ularning hash qiymatlari saqlanadi. Agar hash noto‘g‘ri ishlasa, quyidagidek muammo bo‘ladi:

Klass yaratish:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

"""Obyektlarni solishtirish va hash ning o‘rni:"""

# Person obyektlari
p1 = Person("Ali", 25)
p2 = Person("Ali", 25)
p3 = Person("Vali", 30)

# Obyektlarni taqqoslash
print(p1 == p2)  # True, chunki `name` va `age` teng

# Hash qiymatlarini ko'rish
print(hash(p1))  # Misol: 451234
print(hash(p2))  # Misol: 451234
print(hash(p3))  # Misol: 982342

# `set` da foydalanish
person_set = {p1, p2, p3}
print(len(person_set))  # 2, chunki p1 va p2 bir xil hisoblanadi

# `dict` da foydalanish
person_dict = {p1: "Engineer", p2: "Doctor"}
print(person_dict)  # {p1: 'Engineer'}, chunki p1 va p2 bir xil

"""Agar __hash__ yoʻq boʻlsa yoki notoʻgʻri boʻlsa:
Muammo yuzaga keladi:
set yoki dict notoʻgʻri ishlaydi:
set yoki dict obyektlarni hash qiymati asosida tezlik bilan taqqoslaydi. Agar __hash__ notoʻgʻri ishlatilsa yoki umuman yoʻq boʻlsa, bir xil obyektlar alohida obyektlar sifatida ko‘riladi.
Ishlash tezligi pasayadi:
set yoki dict hash-funksiyadan foydalangani uchun katta maʼlumotlar hajmida juda tez ishlaydi. hash boʻlmasa, faqatgina __eq__ dan foydalaniladi, bu esa sekin ishlaydi.
Ko‘rinishi:
"""

class PersonWithoutHash:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = PersonWithoutHash("Ali", 25)
p2 = PersonWithoutHash("Ali", 25)

# Obyektlarni taqqoslash
print(p1 == p2)  # True, chunki `name` va `age` teng

# `set` da foydalanishga urinish
person_set = {p1, p2}
print(len(person_set))  # 2, chunki `hash` yo‘q va obyektlar alohida hisoblanadi

"""Natija:

Garchi p1 va p2 bir xil bo‘lsa ham, ular set yoki dict ichida alohida obyekt sifatida ko‘riladi.
__hash__ va __eq__ ning muhim bogʻliqligi:
Agar __eq__ o‘zgartirilsa (yaʼni, ikkita obyekt bir xil deb hisoblanadigan shart o‘zgarsa), siz __hash__ funksiyasini ham moslashtirishingiz kerak.
Python'ning qoidasi: Agar obyektlar __eq__ orqali bir xil bo‘lsa, ularning __hash__ qiymatlari ham bir xil bo‘lishi shart.
Nima uchun hash kerak:
Tez ishlash uchun: hash obyektlarning joylashuvini aniqlashda ishlatiladi (masalan, set yoki dict).
Unikal obyektlarni boshqarish uchun: set yoki dict faqat unikal hash qiymatlari bilan ishlaydi.
Xulosa: hash ishlatmasangiz, obyektlaringiz set yoki dict da noto‘g‘ri ishlashi mumkin. Bundan tashqari, obyektlarni boshqarishda va ishlash tezligida sezilarli pasayish kuzatiladi.

__getitem__, __setitem__, va __delitem__ haqida tushuncha
Bu metodlar Python'dagi maxsus metodlardir va ular obyektlar bilan indeksli ishlashni ta'minlash uchun ishlatiladi. Ular aynan indexing va slicing kabi operatsiyalarni qo'llashda yordam beradi. Bu metodlarni moslashtirish orqali o'z sinflaringizda indekslar bilan ishlashni boshqarishingiz mumkin.

__getitem__ — obyektga indeks orqali kirish
Bu metod indeks orqali obyektning qiymatiga kirish imkonini beradi.
Agar siz obyektni indekslashga harakat qilsangiz (masalan, obj[index]), Python avtomatik ravishda __getitem__ metodini chaqiradi.
"""

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

# Misol
my_list = MyList([10, 20, 30, 40])

print(my_list[:])  # 30

"""Izoh:
Bu misolda, my_list[2] chaqirilganda __getitem__ metodiga 2 indeksi beriladi va u items ro'yxatining 2-chi elementini (ya'ni, 30) qaytaradi.
Indekslarni slice bilan ham ishlatish mumkin:
"""

print(my_list[1:3])  # [20, 30]

"""__setitem__ — obyektga indeks orqali qiymat yozish
Bu metod obyektga indeks orqali qiymatni o'rnatish imkonini beradi.
obj[index] = value kabi o'zgartirishda Python avtomatik ravishda __setitem__ metodini chaqiradi.
"""

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value  # Indeksga yangi qiymatni o'rnatish

# Misol
my_list = MyList([10, 20, 30, 40])

my_list[1] = 50  # 1-chi indeksdagi elementni 50 ga o'zgartiradi
print(my_list.items)  # [10, 50, 30, 40]

"""Izoh:
Bu misolda my_list[1] = 50 chaqirilganda __setitem__ metodiga 1-indeks va 50 qiymati beriladi va u items ro'yxatining 1-chi elementini 50 ga o'zgartiradi.
Bu metod indeksni yangilashni yoki to'liq qiymatni o'zgartirishni ta'minlaydi.

__delitem__ — obyektdan indeks orqali elementni o'chirish
Bu metod obyektning elementini indeks orqali o'chirish imkonini beradi.
del obj[index] kabi ishlatilganda Python avtomatik ravishda __delitem__ metodini chaqiradi.
"""

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]  # Indeksni o'chirish

# Misol
my_list = MyList([10, 20, 30, 40])

del my_list[2]  # 2-chi indeksdagi elementni o'chiradi
print(my_list.items)  # [10, 20, 40]

"""__getitem__, __setitem__, va __delitem__ ni ishlatishning maqsadi
Bu metodlar yordamida sinfni indekslash va o'zgartirishni moslashtirish mumkin. Bu metodlar orqali obyektlar ro'yxat, lug'at yoki boshqa ma'lumotlar tuzilmalari kabi ishlashi mumkin.

Indeks orqali o'zgarishlarni qo'llash
Misol uchun, MyDict nomli sinf yaratib, lug'at (dictionary)ga o'xshash tuzilma yaratish mumkin:
"""

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

# Misol
my_dict = MyDict()
my_dict['a'] = 10
my_dict['b'] = 20

print(my_dict['a'])  # 10

del my_dict['a']
print(my_dict.data)  # {'b': 20}