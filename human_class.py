class Human():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email




class Client(Human):
    def __init__(self, payment_details, name, phone, email):
        super().__init__(name, phone, email)
        self.payment_details = payment_details



class Veterinarian(Human):
    def __init__(self, specialisation, name, phone, email):
        super().__init__(name, phone, email)
        self.specialisation = specialisation