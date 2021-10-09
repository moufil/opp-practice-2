class Soda:
    def __init__(self, add = None):
        self.add = add
    def show_my_drink(self):
        print(f"Газировка и {self.add}" if self.add else "Обычная газировка")
soda = Soda(add = "Банан")
soda.show_my_drink()
soda1 = Soda()
soda1.show_my_drink()
