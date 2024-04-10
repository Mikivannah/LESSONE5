import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"{self.player.name} здоровье: {self.player.health}")
            print(f"{self.computer.name} здоровье: {self.computer.health}")
            print("______________________________")

            # Player's turn
            self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name}")

            # Check if computer is still alive
            if not self.computer.is_alive():
                break

            # Computer's turn
            self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name}")

        winner = self.player.name if self.player.is_alive() else self.computer.name
        print(f"{winner} Выигрывает!")

# Игра начинается
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()