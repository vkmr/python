
import argparse

from time import sleep as s

class bcolors:
    """Base class to provide color to user prompts and texts."""
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WHITE = '\033[37m'
    PINK = '\033[35m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[94m'

class Quiz:
    """Base class to store dictionary of questions and answers for the game quizzes"""
    def __init__(self, qNADict={"Ques": "Ans"}):
        self.questionAndAnswer = qNADict
    
class QualifyingQuiz(Quiz):
    """Child class to Quiz class that stores dictionary of questions and answers for the qualifying quiz"""
    def __init__(self, qNADict={"Ques1": "Ans1"}):
        self.questionAndAnswer = qNADict

class SurvivalQuiz(Quiz):
    """Child class to Quiz class that stores dictionary of questions and answers for the Survival quizzes"""
    def __init__(self, qNADict={"Ques2": "Ans2"}):
        self.questionAndAnswer = qNADict

class GameWorld:
    """Base class for creating different worlds in the game"""

    def __init__(self, name='gameWorld', typeW='all'):
        self.worldName = name
        self.worldType = typeW
        self.essentials = []
        self.qualifyingQuiz = QualifyingQuiz()
        self.survivalQuiz1 = SurvivalQuiz()
        self.survivalQuiz2 = SurvivalQuiz()

    def qualifyingQuizMethod(self, questionAndAnswer):
        """Returns number of correct answers for Qualifying quiz. Compares User response with the desired answer from the existing dictionary"""
        questionsRight = 0
        for question in questionAndAnswer:
            answer = input(f"{bcolors.CYAN} {question[0]}\n: {bcolors.ENDC}")
            if answer == question[1]:
                questionsRight += 1
            elif answer.capitalize() == "Quit":
                # User wants to Quit the Game now
                print(f"User wants to quit the game now")
                questionsRight = "Quit"
                break
        
        return questionsRight

    def survivalQuizMethod(self, questionAndAnswer):
        """Returns 1 if User correctly answers all the question of the Survival quiz, else 0. Compares User response with the desired answer from the existing dictionary"""
        questionsRight = 1
        for question in questionAndAnswer: 
            answer = input(f"\n{bcolors.CYAN}{question[0]}\n:{bcolors.ENDC}")
            if answer == question[1]:
                questionsRight *= 1
            elif answer != question[1]:
                questionsRight *= 0
            elif answer.capitalize() == "Quit":
                # User wants to Quit the Game now
                print(f"User wants to quit the game now")
                questionsRight = "Quit"
                break
        
        return questionsRight

    def getEssentialList(self):
        """Returns list of essentials for a particular world"""
        return self.essentials

    def __str__(self):
        return self.worldName

class Nixoterra(GameWorld):
    """Child class for Snow World - Nixoterra"""
    #name = "Nixoterra"
    qNADictQ = {
    "Q1: What is the freezing point of snow?\n a. 0 degrees celcius\n b. 30 degrees celcius\n c. 100 degrees celcius\n d. -5 degrees celcius": "d",
    "Q2: Which ball do we use in the snow ball activity at snow world?\n a. Leather Ball\n b. Foot Ball\n c. Snow Ball\n d. All of the above": "d",
    "Q3: Which cartoon character does snow world have?\n a. Penguin\n b. Olaf\n c. Snowman\n d. All of the above": "d"
    }
    qNADictS1 = {
    "Q1: Describe a typical workweek for a snowboard instructor\n a. Sleep all week long\n b. Play with Ice\n c. Instruct and provide training to groups/individuals": "c",
    "Q2: what's your level of experience with edging, waxing and mounting skis and snowboard?\n a. Novice\n b. Proficient\n c. expert": "c"
    }
    
    qNADictS2 = {
    "Q1: What equipment is/are required for working as an experienced snowmaker\n a. Snow guns\n b. hoses\n c. hydrants\n d. All of the above": "d",
    "Q2: Can you safely lift 50 lbs\n a. Yes\n b. No": "a" 
    }    
    def __init__(self):
        self.worldName = "Nixoterra"
        self.worldType = "SnowWorld"
        self.essentials = ["Mittens", "Snowboots", "Ski Goggles", "Wool Socks", "Hand warmer"]
        self.story = "Ice, Chill, Snow, Cold, Freezerealm, Glacia. You name it. \nThey are all names for the mystic Nixoterra. Allow me, Nixette, to guide you through this world. This land is the mother of all snow and ice. Explore this world carefully, because the temperatures are- well, piercing. But other than that, just chill."
        #ToDo: Fill real name of capital city
        self.qualifyingQuiz = QualifyingQuiz(Nixoterra.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Nixoterra.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Nixoterra.qNADictS2)
    
