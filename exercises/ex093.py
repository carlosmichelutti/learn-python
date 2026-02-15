class Restaurant:
    def __init__(
        self: object, 
        name: str,
        category: str,
        rating: float,
        active: bool = False
    ) -> None:

        self.name: str = name
        self.category: str = category
        self.rating: float = rating
        self.active: bool = active

    def __str__(self):
        return f'Name: {self.name} | Category: {self.category} | Rating: {self.rating} | Active: {self.active}'

restaurant1 = Restaurant(name='Pasta Palace', category='Italian', rating=4.5)
restaurant2 = Restaurant(name='Sushi Central', category='Japanese', rating=4.8)
restaurant3 = Restaurant(name='Burger Barn', category='American', rating=4.2)

print(restaurant1, restaurant2, restaurant3, sep='\n')
