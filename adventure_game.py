import time
import random
items = []
field = []
wrong_way = ("You rapidly realize you do NOT "
             "want to go THAT direction.\n")


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    landscape = random.choice(["brilliant orange poppies",
                               "ancient monolithic stones",
                               "writhing, innocuous snakes"])
    print_pause("You awake in the valley of an unfamiliar mountain range.")
    print_pause("Bewildered and laying in a field of")
    print_pause(" " + landscape + ", you struggle to remember")
    print_pause(" what events lead you to this place...")
    print_pause("Nearby, you see the entrance to a small cave.")
    print_pause("And, in the distance to the east, you spot a cottage.")
    field.append(landscape)


def arrival(choice, action, result):
    print_pause("You head towards the " + choice + ".")
    print_pause("You arrive and " + action + ".")
    print_pause(result)
    print_pause("What will you do next? \n")


def destination_choice(option1, option2, location):
    choice = input("Enter 1 to " + option1 + "\n"
                   "Enter 2 to " + option2 + "\n")
    if location == "field":
        if choice == "1":
            destination_cave()
        elif choice == "2":
            destination_cottage()
        else:
            print_pause(wrong_way)
            destination_choice("go to the cave", "go to the cottage", "field")
    elif location == "cottage":
        if choice == "1":
            destination_cottage_battle()
        elif choice == "2":
            choice = ("field of " + field[0] + "")
            arrival(choice, "collapse", "You tremble with fear and shame.")
            destination_choice("hide in the cave.",
                               "return and battle the evil unicorn.",
                               "field")
        else:
            print_pause(wrong_way)
            destination_choice("fight the evil unicorn!", "flee!", "cottage")
    elif location == "cave":
        if choice == "1":
            destination_cave()
        elif choice == "2":
            destination_cottage()
        else:
            print_pause(wrong_way)
            destination_choice("hide in the cave.",
                               "check out the cottage.",
                               "cave")


def destination_cave():
    choice = "cave"
    weapon = random.choice(["magical sword of rainbows",
                            "golden horn of oblivion",
                            "laser of laceration"])
    if items != []:
        action = "peer back into the small, still uninhabited grotto"
        result = "You find nothing new here."
    else:
        action = "peer into the small, uninhabited grotto"
        result = ("An object glints."
                  " Picking it up, you recognize the"
                  " " + weapon + ". \n"
                  "Still dazed, you wander back out to the field,"
                  " " + weapon + " in hand.")
        items.append(weapon)
    arrival(choice, action, result)
    destination_choice("hide in the cave.", "check out the cottage.", "cave")


def destination_cottage():
    choice = "cottage"
    action = ("knock on the weathered green door, \n"
              " which suddenly swings open..")
    result = ("An evil unicorn rears up and threatens you with a treacherous\n"
              " obsidion horn.")
    arrival(choice, action, result)
    destination_choice("fight the evil unicorn!", "flee!", "cottage")


def destination_cottage_battle():
    if items != []:
        weapon = items[0]
        print_pause("You wield your " + weapon + ".")
        print_pause("The evil unicorn's eyes bulge with fear.\n"
                    "Knowing his demise is imminent, "
                    "he bolts for the mountains!")
        print_pause("You are victorious!")
        new_game = input("Would you like to play again? (y/n)")
        if new_game == "y":
            print_pause("YOU are a true hero!\n")
            adventure_game()
        else:
            print_pause("Thank you for playing!\n")
    else:
        print_pause("Immediately, the folly of your haste registers.")
        print_pause("You have no weapon...no powers.")
        print_pause("You are no match for an evil unicorn, "
                    "and you flee to the cave!")
        destination_cave()


def adventure_game():
    intro()
    destination_choice("explore the cave.", "inquire at the cottage.", "field")


adventure_game()
