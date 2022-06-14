import math
import random
import json

from dota2.dota2.items import items
from dota2.dota2.special_effects import special_effects
from dota2.dota2 import constants


class Hero:
    def __init__(self, file=None, active_items=None, active_effects=None):
        if file is not None:
            with open(file, 'r') as f:
                data = json.loads(''.join(f.readlines()))
                self.name = data['name']
                self.base_strength = float(data['base_strength'])
                self.base_agility = float(data['base_agility'])
                self.base_intelligence = float(data['base_intelligence'])
                self.base_armor = float(data['base_armor'])
                self.base_att_speed = float(data['base_att_speed'])
                self.base_min_att_damage = float(data['base_min_att_damage'])
                self.base_max_att_damage = float(data['base_max_att_damage'])
                self.str_per_lvl = float(data['str_per_lvl'])
                self.agi_per_lvl = float(data['agi_per_lvl'])
                self.int_per_lvl = float(data['int_per_lvl'])
                self.cur_lvl = 1
                self.hero_type = data['hero_type']
                self.bat = float(data['bat'])
                self.magic_resistance = float(data['magic_resistance'])/100
                self.status_resistance = float(data['status_resistance'])/100
                self.assertions = data['assertions']

        if active_items is None:
            self.active_items = []
        else:
            self.active_items = active_items
        if active_effects is None:
            self.active_effects = []
        else:
            self.active_effects = active_effects

        self.bonus_attrs = {17: 2, 18: 2, 19: 4, 20: 4, 21: 6, 22: 8, 23: 10, 24: 12, 25: 12}

    def overwrite(
        self, base_strength=0, base_agility=0, base_intelligence=0, base_armor=0, base_att_speed=100,
        base_min_att_damage=0, base_max_att_damage=0, str_per_lvl=0, agi_per_lvl=0, int_per_lvl=0,
        cur_lvl=0, hero_type=None, bat=1.7, magic_resistance=0.25, status_resistance=0, name='',
        active_items=None, active_effects=None
    ):
        self.name = name
        self.base_strength = base_strength
        self.base_agility = base_agility
        self.base_intelligence = base_intelligence
        self.base_armor = base_armor
        self.base_att_speed = base_att_speed
        self.base_min_att_damage = base_min_att_damage
        self.base_max_att_damage = base_max_att_damage
        self.str_per_lvl = str_per_lvl
        self.agi_per_lvl = agi_per_lvl
        self.int_per_lvl = int_per_lvl
        self.cur_lvl = cur_lvl
        self.hero_type = hero_type
        self.bat = bat
        self.magic_resistance = magic_resistance

        if active_items is None:
            self.active_items = []
        else:
            self.active_items = active_items
        if active_effects is None:
            self.active_effects = []
        else:
            self.active_effects = active_effects

    def set_level(self, level):
        self.cur_lvl = level

    def get_level(self, level):
        return self.cur_lvl

    def get_bonus_attr(self):
        if self.cur_lvl >= 26:
            return 14
        if self.cur_lvl not in self.bonus_attrs:
            return 0
        return self.bonus_attrs[self.cur_lvl]

    def get_health(self):
        cur_health = constants.base_health
        print(f'cur_health 1 = {cur_health}')
        bonus_strength = self.get_bonus_attr()
        cur_health += round(
            (self.str_per_lvl*(self.cur_lvl-1))+self.base_strength+bonus_strength
        ) * constants.health_per_strength
        print(f'cur_health 2 = {cur_health}')

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'strength' in item:
                cur_health += constants.health_per_strength * item['strength']
            if 'health' in item:
                cur_health += item['health']

        return cur_health

    def get_mana(self):
        cur_mana = constants.base_mana
        bonus_int = self.get_bonus_attr()
        cur_mana += (round((self.int_per_lvl*(self.cur_lvl-1))+self.base_intelligence+bonus_int)) * constants.mana_per_int

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'intelligence' in item:
                cur_mana += constants.mana_per_int * item['intelligence']
            if 'mana' in item:
                cur_mana += item['mana']

        return cur_mana

    # TODO: Check whether this calculation is correct or not
    def get_armor(self):
        cur_armor = self.base_armor
        bonus_agility = self.get_bonus_attr()
        cur_armor += (round((self.agi_per_lvl*(self.cur_lvl-1))+self.base_agility+bonus_agility, 2)) * constants.armor_per_agility

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'agility' in item:
               cur_armor += constants.armor_per_agility * item['agility']
            if 'armor' in item:
               cur_armor += item['armor']

        return cur_armor

    def get_attack_damage(self):
        cur_damages = [[1, (self.base_min_att_damage+self.base_max_att_damage)/2]]
        bonus_attr = self.get_bonus_attr()

        if self.hero_type == 'strength':
            cur_damages[0][1] += round((self.str_per_lvl*(self.cur_lvl-1))+self.base_strength+bonus_attr)
        elif self.hero_type == 'agility':
            cur_damages[0][1] += round((self.agi_per_lvl*(self.cur_lvl-1))+self.base_agility+bonus_attr)
        elif self.hero_type == 'intelligence':
            cur_damages[0][1] += round((self.int_per_lvl*(self.cur_lvl-1))+self.base_intelligence+bonus_attr)
        else:
            raise Exception('Invalid hero type')

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'damage' in item:
                cur_damages[0][1] += item['damage']
            if self.hero_type in item:
                cur_damages[0][1] += item[self.hero_type]

        for special_effect in self.active_effects:
            if special_effect not in special_effects:
                continue
            special_effect = special_effects[special_effect]
            if 'damage' in special_effect:
                cur_damages[0][1] += special_effect['damage']
            if self.hero_type in special_effect:
                cur_damages[0][1] += special_effect[self.hero_type]

        for special_effect in self.active_effects:
            if special_effect not in special_effects:
                continue
            # This flow is not tested yet
            if 'critical_hit_chance' in special_effect and 'critical_hit_damage' in special_effect:
                for cur_damage in cur_damages[:]:
                    cur_damages.append([
                        cur_damage[0] * special_effect['critical_hit_chance'],
                        cur_damage[1] + special_effect['critical_hit_damage']
                    ])

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'critical_hit_multiplier' in item and 'critical_hit_chance' in item:
                for cur_damage in cur_damages[:]:
                    cur_damages.append([
                        cur_damage[0] * item['critical_hit_chance'],
                        cur_damage[1] * item['critical_hit_multiplier']
                    ])

        for special_effect in self.active_effects:
            if special_effect not in special_effects:
                continue
            special_effect = special_effects[special_effect]
            if 'critical_hit_multiplier' in special_effect and 'critical_hit_chance' in special_effect:
                for cur_damage in cur_damages[:]:
                    cur_damages.append([
                        cur_damage[0] * special_effect['critical_hit_chance'],
                        cur_damage[1] * special_effect['critical_hit_multiplier']
                    ])

        return cur_damages

    # TODO: Check whether this calculation is correct or not
    def get_attack_speed(self):
        cur_attack_speed = self.base_att_speed
        bonus_agility = self.get_bonus_attr()
        cur_attack_speed += round((self.agi_per_lvl*(self.cur_lvl-1))+self.base_agility+bonus_agility)

        for item in self.active_items:
            if item not in items:
                continue
            item = items[item]
            if 'attack_speed' in item:
                cur_attack_speed += item['attack_speed']
            if 'agility' in item:
                cur_attack_speed += item['agility']

        cur_attack_speed = min(cur_attack_speed, 700)
        return cur_attack_speed

    def get_attacks_per_sec(self):
        cur_attack_speed = self.get_attack_speed()/(self.bat*100)
        return cur_attack_speed

    def get_physical_damage_taken(self, physical_damage):
        total_damage = physical_damage
        armor = self.get_armor()
        damage_multiplier = 1 - (constants.armor_damage_factor * armor)/(1+(constants.armor_damage_factor * abs(armor)))
        return total_damage * damage_multiplier

    def get_magical_damage_taken(self, magical_damage):
        total_damage = magical_damage
        total_damage = total_damage * (1-self.magic_resistance)
        return total_damage

    def get_required_attacks_to_finish(self, opponent):
        probability, attack_damage = map(list, zip(*self.get_attack_damage()))
        print(attack_damage, probability)
        mean_damage = sum(random.choices(attack_damage, probability, k=10000))/10000
        damage_per_attack = opponent.get_physical_damage_taken(mean_damage)
        num_attacks = math.ceil(opponent.get_health()/damage_per_attack)
        return num_attacks

    def get_required_time_to_finish(self, opponent):
        num_attacks = self.get_required_attacks_to_finish(opponent)
        time_in_secs = num_attacks/self.get_attacks_per_sec()
        return time_in_secs

    def __str__(self):
        return str({
            'name': self.name,
            'hero_type': self.hero_type,
            'base_strength': self.base_strength,
            'base_agility': self.base_agility,
            'base_intelligence': self.base_intelligence,
            'base_armor': self.base_armor,
            'base_att_speed': self.base_att_speed,
            'base_min_att_damage': self.base_min_att_damage,
            'base_max_att_damage': self.base_max_att_damage,
            'str_per_lvl': self.str_per_lvl,
            'agi_per_lvl': self.agi_per_lvl,
            'int_per_lvl': self.int_per_lvl,
            'cur_lvl': self.cur_lvl,
            'bat': self.bat,
            'magic_resistance': self.magic_resistance,
            'active_items': self.active_items,
            'active_effects': self.active_effects,
        })