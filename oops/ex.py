# print("hello world")

class phone():
    def __init__(self, brand, color, type):
        self.brand = brand
        self.color = color
        self.type = type
    
    def display(self):
        return {"brand" : self.brand,
                "color" : self.color,
                "type" : self.type}

phone1 = phone('Iqoo', 'Black', 'Android')

# phone1.brand = 'Samsung'

print(phone1.display())

