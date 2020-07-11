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

    def check_arrows(self):
        print(f" {self.num_arrows} remaining")

    def run(self):
        print("run fast")


class HybridBorg(Wizerd, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizerd.__init__(self, name, power)


hb1 = HybridBorg("borgeie", 50, 70)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
