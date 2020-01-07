input = "Hezam Kafe Mohammed"
def reverse(string):
    string = list(string)
    lenOfString = len(string) - 1
    counter = 0
    while counter < lenOfString:
        tempLetter = string[lenOfString]
        string[lenOfString] = string[counter]
        string[counter] = tempLetter
        counter +=1 
        lenOfString -=1
    return string

def reversingLetter(string, sw, ew):
    while sw < ew:
        tempLetetr = string[ew]
        string[ew] = string[sw]
        string[sw] = tempLetetr
        sw +=1
        ew -=1
    return string 
    

def swapping(string):
    lstString = reverse(string)
    i = 0
    sw = 0
    ew = 0
    lenOfstring = len(lstString) - 1
    while i < lenOfstring:
        if lstString[i] == ' ':
            cp = i - 1
            ew = cp
            # Calling the reversingLetter functin to reverese letter
            reversingLetter(lstString, sw, ew)
            sw = i +1
        i = i + 1
    # Calling the reversingLetter functin to reverese letter    
    reversingLetter(lstString, sw, i)
    return lstString 
print(swapping(input))
