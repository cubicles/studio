class HousePet:
    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age

def future_age(now: int, future_years: int):
    sum = now + future_years
    print(f'The pet is currently {now} years old. In {future_years} years it will be {sum}')
    
    


