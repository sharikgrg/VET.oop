# an pet should have:
    # name
    #breed
    #species
    #owner
class Pet():
    def __init__(self, name, breed, species, owner = ''):
        self.name = name
        self.breed = breed
        self.species = species
        self.owner = owner
