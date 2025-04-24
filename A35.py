# 35. Demonstrate inheritance with Animal and Dog classes.
class Animal:
    def __init__(self,name):
        self.name=name
    def breed_name(self):
        print("not define ")
    
class Dog (Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def breed_name(self):
        print(self.name, self.breed)

Dog("rocky","germanShp").breed_name()