#--- BEFORE RELATIONSHIP ---
class Calculator:
    def __init__(self, color, lowbattery, price):
        self.attribute1 = color
        self.attribute2 = lowbattery
        self.__private_attribute = price
        self.pencilC = None

    def display_size(self, att):
        print(f"Size of pencil case accessed through calculator: {att}")
      
class PencilCase:
    def __init__(self, size, broken, price):
        self.attribute1 = size
        self.attribute2 = broken
        self.__private_attribute = price
        self.calc = None

    def display_lowbattery(self, att):
        print(f"Low battery variable of calculator accessed through pencil case: {att}")

#--- BUILDING RELATIONSHIP ---
calc = Calculator("red", True, 1200)
pencilC = PencilCase(20, False, 32)

calc.pencilC = pencilC
pencilC.calc = calc

#--- AFTER RELATIONSHIP ---
pencilC.display_lowbattery(pencilC.calc.attribute2)
calc.display_size(calc.pencilC.attribute1)

#Related object(s):
# Pencil Case and Calculator
