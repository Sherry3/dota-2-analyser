from dota2.dota2.Hero import Hero
from dota2.dota2.constants import strength_heroes, agility_heores, intelligence_heroes

heroes = {}
for hero_name in strength_heroes + agility_heores + intelligence_heroes:
    hero_name = hero_name.replace(' ', '_')
    heroes[hero_name] = Hero(file=f'Heroes_data/{hero_name}.json')

'''
abaddon = Hero(
    name='Abaddon', hero_type='strength',
    base_strength=22, base_agility=23, base_intelligence=18,
    str_per_lvl=2.6, agi_per_lvl=1.5, int_per_lvl=2, base_armor=-1,
    base_min_att_damage=50, base_max_att_damage=60, base_att_speed=120
)


alchemist = Hero(
    name='Alchemist', hero_type='strength',
    base_strength=25, base_agility=22, base_intelligence=25,
    str_per_lvl=2.9, agi_per_lvl=1.5, int_per_lvl=1.8, base_armor=-1,
    base_min_att_damage=52, base_max_att_damage=58
)


ancient_apparition = Hero(
    name='Ancient Apparition', hero_type='intelligence',
    base_strength=20, base_agility=20, base_intelligence=23,
    str_per_lvl=1.9, agi_per_lvl=2.2, int_per_lvl=3.4, base_armor=-1,
    base_min_att_damage=44, base_max_att_damage=54
)


anti_mage = Hero(
    name='Anti-Mage', hero_type='agility',
    base_strength=21, base_agility=24, base_intelligence=12,
    str_per_lvl=1.6, agi_per_lvl=2.8, int_per_lvl=1.8, base_armor=0,
    base_min_att_damage=53, base_max_att_damage=57, bat=1.4
)


arc_warden = Hero(
    name='Arc Warden', hero_type='agility',
    base_strength=22, base_agility=20, base_intelligence=24,
    str_per_lvl=2.6, agi_per_lvl=3, int_per_lvl=2.6, base_armor=-1,
    base_min_att_damage=51, base_max_att_damage=57
)


axe = Hero(
    name='Axe', hero_type='strength',
    base_strength=25, base_agility=20, base_intelligence=18,
    str_per_lvl=3.4, agi_per_lvl=2.2, int_per_lvl=1.6, base_armor=-1,
    base_min_att_damage=52, base_max_att_damage=56
)


bane = Hero(
    name='Bane', hero_type='intelligence',
    base_strength=22, base_agility=22, base_intelligence=22,
    str_per_lvl=2.5, agi_per_lvl=2.5, int_per_lvl=2.5, base_armor=1,
    base_min_att_damage=55, base_max_att_damage=61
)


batrider = Hero(
    name='Batrider', hero_type='intelligence',
    base_strength=28, base_agility=15, base_intelligence=22,
    str_per_lvl=2.8, agi_per_lvl=1.8, int_per_lvl=2.9, base_armor=2,
    base_min_att_damage=39, base_max_att_damage=43
)


beastmaster = Hero(
    name='Beastmaster', hero_type='strength',
    base_strength=23, base_agility=18, base_intelligence=16,
    str_per_lvl=2.9, agi_per_lvl=1.6, int_per_lvl=1.9, base_armor=0,
    base_min_att_damage=54, base_max_att_damage=58
)


bloodseeker = Hero(
    name='Bloodseeker', hero_type='agility',
    base_strength=24, base_agility=22, base_intelligence=17,
    str_per_lvl=2.7, agi_per_lvl=3.1, int_per_lvl=2, base_armor=2,
    base_min_att_damage=57, base_max_att_damage=63
)


bounty_hunter = Hero(
    name='Bounty Hunter', hero_type='agility',
    base_strength=20, base_agility=21, base_intelligence=22,
    str_per_lvl=2.5, agi_per_lvl=2.6, int_per_lvl=1.9, base_armor=4,
    base_min_att_damage=51, base_max_att_damage=59
)


brewmaster = Hero(
    name='Brewmaster', hero_type='strength',
    base_strength=23, base_agility=19, base_intelligence=15,
    str_per_lvl=3.7, agi_per_lvl=2, int_per_lvl=1.6, base_armor=-1,
    base_min_att_damage=52, base_max_att_damage=59
)


centaur_warrunner = Hero(
    name='Centaur Warrunner', hero_type='strength',
    base_strength=27, base_agility=15, base_intelligence=15,
    str_per_lvl=4, agi_per_lvl=1, int_per_lvl=1.6, base_armor=1,
    base_min_att_damage=63, base_max_att_damage=65, base_att_speed=90
)


chaos_knight = Hero(
    name='Chaos Knight', hero_type='strength',
    base_strength=22, base_agility=18, base_intelligence=18,
    str_per_lvl=3.2, agi_per_lvl=1.4, int_per_lvl=1.2, base_armor=2,
    base_min_att_damage=51, base_max_att_damage=81
)


chen = Hero(
    name='Chen', hero_type='intelligence',
    base_strength=25, base_agility=15, base_intelligence=19,
    str_per_lvl=2, agi_per_lvl=2.1, int_per_lvl=3.2, base_armor=-1,
    base_min_att_damage=46, base_max_att_damage=56
)


clinkz = Hero(
    name='Clinkz', hero_type='agility',
    base_strength=16, base_agility=22, base_intelligence=18,
    str_per_lvl=2, agi_per_lvl=2.5, int_per_lvl=2.2, base_armor=0,
    base_min_att_damage=37, base_max_att_damage=43
)


clockwerk = Hero(
    name='Clockwerk', hero_type='strength',
    base_strength=26, base_agility=13, base_intelligence=18,
    str_per_lvl=3.5, agi_per_lvl=2.3, int_per_lvl=1.5, base_armor=1,
    base_min_att_damage=50, base_max_att_damage=52
)


crystal_maiden = Hero(
    name='Crystal Maiden', hero_type='intelligence',
    base_strength=17, base_agility=16, base_intelligence=16,
    str_per_lvl=2.2, agi_per_lvl=1.6, int_per_lvl=3.3, base_armor=-1,
    base_min_att_damage=44, base_max_att_damage=50
)


dark_seer = Hero(
    name='Dark Seer', hero_type='intelligence',
    base_strength=22, base_agility=19, base_intelligence=21,
    str_per_lvl=2.6, agi_per_lvl=1.8, int_per_lvl=2.7, base_armor=2,
    base_min_att_damage=54, base_max_att_damage=60
)


dark_willow = Hero(
    name='Dark Willow', hero_type='intelligence',
    base_strength=20, base_agility=18, base_intelligence=21,
    str_per_lvl=2, agi_per_lvl=1.6, int_per_lvl=3.5, base_armor=-1,
    base_min_att_damage=48, base_max_att_damage=56, base_att_speed=15, bat=1.5
)


dawnbreaker = Hero(
    name='Dawnbreaker', hero_type='strength',
    base_strength=26, base_agility=14, base_intelligence=20,
    str_per_lvl=3.4, agi_per_lvl=1.7, int_per_lvl=2.2, base_armor=-2,
    base_min_att_damage=57, base_max_att_damage=61
)


dazzle = Hero(
    name='Dazzle', hero_type='intelligence',
    base_strength=18, base_agility=20, base_intelligence=25,
    str_per_lvl=2.3, agi_per_lvl=1.7, int_per_lvl=3.7, base_armor=0,
    base_min_att_damage=47, base_max_att_damage=53
)


death_prophet = Hero(
    name='Death Prophet', hero_type='intelligence',
    base_strength=21, base_agility=14, base_intelligence=24,
    str_per_lvl=3.1, agi_per_lvl=1.8, int_per_lvl=3.3, base_armor=1,
    base_min_att_damage=47, base_max_att_damage=57
)


disruptor = Hero(
    name='Disruptor', hero_type='intelligence',
    base_strength=21, base_agility=15, base_intelligence=20,
    str_per_lvl=2.4, agi_per_lvl=1.4, int_per_lvl=2.9, base_armor=0,
    base_min_att_damage=49, base_max_att_damage=53
)


doom = Hero(
    name='Doom', hero_type='strength',
    base_strength=24, base_agility=11, base_intelligence=15,
    str_per_lvl=3.7, agi_per_lvl=0.9, int_per_lvl=1.7, base_armor=3,
    base_min_att_damage=58, base_max_att_damage=68
)


# ---------- haha ----------


sniper = Hero(
    name='Sniper', hero_type='agility',
    base_strength=19, base_agility=27, base_intelligence=15,
    str_per_lvl=2, agi_per_lvl=3.2, int_per_lvl=2.6, base_armor=-1,
    base_min_att_damage=40, base_max_att_damage=46
)


slardar = Hero(
    name='Slardar', hero_type='strength',
    base_strength=21, base_agility=17, base_intelligence=15,
    str_per_lvl=3.6, agi_per_lvl=2.4, int_per_lvl=1.5, base_armor=3,
    base_min_att_damage=51, base_max_att_damage=59
)
'''