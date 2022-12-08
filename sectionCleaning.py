#%% Problem Description:
    # Unique Section ID for each section
    # Each elf assigned a range of section IDs
    # Some assigned section IDs overlap within the elves
    # Section IDs of pairs of elves compared
    # Range of section IDs with one elf: x-y, i.e. the elf has y-x+1 sections starting from section x to section y
    # To Find: #Elf Pairs where one of the ranges fully contain the other range
    
#%% Extracting the assignment pairs
with open('assignmentPairs.txt') as f:
    lines = f.readlines();

#%% Strategy:
    # Range A completely fully contains Range B iff RangeA[0] <= RangeB[0] && RangeA[-1] >= RangeB[-1] 
# Function for checking overlap between 2 ranges A & B
def fullOverlap(A,B):
    # A and B are both strings with format: 'x-y' with y-x+1 values
    # Function returns true if Range A completely overlaps Range B 
    if int(A.split('-')[0]) < int(B.split('-')[0]):
        if int(A.split('-')[-1]) >= int(B.split('-')[-1]): # Ex: 4-8 overlaps both 5-8 and 6-7
            return True
        return False
    elif int(A.split('-')[0]) == int(B.split('-')[0]):
        if int(A.split('-')[-1]) >= int(B.split('-')[-1]): # Ex: 4-8 overlaps 4-6 and 4-8 
            return True
        return False 
    return False

def partOverlap(A,B):
    # Function returns true if Range A partially overlaps Range B 
    if int(A.split('-')[-1]) >= int(B.split('-')[0]) and int(A.split('-')[0]) <= int(B.split('-')[-1]):
        return True
    return False

#%%
fOverlap = 0
pOverlap = 0
for ii in range(0,len(lines)):
    pairs = lines[ii].split('\n')[0]
    firstRange = pairs.split(',')[0]
    secondRange = pairs.split(',')[-1]
    
    # if either the 1st range completely overlaps the 2nd range or vice versa
    if fullOverlap(firstRange,secondRange) or fullOverlap(secondRange,firstRange):
        fOverlap = fOverlap + 1
    if partOverlap(firstRange,secondRange) or partOverlap(secondRange,firstRange):
        pOverlap = pOverlap + 1
        
print(pOverlap)     

#%% Part 2
   
        