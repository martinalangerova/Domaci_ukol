
import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name  # Název katastru/obce
        self.locality_coefficient = locality_coefficient  # Místní koeficient

    def __str__(self):
        return f"Lokalita {self.name} s koeficientem {self.locality_coefficient}."
    
class Property:
    def __init__(self, locality):
        if not isinstance(locality, Locality):  # Kontrola, že locality je objekt typu Locality
            raise ValueError("locality musí být objekt třídy Locality.")
        self.locality = locality  # Lokalita, kde se nemovitost nachází
      
    def __str__(self):
        return f"Nemovitost se nachází v: {self.locality}"

# Příklad použití:
locality = Locality(name="Praha", locality_coefficient=1.5)
# print(locality)
property1 = Property(locality=locality)
print(property1)

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    ESTATE_COEFFICIENTS = {
        "land": 0.85,
        "building site": 9,
        "forrest": 0.35,
        "garden": 2
    }
    def calculate_tax(self):
        # if self.estate_type not in self.ESTATE_COEFFICIENTS:
        #     raise ValueError("Neplatný typ pozemku")
        tax = self.area * self.ESTATE_COEFFICIENTS[self.estate_type] * self.locality.locality_coefficient
        return math.ceil(tax)

# Příklad použití
locality1 = Locality("Praha", 1.5)
estate1 = Estate(locality1, "building site", 500)
print("Výše daně:", estate1.calculate_tax())






