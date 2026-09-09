#--- BEFORE RELATIONSHIP ---
class Calculator:
    def __init__(self, color, lowbattery, price):
        self.attribute1 = color
        self.attribute2 = lowbattery
        self.__private_attribute = price
        self.pencilC = None

    def color(self, color_ref):
        self.attribute1 = color_ref

    def price(self, price_ref):
        self.__private_attribute = price_ref

    def lowbattery(self, low_ref):
        self.attribute2 = low_ref
      
class PencilCase:
    def __init__(self, size, broken, price):
        self.attribute1 = size
        self.attribute2 = broken
        self.__private_attribute = price
        self.calc = None

    def size(self, size_ref):
        self.attribute1 = size_ref

    def price(self, price_ref):
        self.__private_attribute = price_ref

    def broken(self, broken_ref):
        self.attribute2 = broken_ref

#--- BUILDING RELATIONSHIP ---
calc = Calculator("red", True, 1200)
pencilC = PencilCase(20, False, 32)

calc.pencilC = pencilC
pencilC.calc = calc

#--- AFTER RELATIONSHIP ---
print(f"Size of pencil case accessed through calculator: {calc.pencilC.attribute1}")
print(f"Low battery variable of calculator accessed through pencil case: {pencilC.calc.attribute2}")

#Related object(s):
# Pencil Case and Calculator
