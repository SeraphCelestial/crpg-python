import random

# Player Characters
class Player:
    def __init__(self, health, strength, defence, manaStrength, mana, gold, experiencePoints, level):
        self.health = health
        self.strength = strength
        self.defence = defence
        self.manaStrength = manaStrength
        self.mana = mana
        self.gold = gold
        self.experiencePoints = experiencePoints
        self.level = level

warrior = Player(20, 3, 3, 0, 0, 0, 0, 1)
mage = Player(1, 3, 1, 5, 20, 0, 0, 1)
rouge = Player(10, 5, 1, 0, 0, 0, 0, 1)

# Weapons
class Weapon:
    def __init__(self, name, pluralName, damage, manaUse, quantity, inventoryQuantity):
        self.name = name
        self.pluralName = pluralName
        self.damage = damage
        self.manaUse = manaUse
        self.quantity = quantity
        self.inventoryQuantity = inventoryQuantity

rustySword = Weapon("Rusty Sword", "Rusty Swords", 1, 0, 1, 1)
oldStaff = Weapon("Old Staff","Old Staffs", 1, 2, 1, 1)
rustyDagger = Weapon("Rusty Dagger", "Rusty Daggers", 1, 0, 1, 1)

#Items
class Item:
    def __init__(self, name, pluralName, quantity, inventoryQuantity):
        self.name = name
        self.pluralName = pluralName
        self.quantity = quantity
        self.inventoryQuantity = inventoryQuantity

tornFabric = Item("Piece of Torn Fabric", "Pieces of Torn Fabric", 1, 0)
bone = Item("Bone", "Bones", 1, 0)
spiderEye = Item("Spider Eye", "Spider Eyes", 1, 0)

# Enemies
class Enemy:
    def __init__(self, name, health, strength, defence, loot):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.loot = loot

goblin = Enemy("Goblin", 5, 3, 2, tornFabric)
skeleton = Enemy("Skeleton", 8, 5, 2, bone)
spider = Enemy("Spider", 10, 7, 4, spiderEye)
null = Enemy("", 0, 0, 0, 0)

#Quests
class Quest:
    def __init__(self, name, description, completionStatus, loot):
        self.name = name
        self.description = description
        self.completionStatus = completionStatus
        self.loot = loot

killSkeletons = Quest("Kill Skeletons", "Kill 5 of the Skeletons that are in the Dark Forest", "Not Started", rustySword)
killGoblins = Quest("Kill Goblins", "Kill 5 of the Goblins that have taken over the Forest Path.", "Not Started", oldStaff)
null = Quest("", "", "", 0)

#Locations
class Location:
    def __init__(self, name, description, enemy, locToNorth, locToSouth, locToEast, locToWest, ogEnemy, quest):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.ogEnemy = ogEnemy
        self.quest = quest
        
darkForest = Location("Dark Forest", "A dense forest packed with tall evergreens on all sides. Looking up, one can barely see the sun through the thick needles.", skeleton, None, None, None, None, skeleton, killSkeletons)
forestPath = Location("Forest Path", "A path covered in stones, grass, and dirt that leads into the deep forest.", goblin, None, None, None, None, goblin, killGoblins)
home = Location("Home", "This is your home. It's quite barren.", null, None, None, None, None, null, null)
null = Location("", "", 0, 0, 0, 0, 0, 0, 0) 

setattr(darkForest, "locToNorth", null)
setattr(darkForest, "locToSouth", forestPath)
setattr(darkForest, "locToEast", null)
setattr(darkForest, "locToWest", null)

setattr(forestPath, "locToNorth", darkForest)
setattr(forestPath, "locToSouth", home)
setattr(forestPath, "locToEast", null)
setattr(forestPath, "locToWest", null)

setattr(home, "locToNorth", forestPath)
setattr(home, "locToSouth", null)
setattr(home, "locToEast", null)
setattr(home, "locToWest", null)

#Inventory Creator
inventory = []

#Quest List Creator
quests = []

# Misc. Scripts
def GameOver(character):
    if character[0].health < 1:
        print("You died.")
        print("Thank you for playing!")
        exit()

