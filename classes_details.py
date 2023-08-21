#!/usr/bin/python3

from classes import Warrior, Knight, character_class

classes = [
    ["Warrior", 11, 15, 9],
    ["Knight", 13, 7, 15]
        ]
#prints infos about the default stats of a class
def classes_details_printer(selected_class):
    for class_data in classes:
        if selected_class == class_data[0]:
            print("----------------------------------------------")
            print("Character class : ", selected_class)
            print("Base HP = ", class_data[1])
            print("Base Atk = ", class_data[2])
            print("Base Def = ", class_data[3])
            print("----------------------------------------------")



def callClass(player):
    if player["character class"] == "Warrior":
        player_ = Warrior(player)
    elif player["character class"] == "Knight":
        player_ = Knight(player)
    else:
        player_ = character_class(player)
    return player_
