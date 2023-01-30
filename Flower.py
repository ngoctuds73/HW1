class Flower:

    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def water(self, water_requirements: int):
        if water_requirements >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return F"{self.name} not happy"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())