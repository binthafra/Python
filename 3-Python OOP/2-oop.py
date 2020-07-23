class PlayerCharacter:
    # Class object Attribute -> Static
    membership = True

    def __init__(self, name="anonymous", age=0):
        # if(PlayerCharacter.membership):
        if(age > 18):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter('Afra', 10)


# print(player1.name)
# print(player2.membership)
print(player1.shout())
