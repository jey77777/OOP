# # menu
# # taomlar class title,price
# # osh 20
# # somsa 800
# # qounatity
# # 1,2
# class Menu:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price

#     def get(self):
#         return f"{self.title} narxi {self.price}"


# menu=[]
# while True:
#     print("""
#     1 menu yaratish
#     2 menudan zakaz berish
#     3 exit
#     """)
#     user=int(input("tanlang"))
#     if user==1:
#         title=input('taomni nomi:')
#         price=int(input(f"{title}ning narxi:"))
#         obj=Menu(title,price)
#         menu.append(obj)
#         print(f"{title} menuga qoshildi")
#     elif user==2:
#         view=[m.get() for m in menu]  # [osh,somsa]
#         for i,t in enumerate(view,start=1):
#             print(i,t)
#         order=input('tomlarni raqamini tanlang:')
#         order_list=order.split(',') #
#         narxlar=[]
#         for o in order_list:
#             for i,t in enumerate(menu,start=1):
#                 if int(o)==i:
#                     narxlar.append(t.price)

#         print(sum(narxlar))





class Kiyim:
    def __init__(self):
        return "Aniqlanmagan"
    
class Erkak(Kiyim):
    def __init__(self, mato, rang):
        super().__init__()
        self.mato = mato
        self.rang = rang

    def shim(self):
        return f"Shim {self.mato} matodan, {self.rang} rangda tayyorlanga"
    


class Ayol(Kiyim):
    def __init__(self, mato, rang):
        super().__init__()
        self.mato = mato
        self.rang = rang

    def koyle(self):
        return f"Ko'yle {self.mato} matodan, {self.rang} rangda tayyorlanga"
    

