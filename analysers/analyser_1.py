from dota2.dota2 import Heroes

slardar = Heroes.heroes['Slardar']
print(slardar)

# bash not working yet
# slardar.add_special_effect('bash_lvl_1')

slardar.set_level(10)

print('damage', slardar.get_attack_damage())

for name, opponent in Heroes.heroes.items():
    opponent.set_level(20)
    att_given = slardar.get_required_attacks_to_finish(opponent)
    att_taken = opponent.get_required_attacks_to_finish(slardar)
    time_given = slardar.get_required_time_to_finish(opponent)
    time_taken = opponent.get_required_time_to_finish(slardar)
    fight_status = 'Win' if time_given < time_taken else 'Lose'

    print('-' * 50)
    print(f"Slardar attacks {fight_status} {name} {att_given} {att_taken} {att_taken-att_given}")
    print(f"Slardar seconds {fight_status} {name} {time_given} {time_taken}  {time_taken-time_given}")
    print('-' * 50)
    break


slardar.add_active_item('moon_shard')
print('damage', slardar.get_attack_damage())
for name, opponent in Heroes.heroes.items():
    opponent.set_level(20)
    att_given = slardar.get_required_attacks_to_finish(opponent)
    att_taken = opponent.get_required_attacks_to_finish(slardar)
    time_given = slardar.get_required_time_to_finish(opponent)
    time_taken = opponent.get_required_time_to_finish(slardar)
    fight_status = 'Win' if time_given < time_taken else 'Lose'

    print('-' * 50)
    print(f"Slardar attacks {fight_status} {name} {att_given} {att_taken} {att_taken-att_given}")
    print(f"Slardar seconds {fight_status} {name} {time_given} {time_taken}  {time_taken-time_given}")
    print('-' * 50)
    break
