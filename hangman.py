#
# Name: Robert Bryant
# hangman.py
#
# Problem: A game of hangman
#
# Certification of Authenticity:  
#   I certify that this lab is entirely my own work.

from random import randint
from graphics import *
import time
import math

#returns the contents of a file as a list
def fileContents(fileName):
    infile = open(fileName, "r")
    items = infile.readlines()
    infile.close()
    return items

#returns a random member of a list
def randomListItem(items):
    size = len(items)
    selection = items[randint(0,size-1)]
    #selection = items[0]  #uncomment for testing constant
    selection = selection[0:-1]
    return selection

#checks to see if a string is a member of a list
def inList(value,items):
    for char in items:
        if value == char:
            return True
    return False

#turns a list into a string with spaces in between each element
def stringWithSpaces(items):
    string = ''
    for char in items:
        string += " " + char
    return string

#refresh the status message after each entry
def refreshStatus(text):
    global statusMessage
    try:
        statusMessage.undraw()
    except:
        pass
    statusMessage = Text(Point(width/2,585),"Status: " + text)
    statusMessage.draw(win)

#changes the score
def refreshScore(points):
    global scoreText

    try:
        scoreText.undraw()
    except:
        pass
    scoreText = Text(Point(75,50),points)
    scoreText.draw(win)
    
#checks to see if a string is a member of the alphabet
def inAlphabet(value):
    if len(value)>1 or len(value)<1:
        return False
    
    value = value.lower()
    try:
        if ord(value)<ord("a") or ord(value)>ord("z"):
            return False
        else:
            return True
    except TypeError:
        return False

#creates a strikethrough version of a word.
def strikethrough(string):
    value = ""
    for char in string:
	#the next line is commented out because it is not working correctly on my machine 
        #value += char + chr(822)
	pass
    return value

#game section
def playGame(word):
    score = 0
    letters = []
    badLetters = []
    #word = "apple" #constant word for testing
    
    refreshScore(score)
    guessText = Text(Point(center,560),"What is your guess:")
    guessText.draw(win)
    guessBox = Entry(Point((width*3/4),562),5)
    guessBox.draw(win)
    blanks = Text(Point(center,520),blankWord(word,letters))
    blanks.draw(win)
    button = Rectangle(Point(width*2/5,610),Point(width*3/5,640))
    button.setFill("gray")
    button.draw(win)
    buttonText = Text(Point(center,625),"Try It!")
    buttonText.draw(win)

    #primary logic of game
    while len(badLetters) < 7:

        displayLetters = Text(Point(width/2,540),"You have already guessed the following letters:" + stringWithSpaces(letters))
        displayLetters.draw(win)

        click = win.getMouse()
        while not buttonClickTest(click,button.getP1(),button.getP2()):
            click = win.getMouse()
        guess = guessBox.getText()
        guess = guess.lower()

        #get input and check for validity and repetition.
        while guess == "" or inList(guess, letters) or not inAlphabet(guess):
            if len(guess)>1:
                refreshStatus("That was multiple charecters, you know how to play hangman right?")
            elif inList(guess, letters) and guess != "":
                refreshStatus("You already tried that, you must be from SC.")
            elif not inAlphabet(guess) and guess != "":
                refreshStatus("a-z only. No accients either, it is not hangma"+chr(241)+"o")
            guessBox.setText("")

            click = win.getMouse()
            while not buttonClickTest(click,button.getP1(),button.getP2()):
                click = win.getMouse()
            guess = guessBox.getText()
            guess = guess.lower()
        letters += guess

        blanks.undraw()
        blanks = Text(Point(width/2,520),blankWord(word,letters))
        blanks.draw(win)         
        #check to see if guess is in word
        if inList(guess,word):
            refreshStatus("Good Job")
            score += ord(guess)*10
            refreshScore(score)
            if spellCheck(word,letters):
                refreshStatus("Cortana is safe, you win.")
                break
        else:
            badLetters += guess
            refreshStatus("Incorrect " + str(7 - len(badLetters)) + " guesses left")
            drawCortana(len(badLetters))
        displayLetters.undraw()
        guessBox.setText("")
        
    if len(badLetters) == 7:
        refreshStatus("You killed " + strikethrough("kenny") + "  Cortana, you bastard!")

    button.undraw()
    buttonText.undraw()
    again = playAgain()
    guessText.undraw()
    guessBox.undraw()
    blanks.undraw()
    statusMessage.undraw()
    scoreText.undraw()
    displayLetters.undraw()
    undrawCortana()
    return again
    
    
