# an appointment should have:
    # disease
    #date
    #pet
    #vet
    #price
class Appointment():
    def __init__(self, disease, date, price, vet = '', pet = ''):
        self. disease = disease
        self.date = date
        self.price = price
        self.vet = vet
        self.pet = pet
        self.list_appointments = []

    def adding_pet(self, pet):
        self.pet = pet

    def adding_vet(self, vet):
        self.vet = vet

    def list_appointments(self, pet):
        self.list_appointments.append(pet)

    def get_vet(self):
        return self.vet

    def get_pet(self):
        return self.pet
    # def get_vet(self):

