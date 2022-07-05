# Kyle Strycharz
# July 5, 2022
# Random Number Generator with a customizable inital list 
# Applicaition uses PySimpleGui to generate random numbers for a given list

#Dependencies 
# pySimpleGUI pythons GUI module
# randomnum.py - custom methods for purpose of this project, designed in a way to have a text and GUI based app
# numpy - specifically the empty method



 ############### Variables ###############  
# totalSelectedNumList - 2 element array index 0 stores current number of values to be selected and index 1 stores total
# highNumError, lowNumError, selectedNumError - strings used in displaying messages in gui
# window - PySimpleGui object
# numLow - starting value of list
# numHigh - amount of values to be in list
# numList - List of numbers that can be selected, dynamically changes through program execution
# numListLength - length of numList
# runAgain - boolean value used as trigger for selecting more numbers from list
# endProgram - boolean value used when user is done selecting numbers, initiates the end of program sequence
# numsLeftInt - numbers left to be drawn from numList, only used for GUI
# drawNums - number of elements to draw from numList for that specific number selection request
# getIndex - index value, index gets removed from numList, using methods from randomnum.py                                  #
# getSelectedValue - value at numList[getIndex]       
# selectedNumbers - list of selected values                        #

 ############### Methods ###############    
 # belowZeroIndex - checks if the user is selecting too many values than what are avaliable in numList
 # inputErrorChecking - checks user inputs to make sure they are integer values, if they arent prompts user to re enter them
 # totalSelectedNumbers - returns totalSelectedNumList
 #        

 # Print Statements used for debugging purposes
        
            
import PySimpleGUI as sg                       # Part 1 - The import
import randomnum
from numpy import empty


#Varibles that need to be initialized before program start
totalSelectedNumList = empty(2, dtype = int)
totalSelectedNumList[1] = 0
selectedNumbers = []

highNumError = "Please re-enter the amount of numbers in the list."
lowNumError = "Please re-enter starting value."
selectNumberError = "Please re-enter amount of number to be selected."

# Used for selecting values, checks if user is attempting more values than what are  avaliable
def belowZeroIndex(list, numOfValues):
        
    
    if len(list) == 0:
        #print(" len == 0")
        window['inputErrorText'].Update("You can no longer select more values", visible = True)
        return True

        
     

    if len(list) < numOfValues:
        #print("len < selected")
       # event, values = window.read()
        window['inputErrorText'].Update("You have selected more values than what are currently avaliable, try again with an appropriate value.", visible = True)
        #if event == 'Button' or event == 'Yes':
        return True


       
 
    else:
        #print("Check is OK")
        return False


# Checks user inputs to make sure they are an integer
def inputErrorChecking(window, value, msg):
    window['numText'].Update(visible = False)
    window['numInput'].Update(visible = False)


    while True:   
        if value.isnumeric() == True:
            value = int(value)
            if value > 0:
                return value
        
            else:
                #print("neg")
                
                window['inputErrorText'].Update("You entered a negative value or 0, enter a positive number in both fields to continue", visible = True)
                #Build out method, should work with below
 
        else:
            #print("letter")
            window['inputErrorText'].Update("You entered the field below incorrectly. It must be an integer value.", visible = True)
        while True:


            window['inputErrorFieldText'].Update(msg, visible = True)
            window['inputErrorFieldInput'].Update(visible = True)
            event, values = window.read()
            
            
            if event == 'Button':
                
                value = values.get('inputErrorFieldInput')
                window['inputErrorFieldText'].Update("Re enter the", visible = False)
                window['inputErrorFieldInput'].Update(visible = False)
                window['inputErrorText'].Update("You entered a letter, the fields require numbers", visible = False)
                break
 

# Returns array of the total amount of selected numbers and selected numbers for that iteration
def totalSelectedNumbers(window, selectedNumList):

    window['inputErrorText'].update(visible = False)
    while True:

        window['numText'].Update(visible = True)
        window['numInput'].Update(visible = True)
        event, values = window.read()
        selectedNumList
        if event == 'Button':
            selectedInt = inputErrorChecking(window, values.get('numInput'), selectNumberError)
            selectedNumList[0] = selectedInt
            selectedNumList[1] = selectedNumList[1] + selectedInt
            return selectedNumList




