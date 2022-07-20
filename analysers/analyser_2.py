from dota2.dota2 import Heroes

sniper = Heroes.heroes['Sniper']
print(sniper)

opponent_name = 'Lifestealer'
lifestealer = Heroes.heroes[opponent_name]
print(lifestealer)

for level in range(1, 31):
    sniper.set_level(level)
    lifestealer.set_level(level)

    if level == 15:
        sniper.add_active_item('desolator')

    print(f'At level {level} Sniper damage is {sniper.get_attack_damage()}')
    print(f'At level {level} {opponent_name} damage is {lifestealer.get_attack_damage()}')

    att_given = sniper.get_required_attacks_to_finish(lifestealer)
    att_taken = lifestealer.get_required_attacks_to_finish(sniper)
    time_given = sniper.get_required_time_to_finish(lifestealer)
    time_taken = lifestealer.get_required_time_to_finish(sniper)
    fight_status = 'Win' if time_given < time_taken else 'Lose'

    print('-' * 50)
    print(f"At level {level} Sniper attacks {fight_status} {opponent_name} {att_given} {att_taken} {att_taken - att_given}")
    print(f"At level {level} Sniper seconds {fight_status} {opponent_name} {time_given} {time_taken}  {time_taken - time_given}")
    print('-' * 50)