def HeroSelect():
    global defaultWeapon
    global characterName
    global character
    global currentLocation
    print("Initializing CRPG v0.0.6\n")
    print("Select your hero!")
    heroSelection = input("1. Warrior\n2. Mage\n3. Rouge\n>>> ")
    if heroSelection == "1":
        character = warrior
        characterName = input("What is your name, Warrior?\n>>> ")
        print("You are now", characterName, "the Warrior! Here are your stats...")
        print("Health:", character.health)
        print("Strength:", character.strength)
        print("Defence:", character.defence)
        print("Your starting weapon is a Rusty Sword.\n")
        defaultWeapon = rustySword
        inventory.append(rustySword)
        currentLocation = home
        return character, characterName, currentLocation
    elif heroSelection == "2":
        character = mage
        characterName = input("What is your name, Mage?\n>>> ")
        print("You are now", characterName, "the Mage! Here are your stats...")
        print("Health:", character.health)
        print("Strength:", character.strength)
        print("Mana Strength:", character.manaStrength)
        print("Defence:", character.defence)
        print("Mana:", character.mana)
        print("Your starting weapon is an Old Staff.\n")
        defaultWeapon = oldStaff
        inventory.append(oldStaff)
        currentLocation = home
        return character, characterName, currentLocation
    elif heroSelection == "3":
        character = rouge
        characterName = input("What is your name, Rouge?\n>>> ")
        print("You are now", characterName, "the Rouge! Here are your stats...")
        print("Health:", character.health)
        print("Strength:", character.strength)
        print("Defence:", character.defence)
        print("Your starting weapon is a Rusty Dagger.\n")
        defaultWeapon = rustyDagger
        inventory.append(rustyDagger)
        currentLocation = home
        return character, characterName, currentLocation
    else:
        print("That hero doesn't exist. Please choose again.\n")
        HeroSelect()    

def Game():
    print("Welcome", characterName, "to the world of Bjork!\nType 'help' for a list of commands to get started.\n")
    global currentLocation
    while character[0].health > 0:
        playerInput = input(">>> ")
        if playerInput == "help" or playerInput == "h":
            print("Command List:\nhelp (h): Displays this help list.\nnorth (n): Moves you to the north.\nsouth (s): Moves you to the south.\neast (e): Moves you to the east.\nwest (w): Moves you to the west.\ninventory (i): Displays your current inventory.\nlook (l): Displays information about your current surroundings.\nattack (a): Will cause you to attack an enemy of your choice.\nstats (st): Displays your current stats, amount of gold, level, and experience points.\nexit: Quits the game.")
        elif playerInput == "inventory" or playerInput == "i":
            for i in inventory:
                if i.inventoryQuantity == 1:
                    print(i.inventoryQuantity, i.name)
                else:
                    print(i.inventoryQuantity, i.pluralName)
        elif playerInput == "look" or playerInput == "l":
            print(currentLocation.name)
            print(currentLocation.description)
            if currentLocation.enemy.name == "":
                print("There doesn't seem to be anything nearby.")
            else:
                print("There seems to be a", currentLocation.enemy.name,"nearby.")
        elif playerInput == "north" or playerInput == "n":
            if currentLocation.locToNorth != null:
                setattr(currentLocation, "enemy", currentLocation.ogEnemy)
                currentLocation = currentLocation.locToNorth
                QuestChecker()
            else:
                print("You cannot move north.")
        elif playerInput == "south" or playerInput == "s":
            if currentLocation.locToSouth != null:
                setattr(currentLocation, "enemy", currentLocation.ogEnemy)
                currentLocation = currentLocation.locToSouth
                QuestChecker()
            else:
                print("You cannot move south.")
        elif playerInput == "east" or playerInput == "e":
            if currentLocation.locToEast != null:
                setattr(currentLocation, "enemy", currentLocation.ogEnemy)
                currentLocation = currentLocation.locToEast
                QuestChecker()
            else:
                print("You cannot move east.")
        elif playerInput == "west" or playerInput == "w":
            if currentLocation.locToWest != null:
                setattr(currentLocation, "enemy", currentLocation.ogEnemy)
                currentLocation = currentLocation.locToWest
                QuestChecker()
            else:
                print("You cannot move west.")
        elif playerInput == "attack" or playerInput == "a":
            print("You ready your", defaultWeapon.name, " and are ready to attack.")
            attackChoice = input("What do you see?\n>>> ").lower()
            if attackChoice == currentLocation.enemy.name.lower() and attackChoice != "null":
                global enemy
                enemy = currentLocation.enemy
                BattleState()
            else:
                print("You cannot see anything that would be worth attacking. You lower your", defaultWeapon.name)
        elif playerInput == "stats" or playerInput == "st":
            print("Health:", character[0].health)
            print("Strength:", character[0].strength)
            if character[0] == mage:
                print("Mana Strength:", character[0].manaStrength)
                print("Mana:", character[0].mana)
            print("Defence:", character[0].defence)
            print("Gold:", character[0].gold)
            print("Experience Points:", character[0].experiencePoints)
            print("Level:", character[0].level)
        elif playerInput == "quests" or playerInput == "q":
            print("Current Quests:\n")
            for q in quests:
                print(q.name, "\n", q.description, "\n", q.completionStatus, "\n")
        elif playerInput == "exit":
            print("Are you sure you want to exit? Your current progress will not be saved.")
            choice = input(">>> ")
            if choice == "yes" or choice == "y":
                exit()
            elif choice == "no" or choice == "n":
                Game()
            else:
                Game()
        else:
            print("These instructions don't make sense. You don't have any idea what to do")

