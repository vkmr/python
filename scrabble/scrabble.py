import sys
from score_word import score_word

numWildCards = 0
hasWildCard = False

doFixLetterLocation = False
fixLetters = []
fixLocationLetters = []

numberOfArgs = len(sys.argv)

if numberOfArgs < 2:
    raise Exception("Invalid number of arguments: Need to provide scrabble Rack")

scrabbleRack = str(sys.argv[1])
# Scrabble Rack set to all uppercase as words in sowpods.txt is in all upper cases
scrabbleRack = scrabbleRack.upper()

# Code for Extra Credit point to store specific letter and specific
if numberOfArgs > 2:
    doFixLetterLocation = True
    for i in range(2, numberOfArgs, 2):
        fixLetters.append(str(sys.argv[i]).upper())
        fixLocationLetters.append(int(sys.argv[i+1]))

# Open the sowpods word file and constructs a word list "data"
with open('sowpods.txt',"r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

def checkValidWord(scrabbleRack):
    """Check if the input scrabble rack is Valid and raise exceptions if there are input errors from the user"""
    global numWildCards
    global hasWildCard
    numStarWildCard = 0
    numQuesWildCard = 0
    if len(scrabbleRack) < 2 or len(scrabbleRack) > 7:
        raise Exception("You Entered the wrong word: length of Input word should be > 2 and < 7 ")
    else:
        for i in range(len(scrabbleRack)):
            if scrabbleRack[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ*?":
                raise Exception("You Entered the wrong Scrabble Rack. Please ensure all letters in Rack are in: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*?' ")
            else:
                if scrabbleRack[i] in "*?":
                    if scrabbleRack[i] == "*":
                        if numStarWildCard == 0:
                            numStarWildCard = 1
                        else:
                            raise Exception("Number of WildCard '*' cannot be greater than 1 in one Rack")
                    else:
                        if numQuesWildCard == 0:
                            numQuesWildCard = 1 
                        else:
                            raise Exception("Number of WilCard '?' cannot be greater than 1 in one Rack")    
                    numWildCards = numStarWildCard + numQuesWildCard
                    hasWildCard = True    
                        

# Check if Scrabble Rack is valid and raise exception if there are input errors from the user
checkValidWord(scrabbleRack)

# List of Tuple to store valid word and corresponding score 
score_word_tuple_list = []

# Find all words from the word list that are made of letters that are a subset of the scrabble rack letters
for word in data:
    isValidWord = True # To mark whether word is valid and to be added to the score_word_tuple_list
    length_word = len(word)
    currentWildCardCount = numWildCards # Intialize the count of wild cards from Scrabble rack
    sumScoreWildCard = 0 # Keeps the sum of scores for each wild card

    if length_word > 1 and length_word < 8:
        # Create list of alphabet input tiles from Scrabble rack, i.e. no wild cards in the list
        alphabet_scrabble_rack_list = [i for i in scrabbleRack if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        if hasWildCard:
            # Input rack has wild cards
            for i in word:
                if i in alphabet_scrabble_rack_list:
                    # Found the tile in alphabet scrabble rack and remove it
                    alphabet_scrabble_rack_list.remove(i)
                else:
                    # Tile is not in anphabet scrabble rack list
                    # Check if Wild card can be used
                    if currentWildCardCount > 0:
                        currentWildCardCount -= 1 # Decrement the wild card count once used
                        sumScoreWildCard += score_word(i) # Sum the score of each wildcard added to the word
                    else:
                        # No Wild card left
                        isValidWord = False
                        break
        else:
            # Scrabble rack has no wild cards
            for i in word:
                if i in alphabet_scrabble_rack_list:
                    # Found the tile in alphabet scrabble rack and remove it
                    alphabet_scrabble_rack_list.remove(i)
                    isValidWord = True
                else:
                    isValidWord = False
                    # Break the loop as soon as the letter is not found in alphabet scrabble rack
                    break
    else:
        # length of word from the word list "data" is not in range [2, 7]
        isValidWord = False

    if isValidWord:
        isStillValidWord = True
        # For Extra credit point: specific letters at specific location
        if doFixLetterLocation:
            # Check if certain letter and its location has to be fixed
            if len(word) > fixLocationLetters[-1]:
                for j in range(0, len(fixLetters)):
                    if word[fixLocationLetters[j]] == fixLetters[j]:
                        isStillValidWord = True
                    else:
                        # Didn't find the certain letter at desired location
                        isStillValidWord = False
                        break
            else:
                isStillValidWord = False
        if isStillValidWord:
            # Get Score word for the valid word to be added to tuple list
            scoreWord = score_word(word) - sumScoreWildCard # Deducting score for wild cards
            score_word_tuple_list.append((scoreWord, word.lower()))

# Sorted by the score and then by the word alphabetically
score_word_tuple_list = sorted(score_word_tuple_list, reverse=True, key = lambda x: x[0])

for i in score_word_tuple_list:
    print("(%d, %s)" % i)

print("Total number of words:", len(score_word_tuple_list))
