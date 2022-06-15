from dota2.dota2 import Heroes

sniper = Heroes.heroes['Sniper']
slardar = Heroes.heroes['Slardar']
print(f"Sniper finishes Slardar in {sniper.get_required_attacks_to_finish(slardar)} attacks.")
print(f"Sniper finishes Slardar in {sniper.get_required_time_to_finish(slardar)} seconds.")
