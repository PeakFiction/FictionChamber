# ******************************************************************* 
# # lab07.py - Muhammad Sakhran Thayyib 2206046790
#
# Sorting a list of numbers using the Selection-Sort Algorithm *********************************************

## The selectionSort function sorts a list using the selection sort algorithm.
#
# @param values: the list to sort
# @return the total number of swaps
# calls the function minimumPosition
#
def selectionSort(values): #defines the name of the function as well as the argument, which is values AKA the list that we're trying to sort
    swapCounter = 0 #swapCounter keeps track of how many times an index has been swapped
    for x in range(len(values)-1): #for loop used to check and swap accordingly, len(values)-1 since as it gets to the last index, it will be the same either way and not change
        if values[x] > values[minimumPosition(values, x + 1)]: #to check if the current is larger than the smaller one
            values[x], values[minimumPosition(values, x + 1)] = values[minimumPosition(values, x + 1)], values[x] #and if so, then swap it
            swapCounter = swapCounter + 1 #if the if statement is fulfilled, add one to the swap counter, telling us that it's been swapped
    return swapCounter #returns the swap counter value
##
# Finds the smallest element in a tail range of the list
# @param values: the input list
# @param start: the first position in values to compare
# @return the position of the smallest element in the 
#   range values[start] ... values[len(values) - 1]
#

def minimumPosition(values, start): #assigns the name of the functions, as well as the arguments
    counter = 0 #counter is used to keep track of the position of the checker in relation to the indices, starts at 0 due to the first index being [0]
    minimum = values[start] #minimum keeps track on which is the smallest value
    smallestPosition = start #smallestPosition keeps track on which index has the smallest value
    for i in values[start:]: #checks every index but starts at [start:] since it starts checking at the index after it.
        if i < minimum: # if the minimum current i is less than minimum
            minimum = i #make said i into the new minimum
            smallestPosition = start + counter #update the smallestPosition position index
        counter = counter + 1 #add 1 to keep track of the checking position
    return smallestPosition #returns the smallestPosition of the list when done


## Demonstrates the selection sort algorithm by sorting
#  a list of numbers given by the user.

def main():
    input_string = input("Type a sequence of numbers (example: 3, 100, -5, 3): \n") #input line that gets the input from the user
    splittedInputString = input_string.split(',') #splits it in accordance to the commas
    listInteger = [int(i) for i in splittedInputString] #makes every element inside the list into an integer
    print("Input List:") #prints "Input List:"
    print(f"{listInteger}") #prints the listInteger, before the swapping happens
    swap = selectionSort(listInteger) #does the swap and sort whilst also getting the value on how many times it's been swapped
    print("Sorted List:") #prints "Sorted List:"
    print(f"{listInteger}") #prints the listInteger, after the swapping happens
    print('Number of swaps in Selection-Sort:', swap) #prints 'Number of swaps in Selection-Sort:' followed by the variable with the amount of swaps value

if __name__ == '__main__': #invoking the main function
    main()