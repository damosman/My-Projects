class Person:
    def talk(self):
        print("Hello")
    def compliments(self):
        print("You look good today")

persona = Person()

persona.talk()
persona.compliments()

persona.num = 419
print(persona.num)