#function to draw the parts of Cortana's body.
def drawCortana(part):
    global neck
    global hair0
    global head0
    global head1
    global head2
    global hair1
    global hair2
    global hair3
    global hair4
    global hair5
    global torso
    global leftBreast
    global rightBreast
    global rightHip
    global leftHip
    global waist
    global torsoExtra
    global rightShoulder
    global rightArm
    global leftShoulder
    global leftArm
    global leftLeg
    global rightLeg
    
    if part == 1:
        neckColor = "blue"
        faceColor = "blue"
        neck = Polygon(Point(center-10,160),Point(center+10,160),Point(center+13,185),Point(center-13,185))
        neck.setFill(neckColor)
        neck.setOutline(neckColor)
        neck.draw(win)
        hair0 = Circle(Point(center,130),28)
        hair0.setFill("black")
        hair0.draw(win)
        head0 = Circle(Point(center,130),20)
        head1 = Circle(Point(center,160),17)
        head2 = Polygon(Point(center-20,130),Point(center+20,130),Point(center+17,160),Point(center-17,160))
        head0.setFill(faceColor)
        head1.setFill(faceColor)
        head2.setFill(faceColor)
        head0.setOutline(faceColor)
        head1.setOutline(faceColor)
        head2.setOutline(faceColor)
        head0.draw(win)
        head1.draw(win)
        head2.draw(win)
        hair1 = Polygon(Point(272,127),Point(281,126),Point(279,169),Point(272,170))
        hair1.setFill("black")
        hair1.draw(win)
        hair2 = Polygon(Point(301,108),Point(280,128),Point(281,116),Point(289,110))
        hair2.setFill("black")
        hair2.draw(win)
        hair3 = Polygon(Point(301,110),Point(321,126),Point(323,118),Point(309,107))
        hair3.setFill("black")
        hair3.draw(win)
        hair4 = Polygon(Point(320,125),Point(322,169),Point(328,170),Point(328,129))
        hair4.setFill("black")
        hair4.draw(win)
        hair5 = Polygon(Point(291,115),Point(299,119),Point(311,112),Point(299,105))
        hair5.setFill("black")
        hair5.draw(win)

    if part == 2:
        torso = Polygon(Point(center-13,185),Point(center+13,185),Point(center+13+25,190),Point(center+13+15,300),Point(center-13-15,300),Point(center-13-25,190),Point(center-13,185))
        torso.setFill("blue")
        torso.setOutline("blue")
        torso.draw(win)
        leftBreast = Circle(Point(center-18,232),18)
        leftBreast.setFill("blue")
        leftBreast.setOutline("blue")
        leftBreast.draw(win)
        rightBreast = leftBreast.clone()
        rightBreast.move(36,0)
        rightBreast.draw(win)

    if part == 3:
        rightHip = Circle(Point(center+12,315),24)
        rightHip.setFill("blue")
        rightHip.setOutline("blue")
        rightHip.draw(win)
        leftHip = Circle(Point(center-12,315),24)
        leftHip.setFill("blue")
        leftHip.setOutline("blue")
        leftHip.draw(win)
        waist = Polygon(Point(center+34,310),Point(center+31,290),Point(center-31,290),Point(center-34,310))
        waist.setFill("blue")
        waist.setOutline("blue")
        waist.draw(win)
        torsoExtra = Rectangle(Point(287,339),Point(313,320))
        torsoExtra.setFill("blue")
        torsoExtra.setOutline("blue")
        torsoExtra.draw(win)

    if part == 4:
        rightShoulder = Circle(Point(center+13+24,201),10)
        rightShoulder.setFill("blue")
        rightShoulder.setOutline("blue")
        rightShoulder.draw(win)
        rightArm = Polygon(Point(347,201),Point(357,324),Point(348,325),Point(336,210))
        rightArm.setFill("blue")
        rightArm.setOutline("blue")
        rightArm.draw(win)
        
    if part == 5:
        leftShoulder = Circle(Point(center-13-24,201),10)
        leftShoulder.setFill("blue")
        leftShoulder.setOutline("blue")
        leftShoulder.draw(win)
        leftArm = Polygon(Point(center-47,201),Point(center-57,324),Point(center-48,325),Point(center-36,210))
        leftArm.setFill("blue")
        leftArm.setOutline("blue")
        leftArm.draw(win)
    if part == 6:
        rightLeg = Polygon(Point(336,316),Point(321,458),Point(308,458),Point(center+2,335))
        rightLeg.setFill("blue")
        rightLeg.setOutline("blue")
        rightLeg.draw(win)

    if part == 7:
        leftLeg = Polygon(Point(center-36,316),Point(center-21,458),Point(center-8,458),Point(center-2,335))
        leftLeg.setFill("blue")
        leftLeg.setOutline("blue")
        leftLeg.draw(win)

        #death
        neckColor = "brown"
        neck.setFill(neckColor)
        neck.setOutline(neckColor)



