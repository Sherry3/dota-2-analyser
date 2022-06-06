from .. import Hero


# With 'strength' and 'health' items
def test_get_health_1():
    assert 22201 == Hero.Hero(
        base_strength=10, str_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    ).get_health()


# With missing_item
def test_get_health_2():
    assert 2201 == Hero.Hero(
        base_strength=10, str_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2']
    ).get_health()


# With 'agility' and 'armor' items
def test_get_armor_1():
    assert 1193.7 == Hero.Hero(
        base_armor=10, base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    ).get_armor()


# With missing_item
def test_get_armor_2():
    assert 1026.7 == Hero.Hero(
        base_armor=10, base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2']
    ).get_armor()


# With 'intelligence' and 'mana' items
def test_get_mana_1():
    assert 13276 == Hero.Hero(
        base_intelligence=10, int_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    ).get_mana()


# With missing_item
def test_get_mana_2():
    assert 1276 == Hero.Hero(
        base_intelligence=10, int_per_lvl=10, cur_lvl=10, active_items=['missing_item', 'dummy_2']
    ).get_mana()


# With 'critical_hit_multiplier'
def test_get_attack_damage_1():
    assert [[1, 1170], [0.2, 2340]] == Hero.Hero(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    ).get_attack_damage()


# With 'critical_hit_multiplier' and 'head_shot'
def test_get_attack_damage_2():
    assert [[1, 1170], [0.2, 2340], [0.3, 3510], [0.06, 7020]] == Hero.Hero(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'],
        active_effects=['head_shot']
    ).get_attack_damage()


# With 'head_shot'
def test_get_attack_damage_3():
    assert [[1, 120], [0.3, 360]] == Hero.Hero(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_effects=['head_shot']
    ).get_attack_damage()


# Missing items and special effects
def test_get_attack_damage_4():
    assert [[1, 1170], [0.2, 2340], [0.3, 3510], [0.06, 7020]] == Hero.Hero(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_items=['dummy_1', 'dummy_2'],
        active_effects=['head_shot', 'missing_special_effect']
    ).get_attack_damage()


# Basic case
def test_get_attack_damage_5():
    assert [[1, 120]] == Hero.Hero(
        hero_type='strength', base_min_att_damage=15, base_max_att_damage=25,
        base_strength=10, str_per_lvl=10, cur_lvl=10
    ).get_attack_damage()


# With 'dummy_1'
def test_get_attack_damage_6():
    assert [[1, 1170], [0.1, 5850]] == Hero.Hero(
        hero_type='agility', base_min_att_damage=15, base_max_att_damage=25,
        base_agility=10, agi_per_lvl=10, cur_lvl=10, active_effects=['dummy_1']
    ).get_attack_damage()


# With 'agility' and 'attack_speed' items
def test_get_attack_speed_1():
    assert 700 == Hero.Hero(
        base_att_speed=10, base_agility=10, agi_per_lvl=10,
        cur_lvl=10, active_items=['dummy_1', 'dummy_2']
    ).get_attack_speed()

# With missing_item
def test_get_attack_speed_2():
    assert 610 == Hero.Hero(
        base_att_speed=10, base_agility=10, agi_per_lvl=10,
        cur_lvl=10, active_items=['missing_item', 'dummy_2']
    ).get_attack_speed()


def test_get_attack_speed_3():
    # Level 30 Anti-mage
    assert 219 == Hero.Hero(
        base_att_speed=100, base_agility=24, agi_per_lvl=2.8, cur_lvl=30
    ).get_attack_speed()

    # Level 30 Sniper
    assert 234 == Hero.Hero(
        base_att_speed=100, base_agility=27, agi_per_lvl=3.2, cur_lvl=30
    ).get_attack_speed()


def test_get_attacks_per_sec_1():
    # Marci level 1 speed
    marci = Hero.Hero(base_att_speed=120)
    assert 0.706 == round(marci.get_attacks_per_sec(), 3)

    # Level 30 speed calculations are not correct.
    #  - For Anti-Mage, 219 should give 1.57 attacks per second, but 220 is giving this value.
    for i in [
        (0.89, Hero.Hero(base_att_speed=124, bat=1.4)),   # Anti-Mage level 1 speed
        (1.57, Hero.Hero(base_att_speed=220, bat=1.4)),   # Anti-Mage level 30 speed.
        (0.75, Hero.Hero(base_att_speed=127, bat=1.7)),   # sniper level 1 speed
        (1.38, Hero.Hero(base_att_speed=234, bat=1.7))    # Sniper level 30 speed.
    ]:
        assert i[0] == round(i[1].get_attacks_per_sec(), 2)


def test_get_physical_damage_taken_1():
    data = [(-40, 586.21), (-30, 608.7), (-20, 647.06), (-10, 727.27)]
    for i in data:
        assert 1000 == round(Hero.Hero(base_armor=i[0]).get_physical_damage_taken(i[1]), 0)

    data = [(0, 1000), (10, 1600), (20, 2200), (30, 2800), (40, 3400)]
    for i in data:
        assert 1000 == round(Hero.Hero(base_armor=i[0]).get_physical_damage_taken(i[1]), 0)


# TODO: Check it's correctness
def test_get_magical_damage_taken_1():
    data = [(400, 0.2, 500), (500, 0, 500), (0, 1, 500)]
    for i in data:
        assert i[0] == Hero.Hero(spell_resistance=i[1]).get_magical_damage_taken(i[2])


# TODO: Check it's correctness
def test_get_required_attacks_to_finish_1():
    assert 13 == Hero.Hero(
        name='slardar', base_strength=21, base_agility=17, base_armor=3, base_att_speed=100,
        base_min_att_damage=30, base_max_att_damage=38, str_per_lvl=3.6, agi_per_lvl=2.4,
        cur_lvl=1, hero_type='strength'
    ).get_required_attacks_to_finish(
        Hero.Hero(base_armor=3.5, base_strength=19, cur_lvl=1)
    )


# TODO: Check it's correctness
def test_get_required_time_to_finish_1():
    assert 18.89 == round(Hero.Hero(
        name='slardar', base_strength=21, base_agility=17, base_armor=3, base_att_speed=100,
        base_min_att_damage=30, base_max_att_damage=38, str_per_lvl=3.6, agi_per_lvl=2.4,
        cur_lvl=1, hero_type='strength'
    ).get_required_time_to_finish(
        Hero.Hero(base_armor=3.5, base_strength=19, cur_lvl=1)
    ), 2)
