from dota2.dota2 import Heroes

slardar = Heroes.heroes['Slardar']
print(slardar)

opponent_name = 'Sniper'
sniper = Heroes.heroes[opponent_name]
print(sniper)

for level in range(1, 31):
    slardar.set_level(level)
    sniper.set_level(level)

    if level == 15:
        sniper.add_active_item('desolator')
        sniper.add_active_item('desolator')
        sniper.add_active_item('moon_shard')
        sniper.add_active_item('daedalus')
    if level == 18:
        slardar.add_active_item('shivas_guard')
    if level == 20:
        slardar.add_active_item('heart_of_tarrasque')
        slardar.add_active_item('assault_cuirass')
        slardar.add_active_item('armor_corruption')

    print(f'At level {level} Slardar damage is {slardar.get_attack_damage()}')
    print(f'At level {level} {opponent_name} damage is {sniper.get_attack_damage()}')

    print(f'{slardar.get_physical_damage_taken(100, sniper.active_items)}   {sniper.get_physical_damage_taken(100, slardar.active_items)}')

    att_given = slardar.get_required_attacks_to_finish(sniper)
    att_taken = sniper.get_required_attacks_to_finish(slardar)
    time_given = slardar.get_required_time_to_finish(sniper)
    time_taken = sniper.get_required_time_to_finish(slardar)
    fight_status = 'Win' if time_given < time_taken else 'Lose'

    print('-' * 50)
    print(f"At level {level} Slardar attacks {fight_status} {opponent_name} {att_given} {att_taken} {att_taken - att_given}")
    print(f"At level {level} Slardar seconds {fight_status} {opponent_name} {time_given} {time_taken}  {time_taken - time_given}")
    print('-' * 50)
