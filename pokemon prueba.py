#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.


from unicodedata import name


weapon_list = ["Puñetazo", "Patada", "Codazo", "Cabezazo"]
class Pokemon():
    def __init__(self, ID, name, weapon, health, attack_dmg, defense_stat):
        self.ID = ID
        self.name = name
        self.weapon = weapon
        self.health = health
        self.attack_dmg = attack_dmg
        self.defense_stat = defense_stat

    def setID(self, ID):
        self.ID = int(input("Introduce el ID del pokemon: "))
    
    def setname(self, name):
        self.name = int(input("Introduce el nombre del pokemon: "))
    
    
    
    def setweapon(self, weapon):
        opcion = int(input("Selecciona que arma tiene el pokemon(1:Puñetazo  2:Patada  3:Codazo   4:Cabezazo): "))
        if opcion == 1:
            self.weapon = weapon_list[0]
        elif opcion == 2:
            self.weapon = weapon_list[1]
        elif opcion == 3:
            self.weapon = weapon_list[2]
        elif opcion == 4:
            self.weapon = weapon_list[3]
    
    def sethealth(self, health):
        self.health = int(input("Introduce la vida del pokemon(1-100): "))
    
    def setattack_dmg(self, attack_dmg):
        self.attack_dmg = int(input("Introduce el daño de ataque del pokemon(1-10): "))
    
    def setdefense_stat(self, defense_stat):
        self.defense_stat = int(input("Introduce la defensa del pokemon(1-10): "))

    def get_pokemon_ID(self, ID):
        return ID
    
    def get_pokemon_name(self, name):
        return name
    
    def get_weapon_type(self, weapon):
        return weapon
    
    def get_health_points(self, health):
        return health

    def get_attack_rating(self, attack_dmg):
        return attack_dmg

    def get_defense_rating(self, defense_stat):
        return defense_stat

    def is_alive(self, health):
        if health >= 0:
           vivo = True
        else:
            vivo = False
        return vivo

    def fight_attack(self, pokemon_to_attack):
        global vivo
        if vivo == True:
            pokemon_to_attack = True
        else:
            pokemon_to_attack = False
        return pokemon_to_attack
    
    def fight_defense(self, health, attack_dmg, defense_stat, pokemon_to_defend, pokemon_to_attack):
        while vivo == True:
            if pokemon_to_attack == True:
                health -= attack_dmg*(1 - (0.05*defense_stat))
                pokemon_to_defend = True
            else:
                pokemon_to_defend = False
            return pokemon_to_defend, health
        else:
            print("Al pokemon no le queda vida, el combate ha terminado.")





def main():

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", weapon_list[0], 100, 8, 9)

    if pokemon_1.get_pokemon_name(name) == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type.weapon == weapon_list[0]:
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points.health == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating.attack_dmg == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating.defense_stat == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", weapon_list[1], 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", weapon_list[2], 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", weapon_list[3], 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", weapon_list[0], 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", weapon_list[0], 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
