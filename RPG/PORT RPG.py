import time
import random
import sys

#################################################################################

def delay_print(narration, delay=0.05):
    """
    Print the text with a delay between characters.

    Parameters:
    - narration: The text that will be printed.
    - delay: Delay time between characters (default 0.05 seconds).

    - Fast = 0.0001
    - Slow = 0.01
    - Default = 0.05
    """
    for letter in narration:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)

################################################################################
        
def welcome_image():
    delay_print("""


                                     ==(W{==========-      /===-                        
                              ||  (.--.)         /===-_---~~~~~~~~~------____  
                              | \_,|**|,__      |===-~___                _,-' `
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~      
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`         
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'             
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'                
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                  \_|      /        _) | ;  ),   __--~~                        
                    '~~--_/      _-~/- |/ \   '-~ \                            
                   {\__--_/}    / \\_>-|)<__\      \                           
                   /'   (_/  _-~  | |__>--<__|      |                          
                  |   _/) )-~     | |__>--<__|      |                          
                  / /~ ,_/       / /__>---<__/      |                          
                 o-o _//        /-~_>---<__-~      /                           
                 (^(~          /~_>---<__-      _-~                            
                ,/|           /__>--<__/     _-~                               
             ,//('(          |__>--<__|     /  PortRPG  .----_          
            ( ( '))          |__>--<__|    |                 /' _---_~\        
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
        ,/,'//( (             \__>--<__\    \            /'  //        ||      
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
   ;'( ')/ ,)(                              ~~~~~~~~~~                         
  ' ') '( (/                                                                   
    '   '  `
           
          WELCOME TO PortRPG !! \n""", delay= 0.0001)


#################################################################################
""" Start menu.
    1: Start the game, this gets you into the choose character function (menu).
    2: About, shows you a drescription about the game and a few words of thanks.
    3. Exit, breaks the bucle and exit the game. 
"""
def start_menu():
    
    while True:
        delay_print("Select an Option:\n")
        delay_print("Play.   1\n")
        delay_print("About.  2\n")
        delay_print("Exit.   3\n")  

        start_menu = input(str())

        if start_menu == "1":
            delay_print("The game has started\n")
            choose_character()

        elif start_menu == "2":
            delay_print("ABOUT PortRPG")
            about()
            
        elif start_menu == "3":
            delay_print("You exit the game")
            break
        else:
            print("Invalid option")

#################################################################################
# A short description of the game.      
def about():
    delay_print( """
                        This is an rpg game where, 
                        you will choose your class,
                        buy weapons, fight with multiple monster 
                        in a dark dungeon, loot gold 
                        and find lot of fun.
                
                                        I made this RPG for my portfolio
                                        i hope you enjoy it, and consider
                                        my job and enthusiasm to be part
                                        of your team.
                                                        Thank you sincerely:
                                                                Marcial Bernal
          """, delay= 0.01)
        
##################################################################################
""" Choose character menu.
    In this menu, you choose the character, 
    an instance of the character in question is created, 
    the attributes are already predefined, then the character attributes are displayed 
    and the character actions menu is started.
"""    
def choose_character():

    while True:
        delay_print("Choose your character!:\n")
        delay_print("(M)age.\n")
        delay_print("(W)arrior.\n")
        delay_print("(A)rcher.\n") 
        delay_print("(B)ack to Menu.\n")     

        character_menu= input(str("Choose an option: \n")).lower()

        if character_menu == "m":
            delay_print("You choose the Mage. \n")
            mage = Mage("Merlin", 8, 14, 8, 8, 100, 25, 0)
            mage.skills()
            return mage.play_menu()          
                    
        elif character_menu == "w":
            delay_print("You choose the Warrior.\n")
            warrior = Warrior("Ragnar", 14, 8, 10, 14, 100, 25, 0)  
            warrior.skills()
            return warrior.play_menu()
   
        elif character_menu == "a":
            delay_print("You choose the Archer.\n")
            archer = Archer("Robin", 10, 10, 14, 10, 100,25, 0)
            archer.skills()
            return archer.play_menu()
        
        elif character_menu == "b":
            break
        
        else:
            delay_print("Invalid action")
    
#######################################################################################################
            

    
#######################################################################################################
# This is the main class for the characters to play, most of the functions depart from here.          
class Character:
   
    def __init__(self, name, strenght, intelligence, dextery, defense, health, gold):
        self.name = name
        self.strenght = strenght
        self.intelligence = intelligence
        self.dextery = dextery
        self.defense = defense
        self.health = health
        self.gold = gold
    
