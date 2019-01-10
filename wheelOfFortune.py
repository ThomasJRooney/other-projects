import random

#Global Variables
WHEEL = [50, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 250, 250, 250, 500, 500, 750, 750, 1000, 2000, 5000, 10000, 'Bankrupt', 'Bankrupt']
VOWEL_COST = 250
CONSONANTS = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
VOWELS = ['A','E','I','O','U']

#randomPhraseNumber outputs a random number between 0 and 99
def randomPhraseNumber():
    randomPhraseNumber = random.randint(0,99)
    return(randomPhraseNumber)

#randomPhrase inputs a random number
#drawn from randomPhraseNumber function
#randomPhrase outputs a random phrase from phrase bank
def randomPhrase(randomPhraseNumber):
    PhraseBank = open('phrasebank.txt').read().splitlines()
    theRandomPhrase = PhraseBank[randomPhraseNumber]
    return(theRandomPhrase)

#categoryDeterminator inputs a random number
#drawn from randomPhraseNumber function
#categoryDeterminator outputs the category
#of the phrase selected from phrase bank
def categoryDeterminator(randomPhraseNumber):
    category = ''
    if randomPhraseNumber <= 19:
        category = 'Before and After'
    elif randomPhraseNumber <= 39:
        category = 'Song Lyrics'
    elif randomPhraseNumber <= 59:
        category = 'Around the House'
    elif randomPhraseNumber <= 79:
        category = 'Food and Drink'
    else:
        category = 'Same Name'
    return(category)

#phrasePrint inputs the puzzle solution, a list of correct
#guesses, and the user's most recent guess.
#phrasePrint outputs the phrase as underscores, unless
#user has already correctly guessed a letter or letters.
def phrasePrint(realPhrase, correctGuess):
    realPhraseList = list(realPhrase)
    printedList = []
    for character_ in realPhraseList:
        if character_ != ' ':
            printedList.append('_')
        else:
            printedList.append(' ')
    index = 0
    for letter in realPhraseList:
        for aGuess in correctGuess:
            if letter == aGuess:
                printedList[index] = aGuess
        index += 1
    for letter_ in range(len(printedList)):
        return(' '.join(map(str, printedList)))

#spinTheWheel inputs the puzzle solution and the player's current balance
#spinTheWheel outputs the user's winnings, the consonant guessed,
#how many times it is in the phrase, and if the guess was correct
def spinTheWheel(puzzleSolution, currentBalance):
    theSpin = WHEEL[random.randint(0,23)]
    winnings = 0
    if (theSpin == WHEEL[22]) or (theSpin == WHEEL[23]):
        print('Uh oh, you\'ve spun a Bankrupt! Your winnings will go down to $0.')
        winnings = 0
        letterCount = 0
        inPuzzle = 0
        userInputConsonantUp = None
    else:
        print('You\'ve spun', theSpin,'!')
        print('')
        userInputConsonant = str(input('Guess a letter: '))
        userInputConsonantUp = userInputConsonant.upper()
        letterCount = 0
        while userInputConsonantUp not in CONSONANTS:
            print('Whoops, that\'s not a consonant!')
            userInputConsonant = str(input('Guess a letter: '))
            userInputConsonantUp = userInputConsonant.upper()
        if userInputConsonantUp in CONSONANTS:
            if userInputConsonantUp in puzzleSolution:
                for letter in puzzleSolution:
                    if userInputConsonantUp == letter:
                        letterCount += 1
                winnings = theSpin * letterCount
                inPuzzle = True
            else:
                winnings = theSpin
                inPuzzle = False
    return([winnings, userInputConsonantUp, letterCount, inPuzzle])

#buyAVowel input the puzzle solution and the players current balance
#buyAVowel outputs how many times the vowel appears in the phrase
#and the vowel guessed.
def buyAVowel(puzzleSolution, currentBalance):
    if currentBalance >= 250:
        letterCount = 0
        userInputVowel = str(input('What vowel would you like to buy (A, E, I, O, U)?: '))
        userInputVowelUp = userInputVowel.upper()
        while userInputVowelUp not in VOWELS:
            print('Whoops, that\'s not a vowel!')
            userInputVowel = str(input('What vowel would you like to buy (A, E, I, O, U)?: '))
            userInputVowelUp = userInputVowel.upper()
        if userInputVowelUp in VOWELS:
            if userInputVowelUp in puzzleSolution:
                for letter in puzzleSolution:
                    if userInputVowelUp == letter:
                        letterCount += 1
            else:
                letterCount = 0
    return([letterCount, userInputVowelUp])

#solveThePuzzle inputs the puzzleSolution and the players curret current balance
#solveThePuzzle outputs the user's winnings and if the guess was correct
def solveThePuzzle(puzzleSolution, currentBalance):
    userInputSolve = str(input('Guess the solution: '))
    userInputSolveUp = userInputSolve.upper()
    if userInputSolveUp == puzzleSolution:
        guessCorrect = True
    else:
        guessCorrect = False
        currentBalance = 0
    return([currentBalance, guessCorrect])

