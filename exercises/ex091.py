from dataclasses import dataclass

@dataclass
class Avaliation:
    grade: float

class Music:
    def __init__(
        self: object,
        name: str,
        artist: str,
        duration: int
    ) -> None:

        self.name: str = name
        self.artist: str = artist
        self.duration: int = duration
        self._avaliations: list[Avaliation] = []

    def __str__(self):
        average = f'{self.average_grade:.2f}' if self._avaliations else "N/A"
        return (
            f'Name: {self.name} | '
            f'Artist: {self.artist} | '
            f'Duration: {self.duration}s | '
            f'Average Grade: {average}'
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

musica1 = Music(name='Lose Yourself', artist='Eminem', duration=320)
musica1.avaliate(grade=11)
musica1.avaliate(grade=9.5)
musica1.avaliate(grade=8.0)
musica2 = Music(name='Black or white', artist='Michael Jackson', duration=255)
musica2.avaliate(grade=-1)
musica2.avaliate(grade=9.0)
musica2.avaliate(grade=10)
musica3 = Music(name='Many men', artist='50 cent', duration=298)
musica3.avaliate(grade=8.5)
musica3.avaliate(grade=7.0)
musica3.avaliate(grade=9.0)

print('', musica1, musica2, musica3, sep='\n')
