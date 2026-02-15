from dataclasses import dataclass

@dataclass
class Avaliation:
    grade: float

class Restaurant:
    def __init__(
        self: object, 
        name: str,
        category: str,
        active: bool = False
    ) -> None:

        self.name: str = name
        self.category: str = category
        self.active: bool = active
        self._avaliations: list[Avaliation] = []

    def __str__(self):
        average = f'{self.average_grade:.2f}' if self._avaliations else "N/A"
        return (
            f'Name: {self.name} | '
            f'Category: {self.category} | '
            f'Average Grade: {average} | '
            f'Active: {self.active}'
        )

    def avaliate(self: object, grade: float) -> None:
        if grade < 0 or grade > 10:
            print(f'Grade must be between 0 and 10. The grade {grade} is not valid.')
            return
        avaliation = Avaliation(grade=grade)
        self._avaliations.append(avaliation)
        return

    @property
    def average_grade(self: object) -> float:
        if not self._avaliations:
            return 0.0
        return sum(avaliation.grade for avaliation in self._avaliations) / len(self._avaliations)

restaurant1 = Restaurant(name='Pasta Palace', category='Italian')
restaurant1.avaliate(grade=8.5)
restaurant1.avaliate(grade=9.0)
restaurant2 = Restaurant(name='Sushi Central', category='Japanese')
restaurant2.avaliate(grade=9.5)
restaurant2.avaliate(grade=9.0)
restaurant3 = Restaurant(name='Burger Barn', category='American')
restaurant3.avaliate(grade=5)
restaurant3.avaliate(grade=6)

print('', restaurant1, restaurant2, restaurant3, sep='\n')
