
import random

'''
A short text based adventure that takes place in a post-apocalyptic world. You as the player will have 10 chances to find
food for your survivor camp. You can search for a weapon, fight enemies, and collect food for your camp. The Player
can engage a few different enemies from hostile humans to zombies.



'''


class Player(): #player class holds adventure name, hp, weapon, max Damage, food found, and number of kills
    
    #player class var.
    def __init__(self, playerName, playerHp, weaponType,weaponDamage, food,kills):
        self.name = playerName
        self.hp = playerHp
        self.weapon = weaponType
        self.weaponDmg = weaponDamage
        self.food = food
        self.kills = kills
        
    def __repr__(self): #prints out player info
        return "Name: {} \nHealth: {} \nWeapon Equipped: {} \nMax Damage: {} \nFood Found: {} \nNumber of Kills: {} \n".format(self.name,self.hp,self.weapon,self.weaponDmg,self.food,self.kills)
        
    def getName(self): #gets players name
        return self.name
    
    def getHp(self): #gets players hp
        return self.hp
    
    def getWeapon(self): #gets players current weapon
        return self.weapon
    
    def getWeaponDmg(self): #gets players current weapon max damage.
        return self.weaponDmg
    
    def getFood(self): #gets player food.
        return self.food
    
    def getKills(self): #gets players kill count
        return self.kills
    
    def setName(self, newName): #sets player new name na
        self.name = newName
        
    def setHp(self, newHp):#sets the players hp 
        self.hp = self.hp - newHp
        
    def setWeapon(self,newWeapon): #sets the players new weapon
        self.weapon = newWeapon
        
    def setWeaponDmg(self,newDamage): #sets the players new max damage.
        self.weaponDmg = newDamage
        
    def setFood(self,food): #sets the new amount of food for player
        self.food = self.food + food
        
    def setKills(self,kill): #sets players new kills after getting kill
        self.kills += kill
        
    def randomDamage(self): #Creates a random damage based off the equipped weapon..
        dmgAmount = random.randrange(0,self.weaponDmg + 1)
        return dmgAmount
        
        
class Weapon(): #weapon class holds name, and amount of max damage.
    
    #Weapon class var.
    def __init__(self, weaponName, weaponDmg):
        self.name = weaponName
        self.damage = weaponDmg
        
    def __repr__(self): #for display purposes.
        return "{}, {}".format(self.name,self.damage)
        
    def getWeaponName(self):#gets the weapon name.
        return self.name
    
    def getWeaponDmg(self): #gets the weapons damage.
        return self.damage
    
    def setWeaponName(self, newWeapon): #set the a weapons new name.
        self.name = newWeapon
        
class Enemy(): #Enemy class holds enemy name, descrtiption, Hp, and max damage.
    
    #enemy class vars.
    def __init__(self, enemyName, enemyDescription,enemyHp, enemyDmg):
        self.enemyName = enemyName
        self.enemyHp = enemyHp
        self.enemyDescription = enemyDescription
        self.enemyDmg = enemyDmg
               
    def __repr__(self):#would print out class info.
        return "{}, {}, {}, {}".format(self.enemyName, self.enemyDescription,self.enemyHp, self.enemyDmg)
        
    def getEnemyName(self): #Gets enemy name
        return self.enemyName
    
    def getEnemyDescription(self): #get enemy description.
        return self.enemyDescription
    
    def getEnemyHp(self): #get enemy hp
        return self.enemyHp
    
    def getEnemyDamageDeal(self):  #get the enemy max damage.   
        return self.enemyDmg
    
    def setEnemyHp(self, newHp): #sets the enemy new hp.
        self.enemyHp = self.enemyHp - newHp
        
    def randomDamage(self): #Creates zombies random damage based off the enemy.
        dmgAmount = random.randrange(0,self.enemyDmg + 1)
        return dmgAmount
    

def enemiesAttacking():  #When user is attacked this function is called, grabs random enemy object and returns it.
    femaleZombie = Enemy("Female Zombie","Her cloths are tattered, shes missing an arm. \n", 50,5)#female zombie obj
    maleZombie = Enemy("Male Zombie", "His cloths are ripped, he stares at you..hungrily. \n" , 50,10)#Male zombie obj
    hostileMaleHuman = Enemy("Hostile Man", "He has a crazy look in his eyes. \n",75,20)#hositle Man Obj
    hostileFemaleHuman = Enemy("Hostile Female","Hair tied back in a bun, shes wearing tactical gear with a bat. \n",75,15)#Hostile female Obj
    enemyList = [femaleZombie, maleZombie, hostileMaleHuman, hostileFemaleHuman] # each obj in a list
    theEnemy =random.choice(enemyList)#randomly chooses an enemy obj from list.
    return theEnemy #returns random choice 