# Function made to control the fighting secuence in explore dungeon.    
    def alive(self):
        return self.health >= 1
    
 
    def death(self):
        self.health <= 0
        print(self.name, "Its Dead")

    
# This is the character actions menu.
# All the functions are inside the Character class
    def play_menu(self):
        while True:

            delay_print("Choose an Action\n")
            delay_print("(E)xplore Dungeons.\n")
            delay_print("(S)tore.\n")  
            delay_print("(I)nventory.\n")  
            delay_print("(H)ero Skills.\n")  
            delay_print("(B)ack.\n")

            play_menu = input(str("Select:\n")).lower()

            if play_menu == "e":
                self.explore_dungeon()
                
            elif play_menu == "s":
                self.shop_menu()

            elif play_menu == "i":
                self.show_inventory()

            elif play_menu == "h":
                self.skills()

            elif play_menu == "b":
                break
                
            else:
                delay_print("Invalid option")

        
    def explore_dungeon(self):

        delay_print("You enter the dungeon...\n")
        while True:
                     
            action = input("Do you want to (F)ight or (R)eturn to the actions menu? \n").lower()
            if action == 'f':
                enemy = generate_enemy()
                delay_print(f"{self.name}\n")
                delay_print(f"{self.health} HP\n")
                delay_print(f"An enemy {enemy.name} appears!\n")
                while self.alive() and enemy.alive():
                    delay_print("Player's turn:\n")
                    self.attack(enemy)
                    if not enemy.alive():
                        delay_print(f"You defeated the {enemy.name}!\n")
                        earned_gold = random.randint(1, 25)
                        delay_print(f"You earned {earned_gold} gold.\n")
                        self.gold += earned_gold
                        break
                    delay_print(f"{enemy.name}'s turn:\n")
                    enemy.attack(self)
                    if not self.alive():
                        delay_print("You were defeated!\n")
                        delay_print("GAME OVER")
                        sys.exit()
            elif action == 'r':
                break
            else:
                delay_print("Invalid option. Please enter 'F' or 'R'.")

# This is the function made for the fight sequence.
    def attack(self, enemy): 
        damage = self.damage(enemy)
        enemy.health = enemy.health - damage
        delay_print(f"{self.name} Has done, {damage} damage to {enemy.name}\n")
        if enemy.alive():
            delay_print(f"{enemy.name} health is: {enemy.health}\n")
        else:
            enemy.death() 


    def shop_menu(self):

        delay_print(f"Welcome to the Shop, {self.name}!\n")
        delay_print("Shop Menu:\n")
        for i, item in enumerate(shop_items, 1):
            delay_print(f"{i}. {item.name} - Price: {item.price} gold\n")

        choice = input("Enter the number of the item you want to buy (or 'exit' to leave the shop): \n")

        if choice.lower() == "exit":
            delay_print("Leaving the shop. Goodbye!\n")
            return False

        try:
            choice = int(choice)
            if 1 <= choice <= len(shop_items):
                selected_item = shop_items[choice - 1]
                buy_item(self, selected_item)
            else:
                delay_print("Invalid choice. Please enter a valid number.\n")
        except ValueError:
            delay_print("Invalid input. Please enter a number.\n")

        return True
    

    def show_inventory(self):
        delay_print(f"Inventory from {self.name}:\n")
        delay_print(f"You have {self.gold} gold\n")
        if self.inventory:
                delay_print(f"And a {self.inventory}\n")
        else:
            delay_print("The inventory its empty!\n")


    def skills(self):
        delay_print(f"{self.name}\n")
        delay_print(f"Strenght: {self.strenght}\n")
        delay_print(f"Intelligence: {self.intelligence}\n")
        delay_print(f"Dextery: {self.dextery}\n")
        delay_print(f"Defense: {self.defense}\n")
        delay_print(f"Health: {self.health}\n")

############################################################################################################
""" Function to buy items from the shop. 
    
    Arg: self: the Character choosen
         item: this is the item that where buy in the shop menu
       

    Return: Establish the bought weapon as the wepaon of the character, and  also add it to the inventory.
"""   
def buy_item(self, item):

    if self.gold >= item.price:
        self.gold -= item.price
        if item.weapon == True:
            self.weapon = item.damage
            self.inventory = item.name
            delay_print(f"You bought {item.name} for {item.price} gold and equipped it as your weapon.\n")

    else:
        delay_print("Not enough gold to buy this item.\n")