class Silvia(GameWorld):
    """Child class for Forest World - Silvia"""
    #name = "Silvia"
    qNADictQ = {
    "Q1: Can you use a GPS device effectively?\n a. Yes\n b. No": "a",
    "Q2: Which of the following statement is true?\n a. Forest is on land\n b. Forest is under water": "a",
    "Q3: What NOT to do in a Forest world?\n a. Start fire\n b. Climb on Tree\n c. Enjoy Nature": "a"
    }
    qNADictS1 = {
    "Q1: Name one of the heavy equipments used in the forest operations\n a. Dump trucks\n b. Toycar\n c. Teddybear": "a",
    "Q2: Which is NOT one of the 4 forest types?\n a. Temperate\n b. Tropical\n c. Subtropical\n d. Arboreal" : "d"
    }
    qNADictS2 = {
    "Q1: Forest soil is a natural water filter\n a. True\n b. False": "a",
    "Q2: What is the definition of a forest?\n a. A public green area in a town, used for recreation.\n b. An area rich in biodiversity\n c. A large area of land densely populated by trees\n d. A flat area covered in plants" : "c"
    }

    def __init__(self):
        self.worldName = "Silvia"
        self.worldType = "ForestWorld"
        self.essentials = ["Mosquito Repellent", "Backpack", "Poncho", "Hiking boots", "Trail shoes"]
        self.story = "Hoy there! I'm Bryn, and I will be your personal guide through this wonderful world of trees and plants. \nWelcome to the forest, young explorer! These trees are sacred creatures who descended from the heavens. Enjoy your time in this wonderful place that you can call home"
        self.qualifyingQuiz = QualifyingQuiz(Silvia.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Silvia.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Silvia.qNADictS2)

class Aquamundi(GameWorld):
    """Child class for Water World - Aquamundi"""
    #name = "Aquamundi"
    qNADictQ = {
    "Q1: Spell Water\n a. Water\n b. Waiter": "a",
    "Q2: Is water same as wind?\n a. Yes\n b. No": "b",
    "Q3: Do you know how to swim?\n a. Yes\n b. No": "a"
    }
    qNADictS1 = {
    "Q1: Why do you want to be a Dive instructor?\n a. I like the word Instructor\n b. I love teaching diving": "b",
    "Q2: Do you have a Captain's license?\n a. Yes\n b. No": "a"
    }
    qNADictS2 = {
    "Q1: In case of any emergency call, what will be your first step?\n a. Ignore\n b. Immediately act on it": "b",
    "Q2: What is a large natural stream of flowing water that ends in a sea?\n a. Lake\n b. Ocean\n c. Glacier\n d. River": "d"
    }

    def __init__(self):
        self.worldName = "Aquamundi"
        self.worldType = "WaterWorld"
        self.essentials = ["Swimcap", "Bandana", "Float suit", "Rash guard", "Alternate Air Source"]
        self.story = "I see, you chose the water world. Great choice! I'm Aquanna, and I will be your guide in Aquamundi. If you are wondering when this endless ocean ends, don't waste your time. \nThis is a huge world, filled with nothing but water. Let's hop on our big boat and start this adventure!"
        self.qualifyingQuiz = QualifyingQuiz(Aquamundi.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Aquamundi.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Aquamundi.qNADictS2)