def weaponChoices(playerObject): #Weapon function objects to list. Returns list to lootChoices function.
    leadPipe = Weapon("Leadpipe",20)#lead pip obj
    pistol = Weapon("Pistol",50) #pistol obj
    baseballBat = Weapon("Baseball Bat", 25)#baseballbat obj
    fryingPan = Weapon("Frying Pan", 30)#frying pan obj
    shotgun = Weapon("Shotgun",75)#shotgun obj
    weaponList = [leadPipe,pistol,baseballBat,fryingPan,shotgun] #list of random weapons
    return weaponList #returns list of weapons to lootChoices Function

def lootChoices(playerObject): #function randomly chooses a weapon found from WeaponChoices function
    weaponList = weaponChoices(playerObject)   #Gets weapon list from weaponChoices function.   
    loot =random.choice(weaponList) #randomly chooses a weapon from list.
    return loot #returns to lootFound function
    
def lootFound(playerObject): #If randomly selected funtion gets allows users to choose to equip or not. 
    dropLoot = lootChoices(playerObject) #Gets choice from lootchoices function.
    if dropLoot.getWeaponName() == playerObject.getWeapon():#if  user has the weapon do nothing
        return nothingFound() #return nothing found if user already has weapon.
    else:
        pickWeaponUp = 'n'  #initial var for choice
        print(randomSearchSpots())#prints a random search spot
        #user input if they want to pick up weapon y for yes and n for no.
        pickWeaponUp = input("You found {} would you like to \nswtich your current weapon for it? (y or n) ".format(dropLoot.getWeaponName()))
        if pickWeaponUp == 'n' :#if users types n
            return "You continue to use {}. ".format(playerObject.getWeapon()) #prints user decided to keep current weapon
        elif pickWeaponUp =='y' :#if users type y
            playerObject.setWeapon(dropLoot.getWeaponName())#gets weapon name from class and sets it to player
            playerObject.setWeaponDmg(dropLoot.getWeaponDmg())#gets weapon max damage from class and sets to players
            return "You equipped {}. ".format(dropLoot.getWeaponName())#prints out the weapon name
        else: #easter egg if users didnt type y/n prints If mistakes are made cant go easy on player all the time.
            return "You took to long to decide, and don't \nremember where you seen it! Next time press (y / n) " # poke fun of mistypes
            

def randomEvent(playerObject): #gets random event and returns
    eventHappening = random.choice([nothingFound,randomAmountFoodFound,randomAttack,lootFound])   #list of random events.
    if eventHappening == nothingFound:#if nothing found 
        return eventHappening()
    else: #if anthing else if found
        return eventHappening(playerObject)

def randomAmountFoodFound(playerObject): #function for random amount of food found. 
    foodFound = random.randrange(1,10 + 1)  #Gets a random amount from 1 and 10
    food = foodFound #puts foodfound into a variable. 
    playerObject.setFood(food) #sets new amount of food in player class
    print(randomSearchSpots()) #prints out random search spot.
    return ("You found {} cans of food.".format(foodFound) )  #returns out the amount of food found. 

def nothingFound(): #function called if nothing is found. 
    print(randomSearchSpots()) #sends out random search spots. 
    return "You find nothing." #prints out string

def randomSearchSpots(): #gets a random seach spot. 
    listOfSearchables = ["tool box", "lock box", "car", "old purse", "cubbord", "run down store", "apartment", "body", "old camp"]#list of random searchable things. 
    searched = random.choice(listOfSearchables) #chooses a random spot from list. 
    return "You searched {}: ".format(searched) #prints out the random search item. 

