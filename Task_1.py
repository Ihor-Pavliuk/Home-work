# я суто не бачу сенсу, записувати сюди всілякі різні методи, бо їх можно зробити дуже багато як і кількість атрибутів...
class Person():
    def __init__(self, first_name, last_name, age): #загальний метод
        self.first_name = first_name # загальний атрибут
        self.last_name = last_name # загальний атрибут
        self.age = age # загальний атрибут

class Student(Person):
    #def __init__(self, first_name, last_name, age): #особистий метод
        #super().__init__(first_name, last_name, age)
    pass    

        
class Teacher(Person):
    def __init__(self, first_name, last_name, age, salary): #особистий метод
        super().__init__(first_name, last_name, age)
        self.salary = salary #особистий атрибут

y = Student ("c", "d", 101)
x = Teacher ("a", "b", 20, 2000000)    
print(x.age)
print(x.first_name)
print(x.last_name)
print(x.salary)
print(y.age)

