# -*- coding: utf-8 -*-
"""
5-String Banjo Roll Generator
Created by Kevin Cretsos
kjcretsos@gmail.com
09-18-2020
************************
This program generates a random 5 string banjo roll from a JSON file
Rolls can range from 1, 2, 3, or 4 finger combos
The program also randomizes string patterns (T = 2-5, I = 2-3, M = 1)
Rules: no two fingers will repeat sequentially (ie. end of roll #1 (x) to start of roll #2 (x+1))      
If start of current finger sequence does not equal end of previous sequence, print the roll
Otherwise search for another sequence until the above condition is met
Repeat as many rolls as needed with the loop variable 
                                                
Fingers Key:
T = Thumb finger
I = Index finger
M = Middle finger

Strings Key:
5 = 5th string
4 = 4th string
3 = 3rd string
2 = 2nd string
1 = 1st string

************************
"""
# Repeat as many banjo rolls as needed with the loops variable 
def main():
    x = 0 
    loops = 3
    counter = 0
    firstFinger = ''
    firstString = ''
    lastFinger = ''
    lastString = ''
    print ('\n')   
    
    while (x < (loops*2)):     
        try:
            json_roll, json_chords = getJSON() #get JSON data
            limit = len(json_roll['rolls'])
            r = getRandom(limit) # get random roll
            style, roll, strings = getRoll(json_roll, r) #load roll
            chord, notes = getChord(json_chords) #load chord
            
            #check 1st roll
            if (((x+1) % 2) == 1):
                hand = 1
                firstFinger = roll[0]
                firstString = strings[0]
                flag = getFlag(firstFinger, firstString, lastFinger, lastString)
                # check flag for repeating first and last sequence
                # if flagged, find a new sequence, until not repeating
                
                while (flag == 1): #if repeated, find new sequence
                    r = getRandom(limit) #get random roll
                    style, roll, strings = getRoll(json_roll, r) #load roll
                    firstFinger = roll[0]
                    firstString = strings[0]
                    flag = getFlag(firstFinger, firstString, lastFinger, lastString)                   
                lastFinger = roll[(len(roll)-1)]
                lastString = strings[(len(strings)-1)]
                name1, f1, s1 = getSequence(style, roll, strings)

            #check 2nd roll                
            elif (((x+1) % 2) == 0):
                hand = 2
                firstFinger = roll[0]
                firstString = strings[0]
                flag = getFlag(firstFinger, firstString, lastFinger, lastString)
                # check flag for repeating first and last sequence
                # if flagged, find a new sequence, until not repeating 
                
                while (flag == 1): #if repeated, find new sequence
                    r = getRandom(limit) # get random roll
                    style, roll, strings = getRoll(json_roll, r) #load roll
                    firstFinger = roll[0]
                    firstString = strings[0]
                    flag = getFlag(firstFinger, firstString, lastFinger, lastString)                    
                lastFinger = roll[(len(roll)-1)]
                lastString = strings[(len(strings)-1)]
                name2, f2, s2 = getSequence(style, roll, strings)
                
#            #print roll and string sequence if at 2nd roll
            if (hand == 2):
                fingersLength = (len(f1)+len(f2))
                counter = counter+1
                print('* Banjo Roll #',counter) 
                print (f'{name1} - {name2}')
                print (f'\tsequences: {fingersLength}')
                print(f'\tfingers: {f1}-{f2}')
                print(f'\tstrings: {s1}-{s2}')
                print(f'\tchord: {chord} ({notes})')
                print ("\n") 

        #detect error for not loading JSON
        except KeyError:
            print(f'ERROR: roll from JSON file could not be found.')
        x = x+1
        #...roll on buddy, roll on..."

def getRandom(limit): #get random
    import random
    r = str(random.randint(1,limit))
    return r

def getRoll(json_data, r):
    style = json_data['rolls'][r]['style']
    roll = list(json_data['rolls'][r]['fingers'])
    strings = list(getStrings(roll)) #get string sequence with function
    return style, roll, strings
    