def battle(attackingThing,playerObject): #battle function called if users gets random enenmy encounter.
    while (attackingThing.getEnemyHp() > 0) and (playerObject.getHp() > 0): #while player is alive and enemy is alive. Run the battle seq.
        fightOrFlight = input("Do you want to fight or Run? ( f / r ) ") #ask user if they want to fight or run.
        if fightOrFlight == 'f' : #if user chose fight.
            #playerHitEnemy = random.randrange(0,playerObject.getWeaponDmg() + 1) #calculates damage player does to enemy  based off weapon.
            playerHitEnemy = playerObject.randomDamage()
            print("You hit the {} using your {} dealing {} damage! ".format(attackingThing.getEnemyName(),playerObject.getWeapon(),playerHitEnemy))#prints out amaount of damage player dealt
            attackingThing.setEnemyHp(playerHitEnemy)#sets enemies new hp
            if attackingThing.getEnemyHp() > 0: #if the enemy is not dead it attacks back.
                enemyHitPlayer = attackingThing.randomDamage() #enemy hits player random amount damage based off enemy.
                print("{} hit you dealing {} amount of damage! ".format(attackingThing.getEnemyName(),enemyHitPlayer))#prints out that amount of damage.
                playerObject.setHp(enemyHitPlayer) #sets players new hp.
                print("Your remaining health is {}! ".format(playerObject.getHp()))  #prints out users health.                                    
        elif fightOrFlight == 'r' :  #if player chose to run
            youGotAway = "You were able to get away!" #String for getting away
            didntGetAway = "You were not able to get away!"       #String  if player did not get away
            escape = random.choice([youGotAway, didntGetAway]) #chooses random string.
            if escape == youGotAway: #if you got away  
                attackingThing.setEnemyHp(0) #sets current enemy to dead 
                return youGotAway #returns got away string. 
            else:  #if you didnt 
                print(didntGetAway) #prints out you didnt get away 
                enemyHitPlayer = attackingThing.randomDamage() #enemy hits player random amount damage based off enemy.
                print("{} hit you dealing {} amount of damage! ".format(attackingThing.getEnemyName(),enemyHitPlayer)) #displays damage amount. 
                playerObject.setHp(enemyHitPlayer) #sets users new hp 
                print("Your remaining health is {}! \n".format(playerObject.getHp())) #displays new hp.
    else:  #when player dies or enemy dies.              
        if attackingThing.getEnemyHp() <= 0: #if enemy dies
            playerObject.setKills(1) #sets kill count  +1
            lineBreak() #creates a line break 
            return "{} has died, We made alot of noise lets move on! ".format(attackingThing.getEnemyName()) #displays enemy killed text.                  
        elif playerObject.getHp() <= 0: #if player dies.
            lineBreak() #creates a line break
            return "{} has killed you! ".format(attackingThing.getEnemyName()) #Displays enemy that killed you.         
                 
def randomAttack(playerObject): #function called with inital random event. 
    attackingThing = enemiesAttacking() #gets the attacking enemy from function enemiesAttacking.
    attackingThingName = attackingThing.getEnemyName() #Gets the attacking enemy name stores  in own var. 
    if attackingThingName == "Female Zombie" or attackingThingName == "Male Zombie": #If either is  zombie
        return randomZombieAttack(attackingThing,playerObject)     #sends to randomZombieAttack function.
    elif attackingThingName == "Hostile Man" or attackingThingName == "Hostile Female": #if either human
        return randomHumanAttack(attackingThing,playerObject) # sends to randomHumanAttack function
    else: 
        return "Yikes"
  
def randomZombieAttack(attackingThing,playerObject):#if a zombie was chosen from random event
    print("You hear shuffleing and groans. \nAs you turn you are greeted by a {}".format(attackingThing.getEnemyName()))#prints inital greeting and zombie enemy name.
    print(attackingThing.getEnemyDescription())#prints the attacking zombie description.
    return battle(attackingThing,playerObject) #sends info to battle function.
    
def randomHumanAttack(attackingThing,playerObject): #if a human was chosen from random event 
    print( "You hear someone cough behind you. \nAs you turn you see a {}".format(attackingThing.getEnemyName())) #prints inital greeting and humn enemy name. 
    print(attackingThing.getEnemyDescription()) #prints the attacking human description.
    return battle(attackingThing,playerObject) #sends info to battle function.
    
def printBlankLines(playerObject): #prints out blank lines. 
    for i in range(15):     #intervals of 15 
        print() #prints lines 
    print(playerObject) #prints out player info.
    
def endingDisplay(playerObject,finNum): #ending text.Displays in 
    highScores(playerObject,finNum)
    print("Player: {} ".format(playerObject.getName())) #prints user name
    print("Weapon you had Equipped: {}".format(playerObject.getWeapon()))#prints equipped ramp
    print("Food: {}".format(playerObject.getFood())) #food gathered. 
    print("You had {} Kills".format(playerObject.getKills())) #number of kills.  
    print()
    
def startStory(): #prints the begining story
    print("The world has been overrun with zombies and anarchy.")
    print("You have managed to stay alive by joining a camp.")
    print("Eveyone has there place in the camp")
    print("You are a scavenger for the camp")
    print("Your objective is to find food.")
    print("Your camp has sent you out because food supply is low.")
    lineBreak() #creates a line break

