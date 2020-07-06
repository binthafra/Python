class PlayerCharacter:

    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def ading_things(cls, num1, num2):
        return cls("teddy", num1+num2)

    @staticmethod
    def ading_things(num1, num2):
        return num1+num2

# player1 = PlayerCharacter('Afra', 10)


player3 = PlayerCharacter.ading_things(2, 3)
print(player3.age)
print(player3.name)
