# # class Tortburchak:

# #     def __init__(self,x,y):
# #         self.x=x
# #         self.y=y 

# #     def get_parm(self):
# #         return self.x, self.y

    
# #     def yuzi(self):
# #         return f"To'rtburchak yuri: {self.x * self.y}"

# #     def p(self):
# #         return f"To'rtburchak perimetri: {(self.x + self.y)*2 }"

# # obj=Tortburchak(3,4)
# # print(obj.p(),obj.yuzi())


# # class Tortburchak:
# #     MAX=100
# #     MIN=1

# #     @classmethod
# #     def check_type(cls,t):
# #         return type(t) in (int,float)

# #     @classmethod
# #     def check_num(cls,w):
# #         return cls.MIN<w<cls.MAX

# #     def __init__(self,x,y):
# #         self.x=self.y=0
# #         if self.check_num(x) and self.check_num(y):
# #             self.x=x
# #             self.y=y
# #         print(self.raise_num(self.x),self.raise_num(self.y))

# #     def get_parm(self):
# #         return self.x,self.y

# #     def p_answer(self):
# #         return 2*(self.x+self.y)

# #     def s_answer(self):
# #         return self.x*self.y

# #     @staticmethod
# #     def raise_num(m):
# #         return m**2+Tortburchak.MAX

# # obj=Tortburchak(70,4)
# # # print(obj.p_answer(),obj.s_answer())
# # print(obj.get_parm())



# # new,classmethod,staticmethod,obj,self,cls


# # class Bugdoy:

# #     def __init__(self, sort, kg):
# #         self.sort = sort
# #         self.kg = kg

# #     def get_info(self):
# #         return f"Big'doy sorti {self.sort} massasi {self.kg}"


# # qozoq = Bugdoy('qozoq', 70)
# # tosh = Bugdoy('tosh', 50)
# # vodiy=('vodiy',30)

# # listing=[qozoq,tosh,vodiy]
# # print(qozoq)


# # class Tegrmon:
# #     def __init__(self, name):
# #         self.name = name
# #         self.bugdoy = []

# #     def get_name(self):
# #         return self.name

# #     def get_bugdoy(self):
# #         # return self.bugdoy
# #         # for un in self.bugdoy:
# #         #     print(un.get_info())
# #         return [un.get_info() for un in self.bugdoy]

# #     def add_b(self, objs):
# #         for obj in objs:
# #             if isinstance(obj,Bugdoy):
# #                 self.bugdoy.append(obj)
# #             else:
# #                 print('aladama vodiylik')


# # sam = Tegrmon('samandar ota')
# # # sam.add_b(qozoq)
# # # sam.add_b(tosh)
# # sam.add_b(listing)
# # print(sam.get_bugdoy())


# # new,classmethod,staticmethod,obj,self,cls


# class Car:

#     def __init__(self, type, mator):
#         self.type = type
#         self.mator = mator

#     def get_info(self):
#         return f"Mashina turi {self.type}, matori: {self.mator}"


# mers = Car('Tiko', 4)
# bmw = Car('nexia', 5)
# gm =('GM',1)

# listing=[mers,bmw,gm]
# print(bmw)


# class Zavod:
#     def __init__(self, name):
#         self.name = name
#         self.car = []

#     def get_name(self):
#         return self.name

#     def get_car(self):
#         # return self.bugdoy
#         # for un in self.bugdoy:
#         #     print(un.get_info())
#         return [un.get_info() for un in self.car]

#     def add_b(self, objs):
#         for obj in objs:
#             if isinstance(obj,Car):
#                 self.car.append(obj)
#             else:
#                 print('Teppa GM')


# sam = Zavod('German moshinalari')
# # sam.add_b(qozoq)
# # sam.add_b(tosh)
# sam.add_b(listing)
# print(sam.get_car())


# class Person:

#     def __init__(self,name,job):
#         self.ism=name
#         self.job=job

#     def upper(self):
#         return self.ism.upper()

    
#     # def nomsiz(self):

# b=Person('ozodbek','frontend')
# v=Person('as','sa')
# print(b.upper())
# print(v.job)


# class Car:

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year


#     def cars(self):
#         print(f"Car brand: {self.brand}, model: {self.model},   year: {self.year}")

#     # def models(self):
#     #     print(f"only car moedl{ self.model} ")

#     # def years(self):
#     #     m = self.year + 20
#     #     return print(m)


#     def update_info(self, new_year):
#         self.year = new_year

#     def start_engine(self):
#         print(f"{self.brand} {self.model}'s engine is started")

# car = Car("BMD", "M5", 2025)
# car2 = Car("Mers", "MayBach", 2022)
# car.cars()

# car.update_info(2024)

# car.cars()
# car2.start_engine()
# car.start_engine()

# class Car:

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def info(self):
#         print(f"Car brand is {self.brand}, model: {self.model}, published: {self.year}")


# class SportsCar(Car):
#     def __init__(self, brand, model, year, top_speed):
#         super().__init__(brand, model, year)
#         self.top_speed = top_speed

#     def speed(self):
#         print(f"This {self.brand} {self.model} can reach a top speed of {self.top_speed} km/h!")

# sc = SportsCar("Ferrari", "F8", 2023, 340)
# sc.info()    # inherited from Car
# sc.speed()   # from SportsCar

class User:
    HARF = "qwertyuiopasdfghjklzxcvbnm"
    HARF_U = HARF.upper() + HARF

    def __init__(self, full_name, age, weight, ps):
        self.verify_full_name(full_name)
        self.verify_age(age)
        self.verify_weight(weight)
        self.verify_ps(ps)
        self.__fullname = full_name
        self.__age = age
        self.__weight = weight
        self.__ps = ps



    @classmethod
    def verify_full_name(cls, full_name):
        if type(full_name) != str:
            raise TypeError("siz string malumot kiriting")
        name_list = full_name.split(' ')
        if len(name_list) != 3:
            raise ValueError("siz ism fam ochistva yozishiz kerak")
        check_alpha = cls.HARF + cls.HARF_U
        # print(check_alpha)
        for name in name_list:
            for n in name:
                if not n in check_alpha:
                    raise ValueError("szi faqat lotin harflarida yozing")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int:
            raise TypeError("faqat sonda yozing")
        if not 18 <= age <= 120:
            raise ValueError("siz 18 va 120 oralig'ida bolishiz kerak")

    @classmethod
    def verify_weight(cls, weight):
        if not type(weight) in (int, float):
            raise TypeError(" Vaznni sonda yoki qoldiqli yozing")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Faqat stringda yozing")
        ps_list = ps.split(' ')
        print(ps_list)
        if len(ps_list) != 2:
            raise ValueError("siz seria  raqamni yoznig AA XXXXXXX")
        check_alpha = cls.HARF_U
        m = ps_list[0].strip(check_alpha)

        if len(m) != 0 or not ps_list[1].isdigit() or len(ps_list[1]) != 7:
            raise ValueError("boshqatan yoz")

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self,m):
        self.verify_full_name(m)
        self.__fullname=m



    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,x):
        self.verify_age(x)
        self.__age=x

obj = User("Samandar botirjonov Bahromovich", 20, 85, "AV 1134567")
obj.fullname="Ali Vali Sobir"
obj.age=25
print(obj.__dict__)
