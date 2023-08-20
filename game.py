#!/usr/bin/python3

from classes import character_class
from loops import addToClass, character_selection, character_stats, addToClass, npcMaker
import random
from battle import battle

classes = ["Warrior", "Knight"]
chara_info = {
    "character class" : "",
    "character name" : "",
    "HP" : 0,
    "Atk" : 0,
    "Def" : 0
}

print("a random battle game v0.0.0")
print("----------------------------------------------")
print(">> Available classes:")

for idx, claSS in enumerate(classes, start=1):
    print("{} - {}".format(idx, claSS))

chara_info["character class"] = character_selection(classes)
chara_info["character name"] = input(">> Enter your character's name : ")

print(">> Add the bonus points to the attributes you desire")

main_player = character_stats(chara_info)
main_player = addToClass(main_player)
npc_player = npcMaker()

print("You are up against {} the {}".format(npc_player["character name"], npc_player["character class"]))
Player1 = character_class(main_player)
Player2 = character_class(npc_player)
print("----------------------------------------------")
players_list = [Player1, Player2]
current_player = random.choice(players_list)

print("{} play's first".format(current_player.chara_info["character name"]))

fight = battle()
fight.startBattle(current_player, Player1, Player2)
