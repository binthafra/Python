class User():
    def sign_in(self):
        print("logged In")


class Wizerd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows of {self.num_arrows}")


wizerd1 = Wizerd("marlin", 50)
archer1 = Archer("Robin", 100)
wizerd1.attack()
