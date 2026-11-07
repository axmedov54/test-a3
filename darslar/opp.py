

class Person():
    ism = 'Mustafo'
    familiya = 'Polvanazirov'
    yosh = 17
print(Person.ism)

class Person():
    def __init__(self,ism,familiya,yosh,ish_joyi):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.ish_joyi = ish_joyi
    def __str__(self):
        return f"ismi--> {self.ism}\nfamiliyasi--> {self.familiya}\nyoshi--> {self.yosh}\nish joyi--> {self.ish_joyi}"
        
p1 = Person('Mustafo','Polvanazirov',17,'ishsiz')      
p2 = Person('Azizbek','Atobayev',13,'ishsiz')      
print(p2)

      














