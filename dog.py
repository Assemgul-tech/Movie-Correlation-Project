class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"Собачка по имени {self.name} сейчас сидит")

    def roll_over(self):
        print(f"Собачка по имени {self.name} сейчас перекатывается")

    def setName(self,upd_name):
        self.name = upd_name

    def setAge(self,upd_age):
        if upd_age >= self.age:
           self.age = upd_age 
        else:
            print("Нельзя уменьшать возраст")

    def increment_age(self, inc_age):
         self.age += inc_age