class Calculator:
    def __init__(self, color, lowbattery, price):
        self.attribute1 = color
        self.attribute2 = lowbattery
        self.__private_attribute = price

    def turnon(self):
        return "Turned on calculator!"

    def calculate(self, num1, num2, operator):
        if operator == "+":
            print(f"Sum is {num1 + num2}")
        elif operator == "-":
            print(f"Difference is {num1 - num2}")
        elif operator == "*":
            print(f"Product is {num1 * num2}")
        elif operator == "/":
            print(f"Quotient is {num1 / num2}")
        else:
            print("Invalid operator")

    def repaint(self, color):
        print("Repainted calculator!")
        self.attribute1 = color

    def readprice(self):
        print(f"Price of the calculator is {self.__private_attribute}$")


calc1 = Calculator("red", True, 3000)
calc2 = Calculator("green", False, 1200)

print(f"{calc1.turnon()}")
calc1.repaint("blue")
calc2.readprice()
