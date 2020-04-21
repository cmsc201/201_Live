class Dog:
    def __init__(self, name, age=0, color="Default",
                 weight=0, breed="Mutt", fluffiness=0.6,
                 times_barked=0):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
        self.breed = breed
        self.fluffiness = fluffiness
        self.cuteness = 0.5
        self.things_eaten = []
        self.times_barked = times_barked

    def bark(self):
        self.times_barked += 1
        print(self.name, "says: ", end="")
        for i in range(self.times_barked):
            print("BARK!", end="")
        print("")

    def sleep(self):
        print(self.name, "needs to slep.  zzzzz")

    def eat(self, food):
        self.things_eaten.append(food)

    def diet(self):
        print(self.name, "has eaten", self.things_eaten)


class Pack:
    def __init__(self, name):
        self.name = name
        self.doggos = []

    def join(self, dog):
        self.doggos.append(dog)

    def howl(self):
        print("Let's do it", self.name,"!")
        for dog in self.doggos:
            dog.bark()


if __name__ == '__main__':
    charlie = Dog("Chuckedero", 9.0, "white/brown", 9.0, "chiweenie mix", 0.1)
    charlie.bark()
    charlie.bark()
    charlie.bark()

    spot = Dog("Spot", 9.0, "white/black", 9.0, "doggo", 0.1)
    spot.bark()

    governor = Dog("Governor", 5)
    print(governor.age)
    jeff = Dog("Jeff")


    fang_squad = Pack("Fang squad")
    print(fang_squad.join)
    fang_squad.join(spot)
    fang_squad.join(charlie)
    fang_squad.howl()
