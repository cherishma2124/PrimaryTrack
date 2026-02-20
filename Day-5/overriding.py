class Animal:
    def sound(self):
        print("Random Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class cat(Animal):
    def sound(self):
        print("Meow")

d1 = Dog()
d1.sound()
c1 = cat()
c1.sound()