def playerInfo(): #puts together the player object. Also gets players name.
    playerName = input("What is your name? ")    #Gets player name
    playerHp = 100 #player initial health
    playerFood = 0 #initial food
    playerWeapon = "Fist" #initial Weapon
    playerWeaponDamage = 10 #inital max damage
    playerKills = 0 #inital kill count
    playerObject = Player(playerName,playerHp,playerWeapon,playerWeaponDamage,playerFood,playerKills) #player obj
    printBlankLines(playerObject) #print blank lines 15
    return playerObject #returns playerObject

def lineBreak():#prints a line.
    return  print("---------------") # prints  line to split up

def title(): #greeting.
    print("Welcome to Post-pytholyptic")
    print("A text based adventure game")
    print("Created and Developed by Matthew Mace")
    lineBreak() #Creates a line break
        
def killsEnding(playerObject):#Ending seq if player ends up brining no food back, but gets kills
    lineBreak() #creates a line break
    print("You didnt food back, but managed to get some kills.")
    print("The group decided to make you a camp enforcer instead.")
    endingDisplay(playerObject,2) #prints ending text
    
def noGoodEnding(playerObject): #Ending seq if player gets no kills and brings no food.
    lineBreak()# prints  line to split up
    print("You brought back No food, and got no kills.")
    print("The group decided it didn't need another mouth to feed.")
    print("So you would have to be dinner.....")
    endingDisplay(playerObject,3) #prints ending text
    
def scavengerEnding(playerObject): #Ending seq if player makes it back with food to camp.
    lineBreak() # prints  line to split up 
    print("You made it back to camp with some food!") #prints out congrats
    endingDisplay(playerObject,0) #prints ending text

def highScores(playerObject,finNum): #prints score to external file 
    file = open("Post-pytholyptic_HighScores.txt", "a+")
    print(howFinHS(finNum),file=file)
    print("Player: {} ".format(playerObject.getName()),file=file) #prints user name
    #print("Weapon you had Equipped: {}".format(playerObject.getWeapon()),file=file)#prints equipped ramp
    print("Food: {}".format(playerObject.getFood()),file=file) #food gathered. 
    print("You had {} Kills".format(playerObject.getKills()),file=file) #number of kills.
    print('------------------------------------------', file=file) #insnerts a line.
    file.close() #Closes file
    
def howFinHS(finNum): #prints out the type of finish player had, and sends back to highScores function.
    finishedAsScavenger = "You made it back to camp, with food!" #if finished with food.
    death = "You Died" #if died.
    becameEnforcer = "You made it back to camp, without food. Elected Enforcer!" #if no food but gets kills.
    eaten = "Your camp ate you..pity."  #if worthless.
    finList = [finishedAsScavenger, death, becameEnforcer, eaten] #puts all in list.
    return finList[finNum] #returns number given from finish.
                    
def main():
    title()# displays title sequence.
    playerObject = playerInfo()    #Gets player object.
    startStory()       #prints main story
    stepsToTake = 10 #number of steps to finish

    while playerObject.getHp() >= 0:#While player hp is higher than 0
        try:         
            while stepsToTake > 0:#while steps are above 0
                print()#blank
                takeStep = input("Would you like to move foward? (y/n) ") #ask for player input to move next phase
                print(playerObject) #prints current player obj.
                
                if takeStep == 'y' : #if user wants to move foward subttract 1 step get random event and print blnk lines.
                    
                    stepsToTake = stepsToTake - 1 #subtract one from steps 
                    printBlankLines(playerObject) #print blank lines 15
                    print(randomEvent(playerObject)) #print out random event. 
                    break
            
                elif takeStep == 'n' : #if user wants to wait around. 
                    print("Ok we will just wait here until your ready.") #Tells users we will wait , until they are ready
                    break
                else: #if something other than y or n is chosen 
                    print() #blank
                    print("You need to enter y or n") #tells users try again they didnt type right letter. 
                    
            if stepsToTake == 0: #When users reaches there 10 step goal
                
                if playerObject.getFood() >= 1: #if player brings food back. 
                    scavengerEnding(playerObject) #calls the function if player brings back food to camp.
                elif playerObject.getFood()== 0 and playerObject.getKills() >=1: #if user brings no food back but gets kills
                    killsEnding(playerObject) #calls ending function if player got no food but kills.
                else: # player does not bring food back or gets any kills, or any other scenario.
                    noGoodEnding(playerObject) #function called if player returned with no food or no kills                  
                break
        except Exception as e: #catches and prints out exception.
            print(e)
          
    if playerObject.getHp() <= 0: #if player dies / hp gets to 0 or lower.
        print("Game Over!") #prints gameover
        print("You Have Died") #tells player they died.
        endingDisplay(playerObject,1) #prints ending text.
        
main()