#get string order based on roll sequence
def getStrings(roll):
    import random
    r = ''.join(roll)
    string = [] #current string [i]
    previous = [] #previous string [i -1]   
    #randomize string order and check for duplicate strings
    for i in range(len(roll)):
        if ((roll[i]) == 'T'): #Thumb
            position = (random.randint(2,5))
            position = checkThumb(r, position) #check thumb for string 2
            string.append(str(position))
            previous.append(str(position))
            #check for duplicate string
            #replace string with different position
            if (i != 0): #skip first finger
                if ((string[i]) == (previous[i-1])):
                    if (roll[i-1]== 'I'):
                        string[i] = str(position+1)
                        previous[i] = str(position+1)
                    elif (roll[i-1]== 'M'):
                        string[i] = str(position+1)
                        previous[i] = str(position+1)             
        if ((roll[i]) == 'I'): #Index
            position = (random.randint(2,3))
            string.append(str(position))
            previous.append(str(position))
            #check for duplicate string
            #replace string with different position
            if (i != 0): #skip first finger
                if ((string[i]) == (previous[i-1])):
                    if (roll[i-1]== 'T'):
                        string[i] = str(position-1)
                        previous[i] = str(position-1)
                    elif (roll[i-1]== 'M'):
                        string[i] = str(position+1)
                        previous[i] = str(position+1)
        if ((roll[i]) == 'M'): #Middle
            position = (random.randint(1,1))
            string.append(str(position))
            previous.append(str(position))
            #check for duplicate string
            #replace string with different position
            if (i != 0): #skip first finger
                if ((string[i]) == (previous[i-1])):
                    if (roll[i-1]== 'T'):
                        string[i] = str(position-1)
                        previous[i] = str(position-1)
                    elif (roll[i-1]== 'I'):
                        string[i] = str(position-1)
                        previous[i] = str(position-1)
    s = ''.join(string)
    return s
    
def checkThumb(r, string):
    if ((string == 2) and ((r.startswith('TI')) or (r.endswith('TI')))):
        string = (string+1)
    elif ((string == 2) and ((r.startswith('IT')) or (r.endswith('IT')))):
        string = (string+1)
    elif ((string == 2) and ((r.startswith('ITM')) or (r.endswith('ITM')))):
        string = (string+1)
    elif ((string == 2) and ((r.startswith('TIM')) or (r.endswith('TIM')))):
        string = (string+1)
    return string

def getFlag(firstFinger, firstString, lastFinger, lastString):
    if ((firstFinger == lastFinger) or (firstString == lastString)):
        #print ("ERROR: duplicate sequence")
        return 1
    else:
        return 0

def getSequence(name, fingers, strings):
    x = name
    y = ''.join(fingers)
    z = ''.join(strings)
    return x, y, z
    
def getJSON():
    import json
    import random

    #Option 1: randomize finger combos
    combo = str(random.randint(2, 4))       
    
    #Option 2: Uncomment an option below to practice only one roll combo type
    #combo = '1' # 1 finger rolls 
    #combo = '2' # 2 finger rolls
    #combo = '3' # 3 finger rolls
    #combo = '4' # 4 finger rolls       
    
    #Open JSON file depending on roll type
    if (combo == '1'):
        with open('banjo_1finger.json', 'r') as f:
            json_roll = json.load(f)    
    elif (combo == '2'):
        with open('banjo_2finger.json', 'r') as f:
            json_roll = json.load(f)    
    elif (combo == '3'):
        with open('banjo_3finger.json', 'r') as f:
            json_roll = json.load(f)          
    elif (combo == '4'):
        with open('banjo_4finger.json', 'r') as f:
            json_roll = json.load(f)    

    with open('chords.json', 'r') as f:
        json_chords = json.load(f)              

    return json_roll, json_chords

def getChord(json_chords):
    limit = len(json_chords['key'])
    c = getRandom(limit) # get random chord
    chord = json_chords['key'][c]['scale']
    notes = json_chords['key'][c]['notes']
    return chord, notes       
        
if __name__ == '__main__':
    main()