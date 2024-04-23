class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.animal_type}")