#remove body parts   
def undrawCortana():
    try:
        neck.undraw()
        hair0.undraw()
        head0.undraw()
        head1.undraw()
        head2.undraw()
        hair1.undraw()
        hair2.undraw()
        hair3.undraw()
        hair4.undraw()
        hair5.undraw()
        torso.undraw()
        leftBreast.undraw()
        rightBreast.undraw()
        rightHip.undraw()
        leftHip.undraw()
        waist.undraw()
        torsoExtra.undraw()
        rightShoulder.undraw()
        rightArm.undraw()
        leftShoulder.undraw()
        leftArm.undraw()
        rightLeg.undraw()
        leftLeg.undraw() 
    except:
        pass
        
#returns a string with blanks or charecters if the values are in the argument.  returned blanks/charecters are seperated by spaces
def blankWord(string, items):
    count = 0
    blanks = ""
    check = False
    for char in string:
        for value in items:
            if value == char:
                blanks += char + " "
                check = True
                break
        if not check:
            blanks += "_ "
        check = False

    return blanks

#checks to see if the members of a list are equal to the elements of a string.       
def spellCheck(string, items):
    count = 0
    for char in string:
        for value in items:
            if value == char:
                count += 1
    if count == len(string):
        return True
    else:
        return False

#present logo
def drawDog():
    dogHeight = (height/2)-25
    head = Circle(Point(center,height/2), 75)
    head.setFill("brown")
    head.draw(win)

    ear0 = Oval(Point(center-75,dogHeight-40),Point(center-35,dogHeight+115))
    ear0.setFill("brown")
    ear0.draw(win)

    ear1 = ear0.clone()
    ear1.move(110,0)
    ear1.draw(win)

    nose = Circle(Point(center,dogHeight+45), 10)
    nose.setFill("Black")
    nose.draw(win)

    eye0 = nose.clone()
    eye0.move(-20,-40)
    eye0.draw(win)

    eye1 = nose.clone()
    eye1.move(20,-40)
    eye1.draw(win)

    topText = Text(Point(center,(height/2)-100),"Funny Looking Dog")
    bottomText = Text(Point(center,(height/2)+100),"Studios")
    topText.draw(win)
    bottomText.draw(win)

    time.sleep(1)

    head.undraw()
    ear0.undraw()
    ear1.undraw()
    nose.undraw()
    eye0.undraw()
    eye1.undraw()
    topText.undraw()
    bottomText.undraw()

