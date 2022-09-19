from game_obj import *

round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes WON!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss WON!")
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f"--------- Round {round_number} ---------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.super_ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Aid", 700, 50)

    warrior = Warrior("Ahiles", 270, 10)
    mag = Mag("Wale", 250, 20)
    aibolit = Medic("Aibolit", 220, 15, 20)
    livsi = Medic("Livsi", 250, 10, 5)

    heroes = [warrior, mag, aibolit, livsi]
    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