class Montelocus(GameWorld):
    """Child class for Mountain World - Montelocus"""
    #name = "Montelocus"
    qNADictQ = {
    "Q1: Do you know how to use mountain gear?\n a. Yes\n b. No": "a",
    "Q2: Are you a wayfinder or a lost sheep?\n a. Wayfinder\n b. Lostsheep": "a",
    "Q3: Are you afraid of heights?\n a. Yes\n b. No": "b"
    }
    qNADictS1 = {
    "Q1: What would you select to climb in tricky mountain conditions?\n a. Mountaineering boots\n b. mountains": "a",
    "Q2: What would you do if someone calls for help?\n a. It's their problem, I will just ignore\n b. Go and help them": "b"
    }

    qNADictS2 = {
    "Q1: Which of the following is the highest part of a mountain?\n a. Peak\n b. Base\n c. Slope\n d. None of the above": "a",
    "Q2: What should you do if you fall off a mountain during Climbing?\n a. Have a quick snack\n b. Make a quick phone call\n c. Take a selfie and post it on instagram\n d. Use a harness": "d"
    }
    def __init__(self):
        self.worldName = "Montelocus"
        self.worldType = "MountainWorld"
        self.essentials = ["Climbing Helmet", "Ropes", "Harness", "Mountaineering Boots", "Crampons"]
        self.story = "Isn't it beautiful, the divine mountain range of Montelocus. Oh hey! I didn't see you there! I'm Cashel, and I will lead you through the wonders of this rocky world, with mountains everywhere. \nThese mountains are said to be a gift from the sky. Take a moment to appreciate this particularly beautiful aspect of nature! \nAnyway, see you around!"
        self.qualifyingQuiz = QualifyingQuiz(Montelocus.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Montelocus.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Montelocus.qNADictS2)

class User:
    """Class for storing user information and tracking user activity throughout multiple stages of the game"""
    def __init__(self, name, location, system, coins=100):
        self.name = name
        self.location = location
        # not sure if we need it
        self.system = system
        self.coins = coins
        self.gems = 0
        self.assets = []

    def __str__(self):
        return self.name

    def collectGem(self):
        """Increments gem count of user by 1, if the user earns gem"""
        self.gems += 1

    def buyGem(self, amount):
        """Increments gem count of user by 1 if the buys the gem by spending coins"""
        returnVal = False
        if self.spendCoin(amount=25):
            self.gems += 1
            returnVal = True
        
        return returnVal

    def earnCoin(self, amount):
        """Increments count of coins by a certain amount"""
        self.coins += amount

    def spendCoin(self, amount):
        """Decreases count of coins by a certain amount"""
        returnVal = False
        if self.coins >= amount:
            self.coins -= amount
            returnVal = True

        return returnVal

    def getCoins(self):
        """Returns number of coins of the user"""
        return self.coins

    def getGems(self):
        """Returns number of gems of the user"""
        return self.gems

    def buyEssentials(self, amount=5):
        """Returns list of essential items bought by the user for the selected world and displays the list of user's assets.""" 
        ls = self.location.getEssentialList()
        print(f"{bcolors.WHITE}\nGreat job so far! Now, it's time to arm yourself with some essentials you would need to survive in the {self.location.worldType}.{bcolors.ENDC}")
        print(f"\n{bcolors.CYAN}Following are the essential items for {self.location.worldName}. Please choose a minimum of 3 items to proceed.{bcolors.ENDC}")
        outputList = [str(i+1) + ". " + ls[i] + "\n" for i in range(len(ls))]
        print(f"\n{bcolors.CYAN}{''.join(outputList)}{bcolors.ENDC}")
        sizeEssentialList = len(ls)
        essentialsList = []

        
        choiceInput = False
        while choiceInput is False:
            choices = input(f"{bcolors.CYAN}Input your selection as numbers 1, 2, 3, 4, or 5 separated by comma: {bcolors.ENDC}")
            choiceInput = True
            choices = choices.split(',')
            for choice in choices:
                if choice not in ('1', '2', '3', '4', '5', 'quit', 'QUIT', 'Quit'):
                    print(f"\n{bcolors.PINK}Please enter a valid Input{bcolors.ENDC}\n")
                    choiceInput = False
                    break
        
        for choice in choices:
            if choice.capitalize() == "Quit":
            # User input "Quit" at this stage. So, just quit the game.
                return choices
        

        try:
            # Convert input to integer for index in essentialList item
            choices = [int(i) for i in choices]
        except ValueError:
            # If input is not a number, Quit gracefully!
            print("Input is not a number. Quit")
            return essentialsList

        if max(choices) > sizeEssentialList:
            print(f"Invalid input! Input is not in essentialList")
            return essentialsList

        for j in choices:
            if self.spendCoin(amount):
                essentialsList.append(ls[j-1])
            else:
                print(f"You don't have enough money to buy {j}. You only have {self.coins} coins left.")
                break
        self.assets = essentialsList
        print(f"\n{bcolors.WHITE}Thank you for buying the essentials. Now you are officially ready to enter into the {self.location.worldType}.\nHere is your current asset bag with essential items and the available coins.{bcolors.ENDC}")
        print(f"\n{bcolors.YELLOW}Asset Bag Contents: {self.assets}\nCoins: {self.coins}{bcolors.ENDC}")

        return self.assets

    def getAssets(self):
        """Returns list of assets of the user"""
        return self.assets

    def takeSurvivalQuiz(self, quiz):
        """Returns the result of survival quiz""" 
        if quiz == 'survivalQuiz1':
            print(f"\n{bcolors.WHITE}Starting Survival quiz1 for {self.location.worldName} in 3 2 1....{bcolors.ENDC}")
            s(2)
            print(f"\n{bcolors.CYAN}To answer the following questions, input your choice by entering 'a', 'b', 'c', or 'd': {bcolors.ENDC}")
            userSurvival = [(i, self.location.survivalQuiz1.questionAndAnswer.get(i)) for i in self.location.survivalQuiz1.questionAndAnswer.keys()]
        elif quiz == 'survivalQuiz2':
            print(f"\n{bcolors.WHITE}Starting Survival quiz2 for {self.location.worldName} in 3 2 1....{bcolors.ENDC}")
            s(2)
            #print(f"\n{bcolors.CYAN}To answer the following questions, input your choice by entering 'a', 'b', 'c', or 'd': {bcolors.ENDC}")
            userSurvival = [(i, self.location.survivalQuiz2.questionAndAnswer.get(i)) for i in self.location.survivalQuiz2.questionAndAnswer.keys()]
        else: 
            # Wrong argument, should not have reached here. Return anyway!
            userSurvival = "Quit"
        survivalResults = self.location.survivalQuizMethod(userSurvival)
        return survivalResults

    def navigateToCapitalcity(self, amount=20):
        """Increments number if gems by 1 if the user succesfully navigates to the capital city""" 
        navSuccess = False
        if self.spendCoin(amount):
            self.gems += 1
            navSuccess = True
        return navSuccess
        
