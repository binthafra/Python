class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged In")


class Wizerd(User):
    def __init__(self, name, power, email):
        # super class
        #User.__init__(self, email)
        super().__init__(email)  # super class another way

        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


wizerd1 = Wizerd("marlin", 50, "marline@gmail.com")
print(wizerd1.email)
print(wizerd1.sign_in())
