class AuntSue:
    def __init__(
        self,
        ordinal: int,
        children: int = None,
        cats: int = None,
        # dog breeds
        samoyeds: int = None,
        pomeranians: int = None,
        akitas: int = None,
        vizslas: int = None,
        goldfish: int = None,
        trees: int = None,
        cars: int = None,
        perfumes: int = None
    ):
        self.ordinal = ordinal
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes
    
    def __repr__(self) -> str:
        return f'Aunt Sue (#{self.ordinal}, children={self.children}, cats={self.cats}, dogs: (samoyeds={self.samoyeds}, pomeranians={self.pomeranians}, akitas={self.akitas}, vizslas={self.vizslas}), goldfish={self.goldfish}, trees={self.trees}, cars={self.cars}, perfumes={self.perfumes})'
    