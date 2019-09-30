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