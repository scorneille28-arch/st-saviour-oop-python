
class Flower:
    def __init__(self, name: str, color: str, petals: int, blooming: bool):
        self.name = name 
        self.color = color
        self.petals = petals
        self.blooming = blooming

    def bloom(self) -> str:
        return f'the {self.color} {self.name} blooms with {self.petals} petals!'
    
if __name__ == '__main__':
    # print('new dawn, new day')
    tulip = Flower('Tulip', 'pink', 10, True)
    print(tulip.bloom())

    lily = Flower('lily','yellow', 6 , True)
    print(lily.bloom())