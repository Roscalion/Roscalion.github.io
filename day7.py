class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'covers body'
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise

dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


class Dog(Animal):
    name = 'Campy'

campy = Dog()
campy.color = 'white'
campy.name = 'Campy Doge'

#It takes everything from the class Animal() class.

    # def get_color(self):
    #    return self.color

obj = Dog()
obj == self
obj.color = 'white'
obj.get_color()
