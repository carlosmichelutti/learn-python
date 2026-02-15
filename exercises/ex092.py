class Car:
    def __init__(
        self: object,
        model: str,
        year: int,
        color: str
    ) -> None:

        self.model: str = model
        self.year: int = year
        self.color: str = color

    def __str__(self):
        return f'Model: {self.model} | Year: {self.year} | Color: {self.color}'

car1 = Car(model='Toyota Camry', year=2020, color='Red')
car2 = Car(model='Honda Accord', year=2019, color='Blue')
car3 = Car(model='Ford Mustang', year=2021, color='Black')

print(car1, car2, car3, sep='\n')
