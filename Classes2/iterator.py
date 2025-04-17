class RGB:
    def __init__(self) -> None:
        self.cores = ['red', 'green', 'blue'][::-1]
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

cores = RGB()
print(next(cores))
print(next(cores))
print(next(cores))

try:
    print(next(cores))
except:
    print('FIM DOS NÚMEROS')

for cor in RGB():
    print(cor)