def QuestChecker():
    global character
    global currentLocation
    if currentLocation.quest != null:
        quests.append(currentLocation.quest)
        print("You have gained a new quest! Check your quest log.")

def BattleState():
    global enemy
    print("A wild", enemy.name, "has appeared!")
    print("You have three options.")
    while enemy.health > 0:
        choice = input("1. Physical Attack\n2. Magic Attack\n3. Run Away\n>>> ")
        if choice == "1":
            print("You use your", defaultWeapon.name, "to attack the", enemy.name)
            hitChance = random.randint(0, 10)
            if hitChance >= 3:
                enemy.health = enemy.health - character[0].strength
                if enemy.health > 0:
                    print("You have hit the", enemy.name, "! It is now at", enemy.health, "health.")
                    character[0].health = character[0].health - (enemy.strength / character[0].defence)
                    if character[0].health <= 0:
                        print("The", enemy.name, "attacks you! You now have 0 health.")
                        GameOver(character)
                    else:
                        print("The", enemy.name, "attacks you! You now have", int(round(character[0].health)), "health.")
                else:
                    if enemy.name == "Goblin":
                        enemy.health = 5
                    elif enemy.name == "Skeleton":
                        enemy.health = 8
                    elif enemy.name == "Spider":
                        enemy.health = 10
                    setattr(currentLocation, "enemy", null)
                    print("You have defeated the", enemy.name)
                    goldQuantity = random.randint(1, 5)
                    print("You have recieved", goldQuantity,"gold.")
                    setattr(character[0], "gold", character[0].gold + goldQuantity)
                    expQuantity = random.randint(1, 5)
                    print("You have gained", expQuantity, "experience points!")
                    setattr(character[0], "experiencePoints", character[0].experiencePoints + expQuantity)
                    if character[0].experiencePoints >= 100:
                        print("You've gained 1 level!")
                        setattr(character[0], "level", character[0].level + 1)
                        setattr(character[0], "experiencePoints", 0)
                        lootChance = random.randint(0, 10)
                        if lootChance >= 3:
                            print("It seems to have left something behind.")
                            quantityChance = random.randint(1, 5)
                            if enemy.loot.inventoryQuantity <= 0:
                                setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                inventory.append(enemy.loot)
                            else:
                                setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                            if quantityChance == 1:
                                print("You found", quantityChance , enemy.loot.name)
                            else:
                                print("You found", quantityChance , enemy.loot.pluralName)
                            break
                    else:
                        lootChance = random.randint(0, 10)
                        if lootChance >= 3:
                            print("It seems to have left something behind.")
                            quantityChance = random.randint(1, 5)
                            if enemy.loot.inventoryQuantity <= 0:
                                setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                inventory.append(enemy.loot)
                            else:
                                setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                            if quantityChance == 1:
                                print("You found", quantityChance , enemy.loot.name)
                            else:
                                print("You found", quantityChance , enemy.loot.pluralName)
                            break
            else:
                print("Your", defaultWeapon.name, "slips from your grasp! You fumble and miss.")
                print("The", enemy.name, "hits you for full damage.")
                character[0].health = character[0].health - enemy.strength
                if character[0].health <= 0:
                    print("You now have 0 health.")
                    GameOver(character)
                else:
                    print("You now have", int(round(character[0].health)), "health.")
        elif choice == "2":
            if character[0] != mage:
                print("You are incapable of using magic. Try something else.")
            else:
                if character[0].mana == 0:
                    print("You have ran out of mana. You cannot attack with magic right now.")
                else:
                    print("You conjur a magical blast to attack the", enemy.name)
                    hitChance = random.randint(0, 10)
                    if hitChance > 3:
                        enemy.health = enemy.health - character[0].manaStrength
                        character[0].mana = character[0].mana - 2
                        if enemy.health > 0:
                            print("You have hit the", enemy.name, "! It is now at", enemy.health, "health.")
                            print("You now have", character[0].mana, "mana left.")
                            character.health = character[0].health - (enemy.strength / character[0].defence)
                            if character[0].health <= 0:
                                print("The", enemy.name, "attacks you! You now have 0 health.")
                                GameOver(character)
                            else:
                                print("The", enemy.name, "attacks you! You now have", int(round(character[0].health)), "health.")
                        else:
                            if enemy.name == "Goblin":
                                enemy.health = 5
                            elif enemy.name == "Skeleton":
                                enemy.health = 8
                            elif enemy.name == "Spider":
                                enemy.health = 10
                            setattr(currentLocation, "enemy", null)
                            print("You have defeated the", enemy.name)
                            print("You now have", character[0].mana, "mana left.")
                            goldQuantity = random.randint(1, 5)
                            print("You have recieved", goldQuantity,"gold.")
                            setattr(character[0], "gold", character[0].gold + goldQuantity)
                            expQuantity = random.randint(1, 5)
                            print("You have gained", expQuantity, "experience points!")
                            setattr(character[0], "experiencePoints", character[0].experiencePoints + expQuantity)
                            if character[0].experiencePoints >= 100:
                                print("You've gained 1 level!")
                                setattr(character[0], "level", character[0].level + 1)
                                setattr(character[0], "experiencePoints", 0)
                                lootChance = random.randint(0, 10)
                                if lootChance >= 3:
                                    print("It seems to have left something behind.")
                                    quantityChance = random.randint(1, 5)
                                    if enemy.loot.inventoryQuantity <= 0:
                                        setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                        inventory.append(enemy.loot)
                                    else:
                                        setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                    if quantityChance == 1:
                                        print("You found", quantityChance , enemy.loot.name)
                                    else:
                                        print("You found", quantityChance , enemy.loot.pluralName)
                                    break
                            else:
                                lootChance = random.randint(0, 10)
                                if lootChance >= 3:
                                    print("It seems to have left something behind.")
                                    quantityChance = random.randint(1, 5)
                                    if enemy.loot.inventoryQuantity <= 0:
                                        setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                        inventory.append(enemy.loot)
                                    else:
                                        setattr(enemy.loot, "inventoryQuantity", enemy.loot.inventoryQuantity + quantityChance)
                                    if quantityChance == 1:
                                        print("You found", quantityChance , enemy.loot.name)
                                    else:
                                        print("You found", quantityChance , enemy.loot.pluralName)
                                    break
                    else:
                        print("The magic you summoned was too strong to control! It completely misses the", enemy.name, "and throws you off balance.")
                        print("The", enemy.name, "hits you for full damage.")
                        character[0].health = character[0].health - enemy.strength
                        if character[0].health <= 0:
                            print("You now have 0 health.")
                            GameOver(character)
                        else:
                            print("The", enemy.name, "attacks you! You now have", int(round(character[0].health)), "health.")
        elif choice == "3":
            print("You try to run away from the", enemy.name)
            runChance = random.randint(1, 10)
            if runChance > 3:
                print("You get away from the", enemy.name, "successfully!")
                break
            else:
                print("You trip and fall while running. The", enemy.name, "catches up to you.")
                print("It hits you for full damage.")
                character[0].health = character[0].health - enemy.strength
                if character[0].health <= 0:
                    print("You now have 0 health.")
                    GameOver(character)
                else:
                    print("The", enemy.name, "attacks you! You now have", character[0].health, "health.")
        else:
            print("That is not a valid option. Choose again.")
            
character = HeroSelect()
Game()
