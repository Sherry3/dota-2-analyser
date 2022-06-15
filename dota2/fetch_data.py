import json
import requests
from lxml import etree

from dota2.constants import strength_heroes, agility_heores, intelligence_heroes

xpathselectors = {
    'strength': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[1]/th/div[2]/div[4]/text()[1]',
    'agility': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[1]/th/div[2]/div[5]/text()[1]',
    'intelligence': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[1]/th/div[2]/div[6]/text()[1]',
    'base_armor': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[1]/text()[1]',
    'base_att_speed': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[14]/td[2]/text()[1]',
    'magic_resistance': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[9]/td[2]/text()[1]',
    'status_resistance': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[10]/td[2]/text()[1]',
    'att_damage': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[11]/td[1]/text()[1]',
    'bat': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[14]/td[3]/text()[1]',
}


xpathselectors_assertions = {
    'attacks_per_second_0': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/text()[1]',
    'attacks_per_second_1': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[12]/td[2]/text()[1]',
    'attacks_per_second_15': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[12]/td[3]/text()[1]',
    'attacks_per_second_25': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[12]/td[4]/text()[1]',
    'attacks_per_second_30': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[12]/td[5]/text()[1]',
    'health_0': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[1]/text()[1]',
    'health_1': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/text()[1]',
    'health_15': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[3]/text()[1]',
    'health_25': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[4]/text()[1]',
    'health_30': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[5]/text()[1]',

    'mana_0': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td[1]/text()[1]',
    'mana_1': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/text()[1]',
    'mana_15': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td[3]/text()[1]',
    'mana_25': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td[4]/text()[1]',
    'mana_30': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[5]/td[5]/text()[1]',
    'armor_0': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[1]/text()[1]',
    'armor_1': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[2]/span/text()[1]',
    'armor_15': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[3]/span/text()[1]',
    'armor_25': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[4]/span/text()[1]',
    'armor_30': '/html/body/div[4]/div[3]/div[2]/main/div[3]/div[1]/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[5]/span/text()[1]',
}


def get_stats():
    url = "https://dota2.fandom.com/wiki/"

    def iterate_over_heroes(url, heroes, hero_type):
        for hero in heroes:
            temp_url = url
            hero = hero.replace(' ', '_')
            temp_url += hero
            data = {'name': hero.replace('_', ' '), 'hero_type': hero_type}
            data.update(fetch_data(temp_url))
            with open('Heroes_data/' + hero + '.json', 'w') as f:
                f.write(json.dumps(data))

    #iterate_over_heroes(url, ['Sniper'], 'agility')
    iterate_over_heroes(url, strength_heroes, 'strength')
    iterate_over_heroes(url, agility_heores, 'agility')
    iterate_over_heroes(url, intelligence_heroes, 'intelligence')

def fetch_data(url):
    try:
        data = {}
        ssn = requests.Session()
        source_code = ssn.get(url)
        text = source_code.text
        htmlparser = etree.HTMLParser()
        tree = etree.XML(text, parser=htmlparser)

        strength = tree.xpath(xpathselectors['strength'])[0]
        data['base_strength'], data['str_per_lvl'] = strength.replace(' ', '').split('+')
        agility = tree.xpath(xpathselectors['agility'])[0]
        data['base_agility'], data['agi_per_lvl'] = agility.replace(' ', '').split('+')
        intelligence = tree.xpath(xpathselectors['intelligence'])[0]
        data['base_intelligence'], data['int_per_lvl'] = intelligence.replace(' ', '').split('+')

        data['base_armor'] = tree.xpath(xpathselectors['base_armor'])[0].split('\n')[0]
        data['magic_resistance'] = tree.xpath(xpathselectors['magic_resistance'])[0].split('%')[0]
        data['status_resistance'] = tree.xpath(xpathselectors['status_resistance'])[0].split('%')[0]

        data['base_min_att_damage'], data['base_max_att_damage'] = tree.xpath(
            xpathselectors['att_damage']
        )[0].split('\n')[0].split('‒')

        data['bat'] = tree.xpath(xpathselectors['bat'])[0].split('(')[1].split('s')[0]
        data['base_att_speed'] = tree.xpath(xpathselectors['base_att_speed'])[0].split('\n')[0]

        data['assertions'] = {}
        for key, selector in xpathselectors_assertions.items():
            data['assertions'][key] = tree.xpath(selector)[0].split('\n')[0]

        print('.', end='')
        return data
    except Exception as e:
        print(f'F - {url}')
        print("Error2 : ", str(e))
        return {}

