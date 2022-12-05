#%% Packages
import numpy as np 

#%%
# Extracting the input content
with open('CalorieStock.txt') as f:
    lines = f.readlines()

# Segregating the list into seperate arrays seperated by the space

sepList = []
Sum = 0
for count in range(0,len(lines)):
    if lines[count] == '\n':
        sepList.append(Sum)
        Sum = 0
        continue
    Sum = Sum + int(lines[count].split('\n')[0])
   
maxList = []
for count in range(0,3):
    maxList.append(max(sepList))
    sepList.remove(max(sepList))

totalCals = sum(maxList)
    