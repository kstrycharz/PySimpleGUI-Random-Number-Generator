############### Dependencies ###############
# Random - specifically randint
# array and empty from Numpy
############### Methods ###############
# GenerateArray - generates array from a range and low values
# findRandom - finds a random index from a list
# removeVal - returns a list with a value removed
# getValue - gets value at a given index of a list
# runLoop - Not used in GUI version, prompts user to select to pick more numbers
# selectedList - returns a list of one value added

from random import randint
from numpy import array as arr
from numpy import empty




def GenerateArray(numRange, low): #Generating Initial Array
    array = empty(numRange, dtype = int)
    for x in range (0, numRange): #Creating Array 
        array[x] = x + low    
    return array


def findRandom(array): #finding random index
  randomIndex = randint(0, len(array) - 1)
  return randomIndex

def removeVal(array, index): #Removing selected index from array
    array = array.tolist()
    array.pop(index)
    array = arr(array)
    return array

def getValue(array, index):
    return array[index]

def runLoop():
    value = str(input("Would you like to continue? (Yes/No): "))
    if value == "y" or value == "yes" or value == "Yes":
        return True
    else: 
        return False

def selectedList(selectedVals, newVal):
    selectedVals.append(newVal)
    return selectedVals