class GameSystem:
    """This is the game engine where other classes are ingested. This class controls the whole game system and stores system information"""
   
    def __init__(self):
        self.coins = 100
        self.name = "Gateway To Adventure"
        self.minCorrectAnswers = 2
        self.minGemsWin = 4
        self.minCoinsWin = 25
        self.minGemForCapitalCity = 2
        self.buyGemAmount = 25
        self.minEssentials = 3
        self.maxAssetNum = 5
        self.survivalWinCoins = 10
        self.userName = "Empty"

    def __str__(self):
        return self.name

    def getUserLocation(self, userName, worldList):
        """Returns user location after User selects a world"""
        validInput = False
        itemizedWorldList = [ "\n" + str(i+1) + ". " + worldList[i] for i in range(len(worldList))]
        while validInput is False:
            print(f"{bcolors.CYAN}Choose a world from the following: {bcolors.BOLD}{''.join(itemizedWorldList)}{bcolors.ENDC}")
            
            userLocation = input(f"{bcolors.CYAN}Please input the exact name of the world: {bcolors.ENDC}")
            
            userLocation = userLocation.capitalize()
            if userLocation in worldList:
                validInput = True
            else:
                if userLocation == "Quit":
                    validInput = True
                else:
                    print(f"{bcolors.FAIL}Invalid world name! Please enter a correct World Name {bcolors.ENDC}")
                    validInput = False
        
        return userLocation

    def selectWorld(self, userLocation, userName, availableWorldList):
        """Returns world type and the result of qualifying quiz, after User selects the world"""
        gameReturn = False
        if userLocation in availableWorldList:
            if userLocation == "Nixoterra":
                world = Nixoterra()
            elif userLocation == "Silvia":
                world = Silvia()
            elif userLocation == "Aquamundi":
                world = Aquamundi()
            elif userLocation == "Montelocus":
                world = Montelocus()
            else:
                # Should not have reached here!
                print(f"{bcolors.FAIL}Quitting as {userName} wants to quit the game.{bcolors.ENDC}")
                return gameReturn
            
            print(f"{bcolors.WHITE}Thank you for choosing the {world.worldType}.\n\n-------------\n{world.story}\n-------------\nNow, Let's see if you are ready for the selected world :-)\n\nStarting Qualifying quiz for {userLocation} in 3 2 1...{bcolors.ENDC}\n")
            s(2)
            print(f"{bcolors.CYAN}To answer the following questions, input your choice by entering 'a', 'b', 'c', or 'd'{bcolors.ENDC}")

            userQualifying = [(i, world.qualifyingQuiz.questionAndAnswer.get(i)) for i in world.qualifyingQuiz.questionAndAnswer.keys()]
            qualifyingResults = world.qualifyingQuizMethod(userQualifying)
        
            if self.checkReturn(qualifyingResults, userName):
                return gameReturn
        else:
            print(f"{bcolors.FAIL}You have already failed in the Qualifying quiz of {userLocation}. You can't reattempt thw Qualifyiong quiz.{bcolors.ENDC}")

        return world, qualifyingResults

    def checkReturn(self, returnVal, name):
        """Returns True if user enters 'quit' at any stage of the game"""
        quitGame = False
        if str(returnVal).capitalize() == "Quit":
            print(f"{bcolors.FAIL}Quitting as {name} wants to quit the game.{bcolors.ENDC}")
            # User entered Quit, exit and return accordingly
            quitGame = True
        return quitGame
    
    def evaluateSurvialQuiz(self, player):
        """Evaluates and displays result of survival quiz and also displays the user's current asset"""
        
        print(f"\n{bcolors.WHITE}Let's start earning some more coins by answering survival questions that will help you survive in the world{bcolors.ENDC}")
        quizList = ['survivalQuiz1', 'survivalQuiz2']
        perkReattempt = True
        for quiz in quizList:
            survivalResults = player.takeSurvivalQuiz(quiz)
            if self.checkReturn(survivalResults, player.name):
                return False

            if not survivalResults:
                print(f"{bcolors.FAIL}Sorry, you failed.{bcolors.ENDC}")
                if len(player.getAssets()) > self.minEssentials and perkReattempt:
                    print(f"{bcolors.WHITE}You are eligible for 1 reattempt.{bcolors.ENDC}")
                    perkReattempt = False
                    survivalResults = player.takeSurvivalQuiz(quiz)
                    
                    if self.checkReturn(survivalResults, player.name):
                        return False
                
                    if not survivalResults:
                        print(f"{bcolors.FAIL}Sorry, you failed again.{bcolors.ENDC}")
                    else:
                        player.earnCoin(self.survivalWinCoins * survivalResults)
                        player.collectGem()
                        print(f"{bcolors.YELLOW}Congrats! {player.name}, you have cleared {quiz}{bcolors.ENDC}")
                        #print(f"current coins: {player.getCoins()}\ncurrent Gems:{player.getGems()}")
                        
            else:
                player.earnCoin(self.survivalWinCoins * survivalResults)
                player.collectGem()
                print(f"{bcolors.YELLOW}Congrats {player.name}, you have cleared {quiz}{bcolors.ENDC}")
            print(f"{bcolors.YELLOW}current coins: {player.getCoins()}\ncurrent Gems:{player.getGems()}{bcolors.ENDC}")

        return True

    def gameStart(self): 
        """Returns true if the user successfully completes the game and handles invalid user input. Also, starts the game and create instances of user and world"""     
        
        print(f"{bcolors.WHITE}Hello, and welcome to the {bcolors.BOLD}Gateway of Adventure!{bcolors.ENDC} {bcolors.WHITE} Let's begin the fun ride!\nYou can quit the game at any stage of the game by typing Quit. Good Luck!{bcolors.ENDC}") 
        gameReturn = False
        worldList = ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]
        userInput = input(f"Would you like to view the instruction manual? (y/n): ")
        while userInput.lower() not in ('y', 'n', 'quit'):
            print(f"\n{bcolors.PINK}Please enter a valid input{bcolors.ENDC}\n")
            userInput = input(f"Would you like to view the instruction manual? (y/n): ")
        
        if userInput.lower() == "y":
            print(f"\n{bcolors.WHITE}Open this link to view the Instruction Manual:\n{bcolors.BLUE}{bcolors.UNDERLINE}https://github.prod.oc.2u.com/UCB-INFO-PYTHON/Jyoti_KumariREPO/blob/master/SUBMISSIONS/project_1/Gateway%20to%20Adventure%20-%20%20Instruction%20Manual.pdf{bcolors.ENDC}")
        elif userInput.lower() == "quit":
            self.checkReturn(userInput, "guest")
            return gameReturn

        if game.userName == "Empty":
            userName = input(f"\n{bcolors.CYAN}What is your name? {bcolors.ENDC}")
            self.userName = userName
        else:
            userName = self.userName

        #print(f"{bcolors.FAIL}You can type Quit to quit at any stage of the game. {bcolors.ENDC}")
        
        userLocation = self.getUserLocation(userName, worldList)
        
        if not userLocation:
            return gameReturn

        #userLocation = userLocation.lower()


        if self.checkReturn(userLocation, userName):
            return gameReturn
        
        # Valid User Location found
        # Let's select the world and do the Qualifying quiz for the world
        loopReturn = False
        while True:
            world, qualifyingResults = self.selectWorld(userLocation, userName, worldList)

            if not world:
                loopReturn = False
                break

            print(f"\n{bcolors.YELLOW}{userName}, you got {qualifyingResults} questions right.{bcolors.ENDC}\n")
            if qualifyingResults < self.minCorrectAnswers:
                # User failed the qualifying quiz
                print(f"{bcolors.FAIL}You failed in Qualifying quiz of {userLocation} {bcolors.ENDC}")
                worldList.remove(userLocation)
                if len(worldList):
                    print(f"{bcolors.WHITE}\nTry selecting another world to proceed. You can type Quit to quit at any stage of the game.{bcolors.ENDC}\n")
                    userLocation = self.getUserLocation(userName, worldList)
                    if not userLocation:
                        loopReturn = False
                        break
                    if self.checkReturn(userLocation, userName):
                        loopReturn = False
                        break
                else:
                    loopReturn = False
                    break
            else:
                loopReturn = True
                print(f"{bcolors.YELLOW}Congratulations! you now qualify to enter {userLocation}\n\n{world.story}\n\nYou have just won 100 coins!{bcolors.ENDC}")
                break
        
        if not loopReturn:
            return gameReturn
        # User Qualified the quiz for the world
        # Let's initialize Classes for World and player

        player = User(userName, world, self)

        #print(f"worldName: {world.worldName}\nworldType: {world.worldType}\n")

        #print(f"Player Name: {player.name}\nPlayer Location: {player.location}\nPlayer Coins: {player.getCoins()}\n" )

        essentialsList = player.buyEssentials()

        if not essentialsList:
            # No item selected from the essential list
            # Player can't survive in the world and Exit the world with message
            print(f"{bcolors.FAIL}Quitting as {userName} didn't select any essential items to enter the new world.{bcolors.ENDC}")
            return gameReturn               

        if self.checkReturn(essentialsList, userName):
            return gameReturn

        #print(f"{userName} Assets: ", player.getAssets())
        if len(player.getAssets()) < self.minEssentials:
            print(f"{bcolors.FAIL}{userName} needs to select at least {self.minEssentials} from the list.{bcolors.ENDC}")
            return gameReturn
      
        userInput = input(f"\n{bcolors.WHITE}{userName}, you have successfully entered into the {world.worldType}. As a next step, you would need to buy a gem for 25 coins to further explore this world.\nDo you want to proceed (y/n)?: {bcolors.ENDC}")
        while userInput.lower() not in ('y', 'n', 'quit'):
            print(f"\n{bcolors.PINK}Please enter a valid input{bcolors.ENDC}\n")
            userInput = input(f"\n{bcolors.WHITE}{userName}, you have successfully entered into the {world.worldType}. As a next step, you would need to buy a gem for 25 coins to further explore this world.\nDo you want to proceed (y/n)?: {bcolors.ENDC}")
        
        if userInput.lower() == 'y':
            if player.buyGem(self.buyGemAmount):
                print(f"{bcolors.YELLOW}Thank you {userName}, You now have {player.getGems()} gems and {player.getCoins()} coins{bcolors.ENDC}")
        
        else:
            self.checkReturn("quit", userName)
            return gameReturn

        s(2)
        # Conduct and Evaluate Survial Quiz for player
        if not self.evaluateSurvialQuiz(player):
            return gameReturn

        # Navigate to Capital City  
        if player.getGems() >= self.minGemForCapitalCity:
            print(f"{bcolors.WHITE}\nYay! you are a rockstar! Let's proceed to the next stage of the your journey by going to the very beautiful Capital City of {world.worldName}.{bcolors.ENDC}")
            s(2)
            print(f"{bcolors.WHITE}\nEntering into the Capital City 3 2 1....{bcolors.ENDC}\n")
            s(2)
    
            if len(player.getAssets()) == self.maxAssetNum :
                player.navigateToCapitalcity(10)
            else:
                player.navigateToCapitalcity()
            
            print(f"{bcolors.YELLOW}{userName} has reached the capital city of {userLocation}{bcolors.ENDC}")
            print(f"{bcolors.YELLOW}current coins: {player.getCoins()}\ncurrent Gems:{player.getGems()}{bcolors.ENDC}")
            
            response = input(f"\n{bcolors.WHITE}Do you want to buy addditional Gem for 25 coins? (y/n) {bcolors.ENDC}").lower()
            while response.lower() not in ('y', 'n', 'quit'):
                print(f"\n{bcolors.PINK}Please enter a valid input{bcolors.ENDC}\n")
                response = input(f"\n{bcolors.WHITE}Do you want to buy addditional Gem for 25 coins? (y/n) {bcolors.ENDC}").lower()
            if response == 'y':
                player.buyGem(25)
                print(f"user bought one gem")
            elif response == 'n':
                print(f"{bcolors.WHITE}{userName} declined offer{bcolors.ENDC}\n")
            else:
                self.checkReturn("quit", userName)
                return gameReturn

        # Check if Player has enough gems to win the game
        if player.getGems() >= self.minGemsWin:
            gameReturn = True
            # Check if Player has enough coins to win the game
            if player.getCoins() >= self.minCoinsWin:
                print(f"{bcolors.GREEN}{userName} has {player.getCoins()} coins and {player.getGems()} gems!")
                print(f"{bcolors.GREEN}Congratulations {userName}, you Won!{bcolors.ENDC}")
            else:
                print(f"{bcolors.PINK}Sorry {userName}, you lost.")
                print(f"{userName} has {player.getCoins()} coins left")
                print(f"You needed {self.minCoinsWin} coins to win the game!{bcolors.ENDC}")
        else:
            print(f"{bcolors.PINK}Sorry {userName}, you lost.")
            print(f"{userName} has {player.getCoins()} coins left")
            print(f"You needed {self.minGemsWin} gems to win the game!{bcolors.ENDC}")
            gameReturn = True

        return gameReturn
    
    def gameQuit(self):
        "Displays Goodbye message if the user has selected to quit the game"
        print(f"{bcolors.PINK}Goodbye {self.userName}, see you again!{bcolors.ENDC}")

parser = argparse.ArgumentParser(description = 'Step 1: Select a world --> Step 2: Take Qualifying quiz --> Step 3: Buy essentials(a minimum of 3 items) --> Step 4: Enter World and take 2 survival quizzes, one by one --> Step 5: Go to Capital City to get a gem or buy a gem --> Step 6: You win or lose depending on, if you have 25 coins and 4 gems at a minimum')
args = parser.parse_args()

game = GameSystem()

gameRestart = False
gameRestart = game.gameStart()
while gameRestart:
    gameRestart = input(f"\nDo you want to replay the Game!? (y/n): ")
    if gameRestart.lower() == 'y':
        gameRestart = game.gameStart()
    else:
        gameRestart = False
        game.gameQuit()



