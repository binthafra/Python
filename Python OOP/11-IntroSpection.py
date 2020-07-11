class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged In")


class Wizerd(User):
    def __init__(self, name, power, email):
        # super class
        # User.__init__(self, email)
        super().__init__(email)  # super class another way

        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


# IntroSpection
wizerd1 = Wizerd("marlin", 50, "marline@gmail.com")
print(dir(wizerd1))  # dir->show thr methods it can access
print(wizerd1.sign_in())
