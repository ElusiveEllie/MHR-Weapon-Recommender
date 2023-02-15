from elements import WeaponTree, WeaponDict, mhr_weapons

element_list = []
for weapon in mhr_weapons.weapons:
    if mhr_weapons.weapons[weapon].element not in element_list:
        element_list.append(mhr_weapons.weapons[weapon].element)

weapon_type_list = ["Greatsword", "Long Sword", "Sword & Shield", "Dual Blades", "Lance", "Gunlance", "Hammer", "Hunting Horn", "Switch Axe", "Charge Blade", "Insect Glaive"]

print("Type in the first few letters of the element or affliction damage type you want to deal.")

element_input = str(input("\n")).title()

temp_element_list = element_list.copy()
while len(temp_element_list) > 1:
    match_list = []
    for element in temp_element_list:
        if len(element_input) <= len(element):
            if element[0:len(element_input)] == element_input:
                match_list.append(element)
    if len(match_list) > 1:
        print("Possible matches are:")
        for match in match_list:
            print(match)
        print("\nTo continue, refine your search.")
        print("Type in the first few letters of the element or affliction damage type you want to deal.")
        element_input = str(input("\n")).title()
    elif len(match_list) == 0:
        print("No matches found.")
        print("Type in the first few letters of the element or affliction damage type you want to deal.")
        element_input = str(input("\n")).title()
    else:
        print(f"\nThe only element or affliction that matches is {match_list[0]}. Would you like to look for weapons of the {match_list[0]} element or affliction?")
        print("Enter 'Y' or 'N' to continue:")
        y_or_n = str(input("\n")).title()
        while y_or_n != "Y" and y_or_n != "N":
            print("Input not recognized. Please input 'Y' or 'N'.")
            y_or_n = str(input("\n")).title()
        if y_or_n == "Y":
            element_input = match_list[0]
            temp_element_list = match_list
        else:
            print("\nType in the first few letters of the element or affliction damage type you want to deal.")
            element_input = str(input("\n")).title()

print("\nType in the first few letters of the weapon type you want to use.")

weapon_type_input = str(input("\n")).title()

temp_weapon_type_list = weapon_type_list.copy()
while len(temp_weapon_type_list) > 1:
    match_list = []
    for weapon_type in temp_weapon_type_list:
        if len(weapon_type_input) <= len(weapon_type):
            if weapon_type[0:len(weapon_type_input)] == weapon_type_input:
                match_list.append(weapon_type)
    if len(match_list) > 1:
        print("Possible matches are:")
        for match in match_list:
            print(match)
        print("\nTo continue, refine your search.")
        print("Type in the first few letters of the weapon type you want to use.")
        weapon_type_input = str(input("\n")).title()
    elif len(match_list) == 0:
        print("No matches found.")
        print("Type in the first few letters of the weapon type you want to use.")
        weapon_type_input = str(input("\n")).title()
    else:
        print(f"\nThe only weapon type that matches is {match_list[0]}. Would you like to look {match_list[0]} weapons?")
        print("Enter 'Y' or 'N' to continue:")
        y_or_n = str(input("\n")).title()
        while y_or_n != "Y" and y_or_n != "N":
            print("Input not recognized. Please input 'Y' or 'N'.")
            y_or_n = str(input("\n")).title()
        if y_or_n == "Y":
            weapon_type_input = match_list[0]
            temp_weapon_type_list = match_list
        else:
            print("\nType in the first few letters of the weapon type you want to use.")
            weapon_type_input = str(input("\n")).title()

recommendation_list = []
for weapon in mhr_weapons.weapons:
    if mhr_weapons.weapons[weapon].element == element_input:
        if weapon_type_input in mhr_weapons.weapons[weapon].weapons:
            recommendation_list.append(mhr_weapons.weapons[weapon].name)

if not recommendation_list:
    print(f"\nThere are no {element_input} weapons in the {weapon_type_input} weapon tree.")
else:
    print(f"\n{element_input} weapons in the {weapon_type_input} weapon tree are:")
    for weapon in recommendation_list:
        print(weapon)