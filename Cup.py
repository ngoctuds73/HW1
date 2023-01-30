class Cup:

    def __init__(self, size: int, quantity: int):
        self.size= int(size)
        self.quantity = int(quantity)

    def fill(self, amount_to_fill: int):
        if self.quantity + amount_to_fill <= self.size:
            self.quantity += amount_to_fill

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())