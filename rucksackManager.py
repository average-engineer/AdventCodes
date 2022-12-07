#%% Problem Description (Part 1)
# Each rucksack has 2 large compartments
# Only certain types of items can go into each compartment (only once)
# One wrongly put item per rucksack (i.e. item type in both compartments)
# Item type differentiator: lowercase or uppercase letter
# Single Line: All items in a rucksack (equally divided into compartments so im assuming #chars in every line is even)
# First half: in firstg compartment and second half: in second compartment
# Number of lines = Number of Rucksacks
# Priority number for lowercase: a(1) tp z(26)
# Priority number for uppercase: A(27) tp Z(52)

# To find: all item types shared by compartments of each rucksack and total sum of the resulting priority numbers

#%%
# Extracting the guide
with open('rucksackDatei.txt') as f:
    lines = f.readlines()
   
refinedLines = []
    
# Strategy:
    # Extract the item list for both compartments seperately for each rucksack
    # Nested for loop-> take each character from 1st half list, and see whether it occurs in the second list
    # break both the loops once a repitition is found since only one repeated item exists per rucksack

# Priority number assignment
# Keys: Strings (alphabets)
# Values: Priority Numbers
alphabetList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorityNumberAss = {} 
for ii in range(0,len(alphabetList)):
    priorityNumberAss[alphabetList[ii]] = ii + 1

priorityScore = 0
for ii in range(0,len(lines)):
    firstCom = ''
    secondCom = ''
    items = lines[ii].split('\n')[0]
    refinedLines.append(lines[ii].split('\n')[0]) # list without the \n at the end
    firstCom = items[:int(len(items)/2)]
    secondCom = items[int(len(items)/2):]
    # just a check
    if len(firstCom) != len(secondCom):
        print('Odd items in the rucksack')
        break
    
    errorDetected = 0
    for itemFirst in firstCom:
        for itemSecond in secondCom:
            if itemSecond == itemFirst:
                errorDetected = 1
                print('Error item in rucksack ' + str(ii + 1) + ' detected')
                # Adding to the priority number score
                priorityScore = priorityScore + priorityNumberAss[itemFirst]
                break
            
        if errorDetected == 0:
            continue
        else:
            break # Breaks both the for loops
            

print(priorityScore)

#%% Problem Decription (Part 2)
# One group -> 3 elves
# Identity badge -> Common item carried by all elves in their rucksacks
# To find: the priority number total for all the identifying badges in each group

numGroups = int(len(refinedLines)/3) # number of elf groups
groups = []

identityScore = 0
for ii in range(0,numGroups):
    groups.append(refinedLines[3*ii : 3*(ii + 1)])
    for alpha in refinedLines[3*ii : 3*(ii + 1)][0]:
        if alpha in refinedLines[3*ii : 3*(ii + 1)][1] and alpha in refinedLines[3*ii : 3*(ii + 1)][-1]:
            print('Identity badge for group number ' + str(ii + 1) + ' detected')
            identityScore = identityScore + priorityNumberAss[alpha]
            break # break the inner loop
    
print(identityScore)
        