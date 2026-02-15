from time import sleep

class Car:
    def __init__(
        self: object,
        model: str,
        year: int,
        color: str,
        maximum_speed: int = 120,
        initial_velocity: int = 0
    ) -> None:

        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.maximum_speed: int = maximum_speed
        self.initial_velocity: int = initial_velocity

    def __str__(self):
        return f'Model: {self.model} | Year: {self.year} | Color: {self.color}'

    def accelerate(self: object, acceleration: int) -> None:

        while not self.initial_velocity >= self.maximum_speed:
            print(f'{self.model} accelerating: {self.initial_velocity} km/h')
            self.initial_velocity += acceleration
            sleep(0.5)
        
        print(f'{self.model} reached maximum speed: {self.initial_velocity} km/h')

    def brake(self: object, deceleration: int) -> None:

        while not self.initial_velocity <= 0:
            print(f'{self.model} braking: {self.initial_velocity} km/h')
            self.initial_velocity -= deceleration
            sleep(0.5)
        
        print(f'{self.model} stopped.')

car1 = Car(model='Toyota Camry', year=2020, color='Red', maximum_speed=150)
car2 = Car(model='Honda Accord', year=2019, color='Blue', maximum_speed=140)
car3 = Car(model='Ford Mustang', year=2021, color='Black', maximum_speed=200)
car3.accelerate(acceleration=10)
car3.brake(deceleration=5)

print(car1, car2, car3, sep='\n')
