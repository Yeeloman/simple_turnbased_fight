#!/usr/bin/python3

import random

class character_class:

    def __init__(self, chara_info):
        self.chara_info = chara_info
        self.chara_info.update({"Atk Mod" : character_class.calModifier(chara_info["Atk"]),
                            "Def Mod" : character_class.calModifier(chara_info["Def"]),
                            "HP Mod" : character_class.calModifier(chara_info["HP"]),
                            "Max HP" : chara_info["HP"]})

    def take_damage(self, damage):
        self.chara_info["HP"] -= damage

    @staticmethod
    def damage_cal(player1, player2):
        damage_dealt = player1.attack() - player2.block()
        return damage_dealt

    @staticmethod
    def calModifier(ability_score):
        modifier = (ability_score - 10) // 2
        return modifier

class Warrior(character_class):

    def __init__(self, chara_info):
        super().__init__(chara_info)

    def attack(self):
        atk_amt = random.randint(1, 6) + self.chara_info["Atk Mod"]
        return atk_amt

    def block(self):
        block_amt = random.randint(1, 4) + self.chara_info["Def Mod"]
        return block_amt

    def heal(self):
        while True:
            if self.chara_info["HP"] < self.chara_info["Max HP"]:
                heal_amt = self.chara_info["HP Mod"] + random.randint(1, 2)
                self.chara_info["HP"] += heal_amt
                break
            else:
                print("Already full HP")
        return heal_amt

class Knight(character_class):

    def __init__(self, chara_info):
        super().__init__(chara_info)

    def attack(self):
        atk_amt = random.randint(1, 4) + self.chara_info["Atk Mod"]
        return atk_amt

    def block(self):
        block_amt = random.randint(1, 8) + self.chara_info["Def Mod"]
        return block_amt

    def heal(self):
        while True:
            if self.chara_info["HP"] < self.chara_info["Max HP"]:
                heal_amt = self.chara_info["HP Mod"] + random.randint(1, 4)
                self.chara_info["HP"] += heal_amt
                break
            else:
                print("Already full HP")
                heal_amt = -1
                break
        return heal_amt




