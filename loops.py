#:/usr/bin/python3

from classes_details import classes_details_printer
import random
#character selection function
def character_selection(classes):
    while True:
        try:
            chara_class = int(input("Choose a class: "))
            if 1 <= chara_class <= len(classes):
                selected_class = classes[chara_class - 1]
                print(f"You have chosen the {selected_class} class")
                y_n = input(">> See details about the selected class (y/n) : ").lower()
                y_n = y_n[0]
                if y_n == "y":
                    classes_details_printer(selected_class)
                elif y_n == "n":
                    break
                else:
                    continue
                break
            else:
                print("Class does not exist")
        except ValueError:
            print("Invalid character")
    return selected_class

#sets the additional bonus points to the stats
def character_stats(chara_info):
    bonus_points = 15
    restart_flag = True
    while restart_flag:
        for key in chara_info:
            if key == "character class" or key == "character name":
                continue
            print("remaining points :", bonus_points)
            if bonus_points == 0:
                restart_flag = False
                break
            temp = int(input(f"{key}: "))
            if temp > bonus_points:
                print("not enough points")
            elif temp < 0:
                print("no negative stats")
            else:
                chara_info[key] += temp
                bonus_points -= temp
    return chara_info

classes_stats = [
    {"character class" : "Warrior",
    "character name" : "",
    "HP" : 11,
    "Atk" : 15,
    "Def" : 9},
    {
    "character class" : "Knight",
    "character name" : "",
    "HP" : 13,
    "Atk" : 7,
    "Def" : 15}
]
#function that sets the character stats
def addToClass(stats):
    for class_data in classes_stats:
        if stats["character class"] == class_data["character class"]:
            stats["HP"] += class_data["HP"]
            stats["Atk"] += class_data["Atk"]
            stats["Def"] += class_data["Def"]
    return stats

npc_name = ["Alora", "Anya", "Basil", "Cassia", "Dorian",
            "Ember", "Fiona", "Gwyn", "Halia", "Iris",
            "Jasmine", "Kira", "Lyra", "Mia", "Nadia",
            "Onyx", "Piper", "Quinn", "Rhea", "Sage",
            "Talia", "Valeria", "Willow"]

npc_infos = {
    "character class" : "",
    "character name" : "",
}
npc_states = {
    "HP" : 0,
    "Atk" : 0,
    "Def" : 0
}
classes = ["Warrior", "Knight"]
#NPC character creator
def npcMaker():
    r_states = 15
    npc_infos["character class"] = random.choice(classes)
    npc_infos["character name"] = random.choice(npc_name)
    for char_stats in classes_stats:
        if char_stats["character class"] == npc_infos["character class"]:
            npc_states["HP"] = char_stats["HP"]
            npc_states["Atk"] = char_stats["Atk"]
            npc_states["Def"] = char_stats["Def"]
            break

    while r_states > 0:
        random_attribute = random.choice(list(npc_states.keys()))
        attribute_value = random.randint(1, r_states)
        npc_states[random_attribute] += attribute_value
        r_states -= attribute_value
        if r_states == 0:
            break
    npc = {**npc_infos, **npc_states}
    return npc