###########################################################################################################
""" Function to generate items. 
    
    Arg: name: (str) name of the item
         price: (int) price of the item in shop
         damage: (int) damage of weapon that will be aded to character damage
         weapon: (bool) It is to verify that it is a weapon and the character can equip it

    Return: An item object with their attributtes.
"""
class Item:
    def __init__(self, name, price, damage, weapon = True):
        self.name = name
        self.price = price
        self.damage = damage
        self.weapon = weapon

    """ I made the weapon attribute this way, in case in the future i wanted to add
            other types of items like potions, etc."""

##########################################################################################################
# A list of shop items, instantiated in a list 
shop_items = [
    Item("Great Axe", 25, 4),
    Item("Long Bow", 20, 4),
    Item("Magic Wand", 10, 4),
    Item("Diamond Sword", 100, 10)]

###########################################################################################################
"""These are the classes of heroes that you can choose, 
    they inherit from the parent class Character, 
    functions and attributes have been added, 
    some others have been modified.

    Inventory and Weapon has been aded to attributes.

    Skills now shows the inventory.

    For damage, a specific function has been created for each class, 
    because each one increases their attributes differently when equipping a weapon.

"""        
class Mage(Character):
    def __init__(self, name, strenght, intelligence, dextery, defense, health, gold, weapon):
        super().__init__(name, strenght, intelligence, dextery, defense, health, gold)
        self.weapon = weapon
        self.inventory = []

    def skills(self):
        super().skills()
        if self.inventory == []:
            delay_print("Weapon : You have no weapon yet\n")
        else:
            delay_print(f"Weapon: Plus {self.weapon} damage from {self.inventory}\n")
 
    def damage(self, enemy):
        if self.intelligence > enemy.defense:
            return self.intelligence + self.weapon - enemy.defense
        else:
            return 1
                
########################

class Warrior(Character):
    def __init__(self, name, strenght, intelligence, dextery, defense, health, gold, weapon):
        super().__init__(name, strenght, intelligence, dextery, defense, health, gold)
        self.weapon = weapon
        self.inventory = []

    def skills(self):
        super().skills()
        if self.inventory == []:
            delay_print("Weapon : You have no weapon yet\n")
        else:
            delay_print(f"Weapon: Plus {self.weapon} damage from {self.inventory}\n")

    def damage(self, enemy):
        if self.strenght > enemy.defense:
            return self.strenght + self.weapon - enemy.defense
        else:
            return 1
        
#########################

class Archer(Character):
    def __init__(self, name, strenght, intelligence, dextery, defense, health, gold, weapon):
        super().__init__(name, strenght, intelligence, dextery, defense, health, gold)
        self.weapon = weapon
        self.inventory = []

    def skills(self):
        super().skills()
        if self.inventory == []:
            delay_print("Weapon : You have no weapon yet\n")
        else:
            delay_print(f"Weapon: Plus {self.weapon} damage from {self.inventory}\n")

    def damage(self, enemy):
        if self.dextery > enemy.defense:
            return self.dextery + self.weapon - enemy.defense
        else:
            return 1

######################################################################################################

"""Function to be able instantiate enemies, 
    which inherits from the Character class,some attributes and functions."""

class Enemy(Character):
    def __init__(self, name, strenght, defense, health):
        self.name = name
        self.strenght = strenght
        self.defense = defense
        self.health = health

    def attack(self, enemy): 
        damage = self.damage(enemy)
        enemy.health = enemy.health - damage
        delay_print(f"{self.name} Has done {damage} damage to {enemy.name}\n")
        if enemy.alive():
            delay_print(f"{enemy.name} health is: {enemy.health}\n")
        else:
            enemy.death() 

    def damage(self, enemy):
        if self.strenght > enemy.defense:
            return self.strenght - enemy.defense
        else:
            return 1    

######################################################################################################

def generate_enemy():
    """ Function to generate random enemies 
     
        Arg: str list of enemies names

        Return: An enemy object with their attributtes.
    """
        
    enemy_names = ["Goblin", "Skeleton", "Orc", "Spider"]
    return Enemy(
        name=random.choice(enemy_names),
        strenght=random.randint(10, 20),
        defense= 2,
        health=50,)

    """ On this occasion I have left some attributes pre-established
         instead of using random, just for the purposes of testing the code."""

######################################################################################################


# This works to start the game.
welcome_image()
start_menu()


##########################