def main():
    #Beginning of game prompt, determines the phrase and category
    print('Welcome to the Wheel of Fortune!')
    print('')
    theRandomPhraseNumber = randomPhraseNumber()
    theRandomPhrase = randomPhrase(theRandomPhraseNumber)
    print('The phrase is: ')
    print(phrasePrint(theRandomPhrase, []))
    print('')
    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
    print('')
    print('Your current winnings are: $0')
    print('')
    #The lists that are being updated throughout while loop
    vowelsGuessed = []
    consonantsGuessed = []
    lettersGuessed = []
    currentBalance = 0
    done = False
    while not done:
        if len(lettersGuessed) < 26:
            prompt = str(input('Would you like to Spin the Wheel (type: spin), Buy A Vowel (type: vowel), or Solve the Puzzle (type: solve)? '))
            print('')
            promptU = prompt.upper()
            #Executes when user types in any variation of spin
            #calls the spinTheWheel function, prompts user to guess a consonant,
            #and updates/prints lists and current balance
            if promptU == 'SPIN':
                spin = spinTheWheel(theRandomPhrase, currentBalance)
                print('')
                if spin[3] == True:
                    print('Congratulations,', spin[1], 'appears in the phrase', spin[2], 'time(s)! You\'ve won $', spin[0])
                    print('')
                    consonantsGuessed.append(spin[1])
                    lettersGuessed.append(spin[1])
                    currentBalance += spin[0]
                    print('The phrase is: ')
                    print(phrasePrint(theRandomPhrase, lettersGuessed))
                    print('')
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
                elif spin[1] == None:
                    currentBalance = 0
                    print('The phrase is: ')
                    print(phrasePrint(theRandomPhrase, lettersGuessed))
                    print('')
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
                else:
                    print('Sorry,', spin[1], 'does not appear in the puzzle. You will have $',spin[0], 'deducted from your winnings.')
                    print('')
                    consonantsGuessed.append(spin[1])
                    lettersGuessed.append(spin[1])
                    currentBalance -= spin[0]
                    print('The phrase is: ')
                    print(phrasePrint(theRandomPhrase, lettersGuessed))
                    print('')
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
            #Executes when user types in any variation of vowel
            #calls the buyAVowel function, prompts user to guess a vowel,
            #and updates/prints lists and current balance
            elif promptU == 'VOWEL':
                if currentBalance >= 250:
                    print('Ok! $250 will be deducted from your winnings.')
                    vowel = buyAVowel(theRandomPhrase, currentBalance)
                    print('')
                    if vowel[0] != 0:
                        print('Congratulations!', vowel[1], 'appears in the phrase', vowel[0], 'times!' )
                        print('')
                        vowelsGuessed.append(vowel[1])
                        lettersGuessed.append(vowel[1])
                        currentBalance -= VOWEL_COST
                        print('The phrase is: ')
                        print(phrasePrint(theRandomPhrase, lettersGuessed))
                        print('')
                        print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                        print('')
                        print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                        print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                        print('Your current winnings are:', currentBalance)
                        print('')
                    else:
                        print('Sorry,', vowel[1], 'does not appear in the phrase')
                        print('')
                        vowelsGuessed.append(vowel[1])
                        lettersGuessed.append(vowel[1])
                        currentBalance -= VOWEL_COST
                        print('The phrase is: ')
                        print(phrasePrint(theRandomPhrase, lettersGuessed))
                        print('')
                        print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                        print('')
                        print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                        print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                        print('Your current winnings are:', currentBalance)
                        print('')
                else:
                    print('Sorry, you don\'t have enough winnings to buy a vowel!')
                    print('')
                    print('The phrase is: ')
                    print(phrasePrint(theRandomPhrase, lettersGuessed))
                    print('')
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
            #Executes when user types in any variation of solve
            #calls the solveThePuzzle function, prompts user to guess a solution,
            #and prints if solution is correct and winnings
            elif promptU == 'SOLVE':
                print('What\'s your best guess (be sure to enter your guess with single spaces!)?')
                print('')
                solve = solveThePuzzle(theRandomPhrase, currentBalance)
                if (solve[1] == True) and (currentBalance > 0):
                    print('')
                    print('That\'s correct! You solved the puzzle!')
                    print('')
                    print('Congratulations, you\'ve won the game! Your winnings are $', currentBalance, '. Thank you for playing the Wheel of Fortune!')
                    done = True
                elif (solve[1] == True) and (currentBalance <= 0):
                    print('')
                    print('That\'s correct! You solved the puzzle!')
                    print('')
                    print('Congratulations, you\'ve won the game! Your winnings are $0. Thank you for playing the Wheel of Fortune!')
                    done = True
                elif currentBalance < 0:
                    print('')
                    print('Sorry, that guess is incorrect!')
                    print('')
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
                else:
                    print('')
                    print('Sorry, that guess is incorrect! Your winnings will start over at $0 :(')
                    print('')
                    currentBalance = 0
                    print('The category is: ', categoryDeterminator(theRandomPhraseNumber))
                    print('')
                    print('Vowels Guessed:', ', '.join(map(str, vowelsGuessed)))
                    print('Consanants Guessed:', ', '.join(map(str, consonantsGuessed)))
                    print('Your current winnings are:', currentBalance)
                    print('')
            else:
                print('Whoops, unrecognized input, try again')
                print('')
        else:
            if currentBalance > 0:
                print('')
                print('Sorry, you\'ve guessed all possible letters. Your current winnings are $', currentBalance, '. Thank you for playing the Wheel of Fortune!')
                print('')
            if currentBalance <= 0:
                print('')
                print('Sorry, you\'ve guessed all possible letters. Your current winnings are $',0 , '. Thank you for playing the Wheel of Fortune!')
                print('')
            done = True

if __name__ == '__main__':
    main()
