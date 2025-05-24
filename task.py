# class Market: 
#     def __init__(self, partiya,*products):
#         self.partiya = partiya
#         self.products = list(products)

#     def get_info(self):
#         return self.partiya, self.products
    
#     def get_item(self):
#         for i, v in enumerate(self.products):
#             if v == 'samsung':
#                 return i
        
#     def _getitem__(self, item):
#         return self.product[item]


# yuk = Market("Partiya 1", 'apple', 'mi', 'samsung', 'honor')

# print(yuk.get_info())

# print(yuk.get_item())













class Book:
    def __init__(self,*qahramonlar, **asarMuallif ):
        self.qahramonlar = qahramonlar
        self.asarMuallif = asarMuallif
        
    def get_info(self):
        return self.qahramonlar, self.asarMuallif
    
    def __getitem__(self,item):
        if isinstance(item,int):
            return self.qahramonlar
        else:
            return self.asarMuallif.get(item, "Bunday malumot yoq")



info = Book('Petrov', 'Graf', 'John', urush= "tolstoy", montekristo= "duyma", inovatisya= "professorlar")
        
print(info['montekristo'])

# print(info.get_info())




class Group:
    def __init__(self,title,*args):
        self.title=title
        self.members=list(args)


    def get_info(self):
        return self.title,self.members

    def __getitem__(self, index):
        return self.members[index]
    def __setitem__(self, index, value):
        self.members[index]=value

    def __delitem__(self, index):
        del self.members[index]
#
# gr=Group('back-end','vali','jobir','sobir')
# gr[1]='bobur'
# del gr[1]
# print(gr[:])
# print(gr.get_info())


# Dokon
# partiya
# products=[]
#
# product tarkibida sumsung bo'lsa
# shuni index topib bering
# enmurate


class Market:
    def __init__(self,partiya,*args,**kwargs):
        self.prtiya=partiya
        self.product=list(args)
        self.narx=kwargs

    def get_index(self):
        for i,v in enumerate(self.product):
            if v=='sumsung':
                return i

    def __getitem__(self, item):
        return self.narx[item]

    def __setitem__(self, index, value):
        self.narx[index]=value

    def __delitem__(self, index):
        del self.narx[index]

    def get_narx(self):
        return self.narx



new=Market('ikkinchi','kitob','sumsung','onix','ruchka',non=200,kitob=3000,list=400,lampochka=500)
# print(new.get_index())
# t=new.get_index()
# print(new[t])
# print(new.get_narx())
# new['non']=9000
# del new['non']
# print(new.get('non','bunaqasi yoq'))

# book
# asar:mualif
# qahramonlar list

class Library:
    def __init__(self,*hero,**poem):
        self.hero=list(hero)
        self.poem=poem

    def __getitem__(self, item):
        if isinstance(item,int):
            return self.hero[item]
        else:
            return self.poem.get(item,"Bunday malumot yo'q")

p=Library('lutzer','pauk','alpomish',men='bryon',urush='tolstoy')
print(p['men'])
