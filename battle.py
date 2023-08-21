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
            print("HP : {}/{}".format(player.chara_info["HP"], player.chara_info["Max HP"]))
            action = input(">>>Choose an action (attack/heal): ").lower()

            if action == "attack":
                damage = player.damage_cal(player, npc)
                npc.take_damage(damage)
                print("----------------------------------------------")
                print("{} dealt {} to {}".format(player.chara_info["character name"], npc.chara_info["character name"], damage))
                print("----------------------------------------------")
                break

            elif action == "heal":
                heal_amt = player.heal()
                if heal_amt == -1:
                    continue
                print("----------------------------------------------")
                print("{} healed {}".format(player.chara_info["character name"], heal_amt))
                print("----------------------------------------------")
                break

            else:
                print("action unknown")
        print("----------------------------------------------")

    @staticmethod
    def npc_turn(player, npc):
        print("{}'s turn:".format(npc.chara_info["character name"]))
        print("HP : {}/{}".format(npc.chara_info["HP"], npc.chara_info["Max HP"]))
        actions = ["attack", "heal"]
        if npc.chara_info["HP"] <= npc.chara_info["Max HP"] // 2 + random.randint(1, 3):
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
