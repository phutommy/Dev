from operator import truediv
from re import T
import sys
import time
import random

def textreader():
  for letter in prompt:
    print(letter, end="")
    time.sleep(0.05)

def confused(entity):
    temp_int = entity.atk
    entity.atk = entity.dfen
    entity.dfen = temp_int

def createRandomEnemy():
  temp_int = random.randint (1, 3)
  if temp_int == 1:
      return Slime()
  if temp_int == 2:
      return Dog()
  if temp_int == 3:
      return Dragon()

class Hero:
  adventurer_name = "Hero"
  hp = 20
  attack = 1
  magic = 1
  dfen = 1
  

class Enemy:
  name = "unamed enemy"
  hp = 1
  atk = 1
  dfen = 1

class Slime(Enemy):
  name = "Slime"
  hp = random.randint(3,7)


class Dog(Enemy):
  name = "Dog"
  hp = random.randint(6,9)
  atk = 2

class Dragon(Enemy):
  name = "Dragon"
  hp = random.randint(15,20)
  atk = 4

foe = (Slime, Dog, Dragon)

##print(random.choice(enemy))

print("\n\n\n")

title_card = """
#################################################################################################
================================================================================================
#################################################################################################
 ________   ____  ____  _____  ___    _______    _______    ______    _____  ___      
|"      "\ ("  _||_ " |(\"   \|"  \  /" _   "|  /"     "|  /    " \  (\"   \|"  \     
(.  ___  :)|   (  ) : ||.\\   \    |(: ( \___) (: ______) // ____  \ |.\\   \    |    
|: \   ) ||(:  |  | . )|: \.   \\  | \/ \       \/    |  /  /    ) :)|: \.   \\  |    
(| (___\ || \\ \__/ // |.  \    \. | //  \ ___  // ___)_(: (____/ // |.  \    \. |    
|:       :) /\\ __ //\ |    \    \ |(:   _(  _|(:      "|\        /  |    \    \ |    
(________/ (__________) \___|\____\) \_______)  \_______) \"_____/    \___|\____\)    
                                                                                      
  _______  ___  ___    _______   ___        ______     _______    _______   _______   
 /"     "||"  \/"  |  |   __ "\ |"  |      /    " \   /"      \  /"     "| /"      \  
(: ______) \   \  /   (. |__) :)||  |     // ____  \ |:        |(: ______)|:        | 
 \/    |    \\  \/    |:  ____/ |:  |    /  /    ) :)|_____/   ) \/    |  |_____/   ) 
 // ___)_   /\.  \    (|  /      \  |___(: (____/ //  //      /  // ___)_  //      /  
(:      "| /  \   \  /|__/ \    ( \_|:  \\        /  |:  __   \ (:      "||:  __   \  
 \_______)|___/\___|(_______)    \_______)\"_____/   |__|  \___) \_______)|__|  \___) 
                                                                                      
#################################################################################################
================================================================================================
#################################################################################################


"""

##print(title_card)

player = Hero

adventurer_name = input("What is your name, adventurer? (Alphanumeric characters only, please.)\n");

print("\n\nWelcome to the dungeon, " + adventurer_name + "!")

valid_input_flag = False

prompt = "\n\nSelect a job (Pick a number):\n\n(1) Warrior\n\n(2) Mage\n\n"

while valid_input_flag == False:

    textreader()

    adventurer_job = input()

    if adventurer_job == "1":
        attack = 3
        magic = 1
        valid_input_flag = True

    elif adventurer_job == "2":
        attack = 1
        magic = 3
        valid_input_flag = True

    else:
        prompt = "\n\nSelect a job (Pick a VALID number, dummie):\n\n(1) Warrior\n\n(2) Mage\n\n"

print("\n")

enemy1 = createRandomEnemy()

ongoing_battle_flag = True

prompt = "\nHoly shit a " + str(enemy1.name) + " ambushed you but it's retarted. Select a physical or magic attack: (1) physical or (2) magic\n"

while ongoing_battle_flag == True:
  
  textreader()

  attack_type = input()

  if attack_type == "1":
    enemy1.hp = (enemy1.hp - attack)
    if enemy1.hp <= 0:
      ongoing_battle_flag = False
    prompt = "\nNice physical attack, but the" + str(enemy1) + "still has " + str(enemy1.hp) + " hp! Do another physical (1) or magic (2) attack!\n"

  if attack_type == "2":
    enemy1.hp = (enemy1.hp - magic)
    confused(enemy1)
    if enemy1.hp <= 0:
      ongoing_battle_flag = False
    prompt = "\nNice magic attack, but the" + str(enemy1) + "still has " + str(enemy1.hp) + " hp! Do another physical (1) or magic (2) attack!\n"

  if enemy1.hp > 0:
    player.hp = (player.hp - enemy1.atk)
    print("\nThe" + str(enemy1) + "attacks! You now have " + str(player.hp) + " hp!\n")

  else:
    prompt = "\n\nPick a VALID attack number, dummie):\n\n(1) physical\n\n(2) magic\n\n"

  if enemy1.hp <= 0:  
    print("\ncongrations u beat autismo" + str(enemy1) + "lel\n")
    print("\nYou currently have " + str(player.hp) + " hp.\n")
