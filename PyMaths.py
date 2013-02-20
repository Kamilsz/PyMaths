#helps to learn basic mathematical operations

'''asks user to select what type of operation they want to practice:
1. multiplying
2. adding
3. substracting
4. dividing
5. all
asks user for range and beigns excercise for in range from 1 to x where is provided by user
if user selected all, asks for range for each of the type of operations
asks 10 different questions and in the end summarizes user score'''

from __future__ import division
from random import randint
from easygui import *

def exerciseQuery(exercise):
    '''prompts for selection of exercise'''
    #level boundaries for each type of operation
    if exercise == 'multiplication':
            low = 5
            up = 10
    elif exercise == 'division':
            low = 10
            up = 100
    elif exercise == 'addition':
            low = 20
            up = 1000
    elif exercise == 'substraction':
            low = 20
            up = 1000
    a = integerbox('Select difficulty for {}'.format(exercise), 'Select difficulty', lowerbound = low, upperbound = up)
    if a == None: exit()
    else: return a
    
def mathOperation():
    '''asks user what sort of operation they want to practice and what range they should be, returns the choice'''

    choices = ('multiplication', 'substraction', 'addition', 'division')
    exercisesList = multchoicebox("What would you like to practice today?", "Mathematics", choices)
    if exercisesList == None: exit()
    exercises = {}
    for exercise in exercisesList:
       
        #choice of difficulty for each exercise    
        exercises[exercise] = exerciseQuery(exercise)
    
    return exercises

def promptWindow(query, result):
    ''' prompts user for result of the operation'''
    question = integerbox(query, "What is the result of the following", lowerbound = 0, upperbound = 1000)
    if question == result:
        msgbox('Good job!', 'Awesome!', "Hurray!")
        return 1
    elif question == None: exit()
    else:
        msgbox('I am sorry, the correct answer is {}.'.format(result), 'Sorry...', 'Awwww...')
        return 0
    




def multiplication(difficulty):
    '''multiplication exercise'''
    num1 = randint(2, difficulty)
    num2 = randint(2, difficulty)
    query = "{}x{}= ".format(num1, num2)
    result = num1*num2
    return promptWindow(query, result)
    
        
def division(difficulty):
    ''' division exercise'''
    num1 = randint(2, difficulty)
    num2 = randint(2, difficulty)
    repeat = True
    while repeat:
        if num1 % num2 != 0:
            
            num2 = randint(2, difficulty)
        else: repeat = False
    query = "{}:{}= ".format(num1, num2)
    result = num1/num2
    return promptWindow(query, result)

def addition(difficulty):
    '''addition exercise'''
    num1 = randint(2, difficulty)
    num2 = randint(2, difficulty)
    query = "{}+{}= ".format(num1, num2)
    result = num1+num2
    return promptWindow(query, result)

def substraction(difficulty):
    '''substraction exercise'''
    num1 = randint(1, difficulty)
    num2 = randint(2, difficulty)
    repeat = True
    while repeat:
        if num2 > num1:
            num2 = randint(2,difficulty)
        else: repeat = False
    query = "{}-{}= ".format(num1, num2)
    result = num1 - num2
    return promptWindow(query, result)
    
    
def main():
    ''' main function of the program'''
    repeat = True
    exercises = mathOperation() #asks user what they want to practice and and what range of each math operation they want to try
    while repeat:
        
        repetitions = 1 #number of exercises
        score = 0
        while repetitions <= 3:
            for operation in exercises:
                if operation == 'multiplication':
                    score += multiplication(exercises[operation])
                    repetitions += 1
                elif operation == 'division':
                    score += division(exercises[operation])
                    repetitions += 1
                elif operation == 'addition':
                    score += addition(exercises[operation])
                    repetitions += 1
                elif operation == 'substraction':
                    score += substraction(exercises[operation])
                    repetitions += 1
                    
        result = int((score/(repetitions-1))*100)
        if result < 80:
            msgbox ("Your score is {}%.Unfortunatelly, you need to try again".format(result), 'So sorry...', 'Oh well')
            repeat = True
        else:           
            msgbox ("Outstanding! Your score is {}%".format(result), "Congratulations!", "Hurray!")
            repeat = False

            
        


main()








    


