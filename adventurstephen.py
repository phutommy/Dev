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

print(title_card)

adventurer_name = input("What is your name, adventurer? (Alphanumeric characters only, please.)\n");

print("\n\nWelcome to the dungeon, " + adventurer_name + "!")

attack = -1

magic = -1

valid_input_flag = False

prompt = "\n\nSelect a class (Pick a number):\n\n(1) Warrior\n\n(2) Mage\n\n"

while valid_input_flag == False:

    adventurer_class = input(prompt)

    if adventurer_class == "1":
        attack = 3
        magic = 1
        valid_input_flag = True

    elif adventurer_class == "2":
        attack = 1
        magic = 3
        valid_input_flag = True

    else:
        prompt = "\n\nSelect a class (Pick a VALID number, dummie):\n\n(1) Warrior\n\n(2) Mage\n\n"

print("\n\n\n")