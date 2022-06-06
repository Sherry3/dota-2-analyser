from .. import Hero


sniper = Hero.Hero(
    name='sniper', base_strength=19, base_agility=27, base_intelligence=15, base_armor=-1,
    base_att_speed=100, base_min_att_damage=19, base_max_att_damage=25, str_per_lvl=2,
    agi_per_lvl=3.2, int_per_lvl=2.6, cur_lvl=0, hero_type='agility'
)


slardar = Hero.Hero(
    name='slardar', base_strength=21, base_agility=17, base_intelligence=15, base_armor=3,
    base_att_speed=100, base_min_att_damage=30, base_max_att_damage=38, str_per_lvl=3.6,
    agi_per_lvl=2.4, int_per_lvl=1.5, cur_lvl=0, hero_type='strength'
)


def assert_status_at_levels(hero, method, data, round_pre=None):
    # Health at level 1, 5, 10, 15, 20, 25, 30
    for i in data:
        hero.set_level(i[0])
        if round_pre is not None:
            assert i[1] == round(method(), round_pre)
        else:
            assert i[1] == method()


def test_sniper_health():
    # Health at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 580), (15, 1140), (25, 1780), (30, 2020)]
    assert_status_at_levels(sniper, sniper.get_health, data)


def test_slardar_health():
    # Health at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 620), (15, 1620), (25, 2580), (30, 2980)]
    assert_status_at_levels(slardar, slardar.get_health, data)


def test_sniper_armor():
    # Armor at level 1, 5, 10, 15, 20, 25, 30
    # 10.991 should be 10.97 instead
    data = [(1, 3.509), (15, 10.991), (25, 18.339), (30, 21.345)]
    assert_status_at_levels(sniper, sniper.get_armor, data, round_pre=3)


def test_slardar_armor():
    # Armor at level 1, 5, 10, 15, 20, 25, 30
    # None of the values are exactly matching
    data = [(1, 5.839), (15, 11.45), (25, 17.462), (30, 19.8)]
    assert_status_at_levels(slardar, slardar.get_armor, data, round_pre=3)


def test_sniper_mana():
    # Mana at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 255), (15, 687), (25, 1143), (30, 1323)]
    assert_status_at_levels(sniper, sniper.get_mana, data)


def test_slardar_mana():
    # Mana at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 255), (15, 507), (25, 831), (30, 939)]
    assert_status_at_levels(slardar, slardar.get_mana, data)


def test_sniper_attack_damage():
    # Self calculated target values
    # Attack damage at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, [[1, 49]]), (15, [[1, 94]]), (25, [[1, 138]]), (30, [[1, 156]])]
    assert_status_at_levels(sniper, sniper.get_attack_damage, data)


def test_slardar_attack_damage():
    # Self calculated target values
    # Attack damage at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, [[1, 55]]), (15, [[1, 105]]), (25, [[1, 153]]), (30, [[1, 173]])]
    assert_status_at_levels(slardar, slardar.get_attack_damage, data)


def test_sniper_attack_speed():
    # Self calculated target values
    # Attack speed at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 127), (15, 172), (25, 216), (30, 234)]
    assert_status_at_levels(sniper, sniper.get_attack_speed, data)


def test_slardar_attack_speed():
    # Self calculated target values
    # Attack speed at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 117), (15, 151), (25, 187), (30, 201)]
    assert_status_at_levels(slardar, slardar.get_attack_speed, data)


def test_sniper_attacks_per_second():
    # Didn't calculated target values at all
    # Attacks per second at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 0.747), (15, 1.012), (25, 1.271), (30, 1.376)]
    assert_status_at_levels(sniper, sniper.get_attacks_per_sec, data, round_pre=3)


def test_slardar_attacks_per_second():
    # Didn't calculated target values at all
    # Attacks per second at level 1, 5, 10, 15, 20, 25, 30
    data = [(1, 0.688), (15, 0.888), (25, 1.1), (30, 1.182)]
    assert_status_at_levels(slardar, slardar.get_attacks_per_sec, data, round_pre=3)
