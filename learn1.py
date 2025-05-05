class Employee:
    def __init__(self,name,proficiency,experience):
        self.name = name
        self.proficiency = proficiency
        self.experience = experience

    def get_info(self):
        return f"Ismi: {self.name}, Kasbi: {self.proficiency}, Tajribasi: {self.experience}"
        

staff = Employee('Obid', 'Trader', 3)
staff2 = Employee('Guzal', 'Model', 1)

# print(staff.__dict__)
# print(staff2.__dict__)

print(staff.get_info())
print(staff2.get_info())