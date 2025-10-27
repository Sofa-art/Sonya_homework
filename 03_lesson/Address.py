class Address:
    def __init__(self, index, city, street, apartament, number ):
        self.index = index
        self.city = city
        self.street = street
        self.apartament = apartament
        self.number = number

    def __str__ (self):
        return f"{self.index}, {self.city}, {self.street} , {self.apartament} , {self.number}"
        