#this is the introduction to the game
def openingSequence():
    drawDog()
    
    background = Rectangle(Point(0,0),Point(width,height))
    background.draw(win)
    for i in range(256,0,-15):
        background.setFill(color_rgb(i,i,i))
        time.sleep(.05)
    title = Text(Point(width/2,height/2),"HALO - 0.5\nHangman Evolved")
    title.setSize(36)
    title.draw(win)
    j = i
    for i in range(j,256,15):
        background.setFill(color_rgb(i,i,i))
        time.sleep(.05)
    background.undraw()
    time.sleep(1.75)
    title.undraw()

    story = Text(Point(width/2,height/2),"MASTER CHEIF:\nCortana is trapped in an advanced Covenet construct.\nYou must guess the passcode to free her.\nOn your 7th mistake she will die.\n\nClick to Continue")
    story.draw(win)
    win.getMouse()
    story.undraw()

#this draws the "advanced Coveneant construct" (gallows)
def drawEnvironment():
    base = Rectangle(Point(0,500),Point(width,480))
    base.setFill("dark slate gray")
    base.setOutline("dark slate gray")
    base.draw(win)
    pole = Rectangle(Point(width*4/5,480),Point((width*4/5)+15,75))
    pole.setFill("saddle brown")
    pole.setOutline("saddle brown")
    pole.draw(win)
    bar = Rectangle(Point(width*4/5,75),Point(width/2,90))
    bar.setFill("saddle brown")
    bar.setOutline("saddle brown")
    bar.draw(win)
    hook = Rectangle(Point(center+7,75),Point(center-7,130))
    hook.setFill("saddle brown")
    hook.setOutline("saddle brown")
    hook.draw(win)
    mario = Text(Point(75,30),"MARIO")
    mario.draw(win)

#checks to see if player wants another game.
def playAgain():
    yesButton = Rectangle(Point(width*1/5,610),Point(width*2/5,640))
    yesButton.setFill("gray")
    yesButton.draw(win)
    yesButtonText = Text(yesButton.getCenter(),"Yes")
    yesButtonText.draw(win)

    noButton = Rectangle(Point(width*3/5,610),Point(width*4/5,640))
    noButton.setFill("gray")
    noButton.draw(win)
    noButtonText = Text(noButton.getCenter(),"No")
    noButtonText.draw(win)

    question = Text(Point(center,625),"Play Again?")
    question.draw(win)

    clicked = False
    while not clicked:    
        selection = win.getMouse()
        if buttonClickTest(selection,yesButton.getP1(),yesButton.getP2()) or buttonClickTest(selection,noButton.getP1(),noButton.getP2()):
            clicked = True
    if buttonClickTest(selection,yesButton.getP1(),yesButton.getP2()):
        value = True
    if buttonClickTest(selection,noButton.getP1(),noButton.getP2()):
        value = False

    yesButton.undraw()
    yesButtonText.undraw()
    noButton.undraw()
    noButtonText.undraw()
    question.undraw()
    return value
        
        
#check to see if a mouse click is within two points
def buttonClickTest(testPoint, point1, point2):
	minX = min(point1.getX(),point2.getX())
	minY = min(point1.getY(),point2.getY())
	maxX = max(point1.getX(),point2.getX())
	maxY = max(point1.getY(),point2.getY())
	testXmin = testPoint.getX() - minX
	testYmin = testPoint.getY() - minY
	testXmax = maxX - testPoint.getX()
	testYmax = maxY - testPoint.getY()
	
	#test to see if the click is less than any side
	try:
		temp = math.sqrt(testXmin)
		temp = math.sqrt(testYmin)
	except ValueError:
		return False

	#test to see if the click is greater than any side
	try:
		temp = math.sqrt(testXmax)
		temp = math.sqrt(testYmax)
	except ValueError:
		return False

	#if the click is inside the button return is true
	return True

#main function         
def main():
    global win
    global width
    global height
    global center

    #get words from file
    fileName = "wordList.txt"
    wordList = fileContents(fileName)

    #create window
    width = 600
    height = 650
    center = width/2
    win = GraphWin("hangman.py",width,height)
    win.setBackground("white")

    #setup game
    openingSequence()
    drawEnvironment()

    #play game
    again = True
    while again:
        word = randomListItem(wordList)
        again = playGame(word)
        
    win.close()

main()
