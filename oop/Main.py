# typr_of_enemy : str
# health_point : int = 10
# attack_damage: int = 1


# print(health_point)

from Enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'Zombie'

print(f'{enemy.type_of_enemy} has {enemy.health_point} healthpoint and can do an attack')