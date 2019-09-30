class Human():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email




class Client(Human):
    def __init__(self, payment_details, name, phone, email, pet = ''):
        super().__init__(name, phone, email)
        self.payment_details = payment_details
        self.pet = pet

    def identify_name(self):
        return self.name




class Veterinarian(Human):
    def __init__(self,  name, phone, email, specialisation):
        super().__init__(name, phone, email)
        self.specialisation = specialisation

    def identify_name(self):
        return self.name
