#Imports needed modules.
import re

#Defines the function in order to return the solution.
def move_zeros(array):
    
    #Converts "array" from a list into a string in order to work with the re.sub function.
    array = ' '.join(map(str, array))
    
    #Counts the amount of zeros, deletes all zeros in "array", then appends "array" with the previously counted amount of zeros.
    O_count = array.count('0')
    array = re.sub('0| ', '', array)
    array += '0' * O_count
    
    #Converts "array" back into a list, then converts all values in "array" into an integer.
    array = list(array)
    array = [int(item) for item in array]
    
    #Returns "array" with all zeros moved to the end of the list.
    return array
