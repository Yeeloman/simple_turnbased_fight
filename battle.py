#!/usr/bin/python3

from classes import character_class
import random

class battle:
    @staticmethod
    def startBattle(crnt_player, player, npc):
        print(">>>Battle starts!!")
        while True:
            if crnt_player == player:
                battle.player_turn(player, npc)
            else:
                battle.npc_turn(player, npc)

            if player.chara_info["HP"] <= 0:
                print("You die, hh")
                break
            elif npc.chara_info["HP"] <= 0:
                print("You win sadly")
                break
            crnt_player = player if crnt_player == npc else npc


    @staticmethod
    def player_turn( player, npc):
        while True:
            print("{}'s turn:".format(player.chara_info["character name"]))
            print("HP : {}".format(player.chara_info["HP"]))
            action = input(">>>Choose an action (attack/heal): ").lower()

            if action == "attack":
                damage = player.damage_cal(player, npc)
                npc.take_damage(damage)
                print("{} dealt {} to {}".format(player.chara_info["character name"], npc.chara_info["character name"], damage))
                break

            elif action == "heal":
                heal_amt = player.heal()
                print("{} healed {}".format(player.chara_info["character name"], heal_amt))
                break

            else:
                print("action unknown")

    @staticmethod
    def npc_turn(player, npc):
        print("{}'s turn:".format(npc.chara_info["character name"]))
        print("HP : {}".format(npc.chara_info["HP"]))
        actions = ["attack", "heal"]
        if npc.chara_info["HP"] <= 10:
            action = random.choice(actions)
        else:
            action = "attack"

        if action == "attack":
            damage = npc.damage_cal(npc, player)
            player.take_damage(damage)
            print("{} dealt {} to {}".format(npc.chara_info["character name"], player.chara_info["character name"], damage))

        else:
            heal_amt = npc.heal()
            print("{} healed {}".format(npc.chara_info["character name"], heal_amt))
