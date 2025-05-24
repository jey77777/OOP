class Employee:
    def __init__(self,name, parol, exp):        
        self.name = name
        self.parol = parol
        self.exp = exp 

    def __delattr__(self, name):
        print(name)
        if name == 'parol':
            print("Buni o'chirolmaysiz")
            return None
        super().__delattr__(name)

    


emp = Employee("sobir", 1234, 3)
print(emp)
del emp.parol
print(emp.parol)

