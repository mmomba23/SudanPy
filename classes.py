class Cat:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        print(f"This cat is called {self.name}")
    def meow(self):
        print(f"{self.name} shouting: Meow!")
    def eat(self, food):
        print(f"{self.name}: Meow meow! I like {food} very much!")
kittie=Cat("Smokey")
kittie.meow()
kittie.eat("mouse")
kittie.__str__()
