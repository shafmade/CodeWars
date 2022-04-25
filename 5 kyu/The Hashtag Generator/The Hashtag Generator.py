#Defines the "generate_hashtag" function in order to return the solution.
def generate_hashtag(string):
  
    #Splits "string" into a list in order to capitalize the first character of each word.
    string = string.split(" ")
    for x in range(len(string)):
        string[x] = string[x].title()
        
    #Intersts "#" to the beginning of the list, concatenates the list, then removes any white space.
    final_hashtag = "#" + (" ".join(string))
    final_hashtag = final_hashtag.replace(" ", "")
    
    #Returns "final_hashtag" if the length of it is bigger than 1 but smaller than 140, otherwise it returns False.
    if 1 < len(final_hashtag) <= 140:
        return final_hashtag
    else:
        return False