# Define the window's contents
layout = [       # Part 2 - The Layout
            [sg.Text(key = 'inputErrorText', visible = False), sg.Text("Final Results", key = 'final', visible = False)],
            [sg.Text("Enter starting value of the list.", key = 'lowText', visible = True), sg.Input(key = 'lowInput', visible = True), sg.Text(key = 'inputErrorFieldText', visible = False), sg.Input(key = 'inputErrorFieldInput', visible = False)],
            [sg.Text("How many numbers would you like in the List?", key = 'highText', visible = True), sg.Input(key = 'highInput', visible = True), sg.Text("How many numbers do you want to pick?", key = 'numText', visible = False), sg.Input(key = 'numInput', visible = False)],
            [sg.Text("Original List", visible = False, key = 'oList'), sg.Text(visible = False, key = 'mainListLeft'), sg.Multiline(size=(30, 5), key = 'mainList', visible = False), sg.Text("Original list", key = 'oList', visible = False)],
            [sg.Text("Selected Numbers", visible = False, key = 'sList'), sg.Text(visible = False, key = 'selectedNumsTotal'), sg.Multiline(size=(30, 5),key = 'selectedNums', visible = False)],
            [sg.Button('Exit', key = 'exit', visible = False), sg.Text("Would you like to select more numbers?", visible = False, key = 'yesNoPrompt'), sg.Button('Enter', key = 'Button'), sg.Button('Continue', key = 'errorContinue', visible = False), sg.Button('Yes', key = 'Yes', visible = False), sg.Button('No', key = 'No', visible = False)] ], 


# Create the window
window = sg.Window('Random Number Generator', layout)      # Part 3 - Window Defintion

# Loop to get the range and starting value
while True:
    
    event, values = window.read()   # Storing low and high into values values.get('highInput')
 
 
    #Hiding Elements for Low and High and when hit it stores elements into values dictionary 
    if event == 'Button':
        window['highText'].Update(visible = False)
        window['highInput'].Update(visible = False)
        window['lowText'].Update(visible = False)
        window['lowInput'].Update(visible = False)
        
       
        numLow = inputErrorChecking(window, values.get('lowInput'), lowNumError)
        numHigh = inputErrorChecking(window, values.get('highInput'), highNumError)  # The starting value of the initial list
        #print(type(values.get('highInput')))
        #print(type(numHigh))

        

    
        #print(numHigh)
        #print(numLow)
    
        numList = randomnum.GenerateArray((numHigh), numLow) #Currently an Array Change to 
        numListLength = len(numList)
        break

        



runAgain = True
endProgram = False
#Loop used for selecting numbers, can be user can run mutiple times 
while runAgain == True:
    totalSelectedNumList = totalSelectedNumbers(window, totalSelectedNumList) #will get called again if user want to run it again
    numsLeftInt = numListLength - totalSelectedNumList[1]






###########Needs to be in main, changes numList and Selected Numbers ############
    drawNums = totalSelectedNumList[0]      
    if belowZeroIndex(numList, drawNums) == True:
        numsLeftInt = numListLength - (totalSelectedNumList[1] - totalSelectedNumList[0])
        totalSelectedNumList[1] = totalSelectedNumList[1] - totalSelectedNumList[0]
        #print()
        
    else:
        for x in range(0, drawNums):                                                    #
            getIndex = randomnum.findRandom(numList)                                    #
            getSelectedValue = numList[getIndex]                                        #
            selectedNumbers = randomnum.selectedList(selectedNumbers, getSelectedValue) #
        
            numList = randomnum.removeVal(numList, getIndex)                            #
#################################################################################



    window['numText'].Update(visible = False)
    window['numInput'].Update(visible = False)

    window['oList'].update(visible = True)
    window['mainList'].update(numList.tolist(), visible = True)  #Convert to List for UI
    window['mainListLeft'].update("Numbers left to Choose: {}".format(numsLeftInt), visible = True)

    window['sList'].update(visible = True)
    window['selectedNums'].update(selectedNumbers, visible = True)
    window['selectedNumsTotal'].update("Total Numbers Selected: {}".format(totalSelectedNumList[1]), visible = True)

    #print(selectedNumbers)
    #print(numList)

    window['yesNoPrompt'].update(visible = True)
    window['Button'].update(visible = False)
    window['Yes'].update(visible = True)
    window['No'].update(visible = True)
    
    #Nested loop prompting user if they want to select more numbers, or end 
    while True:
        event, values = window.read()   # Storing low and high into values values.get('highInput')
        # print("in loop")

        if event == 'Yes':
            #print("yes")
            window['numText'].update("How many more numbers would you like to select?")
            break
        if event == 'No':
            #print("no")
            endProgram = True
            repeat = False
            break
    
    if endProgram == True:
        break

    window['Button'].update(visible = True)
    window['Yes'].update(visible = False)
    window['No'].update(visible = False)
    window['yesNoPrompt'].update(visible = False)

#Formatting GUI for end of application
window['Button'].update(visible = False)
window['Yes'].update(visible = False)
window['No'].update(visible = False)
window['yesNoPrompt'].update(visible = False)
window ['exit'].update(visible = True)
window['mainListLeft'].update("Values remaining from original list.")
window['selectedNumsTotal'].update("Values that were selected. Total of {}.".format(totalSelectedNumList[1]))
window['final'].update(visible = True)
window['inputErrorText'].update(visible = False)

#Waiting for user to click exit and close application
while True:

    event, values = window.read()
 
    if event == 'exit':
        break

        
window.close()


    



    
