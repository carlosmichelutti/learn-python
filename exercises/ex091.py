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

    def __str__(self):
        return f'Name: {self.name} | Artist: {self.artist} | Duration: {self.duration}'

musica1 = Music(name='Lose Yourself', artist='Eminem', duration=320)
musica2 = Music(name='Black or white', artist='Michael Jackson', duration=255)
musica3 = Music(name='Many men', artist='50 cent', duration=298)

print(musica1, musica2, musica3, sep='\n')
