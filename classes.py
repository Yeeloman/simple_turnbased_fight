#!/usr/bin/python3

import random

class character_class:

    def __init__(self, chara_info):
        self.chara_info = chara_info

    def attack(self):
        atk_amt = self.chara_info["Atk"] * random.random()
        return atk_amt

    def block(self):
        block_amt = self.chara_info["Def"] * random.random()
        return block_amt

    def heal(self):
        heal_amt = (self.chara_info["HP"] / 2) * random.random()
        self.chara_info["HP"] += heal_amt
        return heal_amt

    def take_damage(self, damage):
        self.chara_info["HP"] -= damage

    @staticmethod
    def damage_cal(player1, player2):
        damage_dealt = player1.attack() - player2.block()
        return damage_dealt
