# 1. Transport vositalari tizimi
# Shart: Transport vositalari uchun Vehicle nomli asosiy klass yarating. Undan voris oluvchi Car, Bicycle, va Truck klasslarini hosil qiling.
# Vehicle klassi umumiy atributlarga ega bo‘lsin: name, speed.
# Car, Bicycle, Truck klasslari har biri o‘ziga xos metodlarga ega bo‘lsin (honk(), load_cargo(), pedal()).
# Ma’lumot: Masalan, Car obyektida honk() metodidan foydalansa, "Bip-bip!" degan natija chiqishi kerak.

class Vehicle:
    def __init__(self,name, speed):
        self.name = name
        self.speed = speed

    def get_info(self):
        return self.name, self.speed


class Car(Vehicle):
    def __init__(self, name, speed, honk):
        super().__init__(name, speed)
        self.honk = honk

    def honks(self):
        return self.name, self.speed, self.honk
    
class Bicycle(Vehicle):

    def __init__(self, name, speed, pedal):
        super().__init__(name, speed)
        self.pedal = pedal

    def pedals(self):
        return self.name, self.speed, self.pedal
    
class Truck(Vehicle):

    def __init__(self, name, speed, load_cargo):
        super().__init__(name, speed)
        self.load_cargo = load_cargo

    def loads(self):
        return self.name, self.speed, self.load_cargo
    
veh = Vehicle("Mers", "300")
car = Car("BMW", "350", "bip-bip!")
truck = Truck('Shackman','200','Load')
print(veh.get_info())
print(car.honks())
print(truck.loads())


# 2. Hayvonot bog‘i tizimi
# Shart: Hayvonlarni ifodalovchi Animal nomli asosiy klass yarating. Undan voris oluvchi Lion, Eagle, va Shark klasslarini hosil qiling.
# Animal klassida umumiy metodlar bo‘lsin (make_sound()).
# Lion, Eagle, Shark klasslari make_sound() metodini o‘ziga xos tarzda o‘zgartirsin (roar(), screech(), splash()).
# Ma’lumot: Masalan, Lion obyektida make_sound() metodini chaqirsak, natija "Roar!" bo‘lishi kerak.

class Animal:
    def make_sound(self):
        print("Hayvonlar ovozi:")

class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Eagle(Animal):
    def make_sound(self):
        print("Screech")

class Shark(Animal):
    def make_sound(self):
        print("Splash")

lion = Lion()
eagle = Eagle()
shark = Shark()

lion.make_sound()
eagle.make_sound()
shark.make_sound()

# 3. Ishchilar boshqaruvi tizimi
# Shart: Ishchilarni ifodalovchi Employee nomli asosiy klass yarating. Undan voris oluvchi Manager, Developer, va Designer klasslarini hosil qiling.
# Employee klassida umumiy metod bo‘lsin: get_salary().
# Manager, Developer, Designer klasslari har biri o‘zining alohida maosh hisoblash usuliga ega bo‘lsin.
# Ma’lumot: Masalan, Developer klassining get_salary() metodi maoshni hourly_rate * hours_worked shaklida qaytarsin.

class Employee:
    def get_salary():
        raise NotImplementedError("Bu method voris classlarda aniqlanishi kerak")
    
class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus
    
class Developer(Employee):
    def __init__(self,hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self):
        return self.hourly_rate * self.hours_worked
    
class Designer(Employee):
    def __init__(self, project_count, per_project):
        self.project_count = project_count
        self.per_project = per_project

    def get_salary(self):
        return self.project_count * self.per_project
    
manager = Manager(base_salary=5000, bonus=1500)
developer = Developer(hourly_rate=50, hours_worked=160)
designer = Designer(project_count=3, per_project=800)

print("Manager oyligi:", manager.get_salary())     
print("Developer maoshi:", developer.get_salary()) 
print("Designer ishbayi:", designer.get_salary())

# 4. Onlayn do‘kon mahsulotlari
# Shart: Product nomli asosiy klass yarating. Undan voris oluvchi Electronics, Clothing, va Food klasslarini hosil qiling.
# Product klassi umumiy atributlarga ega bo‘lsin: name, price.
# Electronics, Clothing, Food klasslari o‘ziga xos metodlarga ega bo‘lsin (apply_discount(), check_expiry()).
# Ma’lumot: Masalan, Electronics klassida apply_discount() metodi mahsulot narxidan 10% chegirma hisoblasin.

class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    
class Electronics(Product):
    def apply_discount(self):
        discount = self.price * 0.9 
        return discount
    
class Clothing(Product):
    def apply_discount(self, percent):
        discount_price = self.price * (1 - percent / 100)
        return discount_price

class Food(Product):
    def __init__(self, name, price, expiry):
        super().__init__(name, price)
        self.expiry = expiry

    def check_expiry(self):
        date = "14.05.2025"
        return date == self.expiry


laptop = Electronics("Laptop", 1500)
print("Chegirma:", laptop.apply_discount())  

shirt = Clothing("T-shirt", 50)
print("Chegirma:", shirt.apply_discount(20)) 

milk = Food("Milk", 2.5, ("14.05.2025"))
print("Yaroqlilik muddati tugagan:", milk.check_expiry())

# 5. Bank hisoblari tizimi
# Shart: BankAccount nomli asosiy klass yarating. Undan voris oluvchi SavingsAccount va CheckingAccount klasslarini hosil qiling.
# BankAccount klassi umumiy atributlarga ega bo‘lsin: balance.
# SavingsAccount, CheckingAccount klasslari withdraw() metodini har xil ishlasin (cheklovlar bilan).
# Ma’lumot: Masalan, SavingsAccount klassida withdraw() metodi faqat hisobda yetarlicha mablag‘ bo‘lsa ishlasin.


class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi, Qoldiq balans {self.balance}")
        else:
            print("Yetarlicha pul yo'q")

class CheckingAccount(BankAccount):
    def __init__(self, balance, income):
        super().__init__(balance)
        self.income = income

    def deposit(self, deposit):
        self.balance += deposit
        print(f"xisobingiz {deposit} so'mga to'ldirildi. Xisob: {self.balance}")


savings = SavingsAccount(1000)
savings.withdraw(500)   
# savings.withdraw(600)   

checking = CheckingAccount(500,500)
checking.deposit(500)  
