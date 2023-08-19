#!/usr/bin/python3

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



