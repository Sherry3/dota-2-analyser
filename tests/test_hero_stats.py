from dota2.dota2 import Heroes

sniper = Heroes.heroes['Sniper']
slardar = Heroes.heroes['Slardar']

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
    print(sniper)
    data = [(1, [[1, 43]]), (15, [[1, 88]]), (25, [[1, 132]]), (30, [[1, 150]])]
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


def test_all_heores_health():
    for name, hero in Heroes.heroes.items():
        for assertion in ['health_1', 'health_15', 'health_25', 'health_30']:
            hero.set_level(int(assertion.split('_')[1]))
            print(f'Hero = {hero.name}')
            assert int(hero.assertions[assertion]) - 20 <= hero.get_health() <= int(hero.assertions[assertion]) + 20


def test_all_heores_mana():
    for name, hero in Heroes.heroes.items():
        for assertion in ['mana_1', 'mana_15', 'mana_25', 'mana_30']:
            hero.set_level(int(assertion.split('_')[1]))
            print(f'Hero = {hero.name}')
            assert int(hero.assertions[assertion]) - 12 <= hero.get_mana() <= int(hero.assertions[assertion]) + 12


def test_all_heores_att_per_sec():
    for name, hero in Heroes.heroes.items():
        for assertion in [
            'attacks_per_second_1', 'attacks_per_second_15', 'attacks_per_second_25', 'attacks_per_second_30'
        ]:
            hero.set_level(int(assertion.split('_')[3]))
            print(f'Hero = {hero.name}')
            assert float(hero.assertions[assertion]) - 0.1 \
                   <= round(hero.get_attacks_per_sec(), 2) \
                   <= float(hero.assertions[assertion]) + 0.1


def test_all_heores_armor():
    for name, hero in Heroes.heroes.items():
        for assertion in ['armor_1', 'armor_15', 'armor_25', 'armor_30']:
            hero.set_level(int(assertion.split('_')[1]))
            print(f'Hero = {hero.name}')
            assert float(hero.assertions[assertion]) - 0.1 \
                   <= round(hero.get_armor(), 2) \
                   <= float(hero.assertions[assertion]) + 0.1