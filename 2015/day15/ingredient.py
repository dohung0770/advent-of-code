class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        
    def __repr__(self) -> str:
        return f'Ingredient (name={self.name}, capacity={self.capacity}, durability={self.durability}, flavor={self.flavor}, texture={self.texture}, calories={self.calories})'
    