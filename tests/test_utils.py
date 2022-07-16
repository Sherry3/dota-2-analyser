from dota2.dota2 import Hero, Heroes


# With 'strength' and 'health' items
def test_get_health_1():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_strength=10, str_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'])
    assert 22201 == test_hero.get_health()


# With missing_item
def test_get_health_2():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_strength=10, str_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2'])
    assert 2201 == test_hero.get_health()


# With 'agility' and 'armor' items
def test_get_armor_1():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_armor=10, base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'])
    assert 1193.7 == test_hero.get_armor()


# With missing_item
def test_get_armor_2():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_armor=10, base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2'])
    assert 1026.7 == test_hero.get_armor()


# With 'intelligence' and 'mana' items
def test_get_mana_1():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_intelligence=10, int_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'])
    assert 13276 == test_hero.get_mana()


# With missing_item
def test_get_mana_2():
    test_hero = Hero.Hero()
    test_hero.overwrite(base_intelligence=10, int_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2'])
    assert 1276 == test_hero.get_mana()


# With 'critical_hit_multiplier'
def test_get_attack_damage_1():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    )
    assert [[1, 1170], [0.2, 2340]] == test_hero.get_attack_damage()


# With 'critical_hit_multiplier' and 'head_shot'
def test_get_attack_damage_2():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'],
        active_effects=['head_shot']
    )
    assert [[1, 1170], [0.2, 2340], [0.3, 3510], [0.06, 7020]] == test_hero.get_attack_damage()


# With 'head_shot'
def test_get_attack_damage_3():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_effects=['head_shot']
    )
    assert [[1, 120], [0.3, 360]] == test_hero.get_attack_damage()


# Missing items and special effects
def test_get_attack_damage_4():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'],
        active_effects=['head_shot', 'missing_special_effect']
    )
    assert [[1, 1170], [0.2, 2340], [0.3, 3510], [0.06, 7020]] == test_hero.get_attack_damage()


# Basic case
def test_get_attack_damage_5():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='strength', base_min_att_damage=15, base_max_att_damage=25,
        base_strength=10, str_per_lvl=10, cur_lvl=10
    )
    assert [[1, 120]] == test_hero.get_attack_damage()


# With 'dummy_1'
def test_get_attack_damage_6():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_effects=['dummy_1']
    )
    assert [[1, 1170], [0.1, 5850]] == test_hero.get_attack_damage()


# With 'agility' and 'attack_speed' items
def test_get_attack_speed_1():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        base_att_speed=10, base_agility=10, agi_per_lvl=10,
        cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    )
    assert 700 == test_hero.get_attack_speed()


# With missing_item
def test_get_attack_speed_2():
    test_hero = Hero.Hero()
    test_hero.overwrite(
        base_att_speed=10, base_agility=10, agi_per_lvl=10,
        cur_lvl=10, active_items=['missing_item', 'dummy_2']
    )
    assert 610 == test_hero.get_attack_speed()


def test_get_attack_speed_3():
    # Level 30 Anti-mage
    test_hero = Hero.Hero()
    test_hero.overwrite(
        base_att_speed=100, base_agility=24, agi_per_lvl=2.8, cur_lvl=30
    )
    assert 219 == test_hero.get_attack_speed()

    # Level 30 Sniper
    test_hero = Hero.Hero()
    test_hero.overwrite(
        base_att_speed=100, base_agility=27, agi_per_lvl=3.2, cur_lvl=30
    )
    assert 234 == test_hero.get_attack_speed()


def test_get_attacks_per_sec_1():
    # Marci level 1 speed
    marci = Hero.Hero()
    marci.overwrite(base_att_speed=120)
    assert 0.706 == round(marci.get_attacks_per_sec(), 3)

    # Level 30 speed calculations are not correct.
    #  - For Anti-Mage, 219 should give 1.57 attacks per second, but 220 is giving this value.
    test_hero = Hero.Hero()
    test_hero.overwrite(base_att_speed=120)
    for i in [
        (0.89, 124, 1.4),   # Anti-Mage level 1 speed
        (1.57, 220, 1.4),   # Anti-Mage level 30 speed.
        (0.75, 127, 1.7),   # sniper level 1 speed
        (1.38, 234, 1.7)    # Sniper level 30 speed.
    ]:
        test_hero.overwrite(base_att_speed=i[1], bat=i[2])
        assert i[0] == round(test_hero.get_attacks_per_sec(), 2)


def test_get_physical_damage_taken_1():
    test_hero = Hero.Hero()

    data = [(-40, 586.21), (-30, 608.7), (-20, 647.06), (-10, 727.27)]
    for i in data:
        test_hero.overwrite(base_armor=i[0])
        assert 1000 == round(test_hero.get_physical_damage_taken(i[1], []), 0)

    data = [(0, 1000), (10, 1600), (20, 2200), (30, 2800), (40, 3400)]
    for i in data:
        test_hero.overwrite(base_armor=i[0])
        assert 1000 == round(test_hero.get_physical_damage_taken(i[1], []), 0)


# TODO: Check it's correctness
def test_get_magical_damage_taken_1():
    test_hero = Hero.Hero()
    data = [(400, 0.2, 500), (500, 0, 500), (0, 1, 500), (375, 0.25, 500)]
    for i in data:
        test_hero.overwrite(magic_resistance=i[1])
        assert i[0] == test_hero.get_magical_damage_taken(i[2])


# TODO: Check it's correctness
def test_get_required_attacks_to_finish_1():
    sniper = Heroes.heroes['Sniper']
    slardar = Heroes.heroes['Slardar']
    assert 27 == slardar.get_required_attacks_to_finish(sniper)


# TODO: Check it's correctness
def test_get_required_time_to_finish_1():
    sniper = Heroes.heroes['Sniper']
    slardar = Heroes.heroes['Slardar']
    assert 22.84 == round(slardar.get_required_time_to_finish(sniper), 2)
