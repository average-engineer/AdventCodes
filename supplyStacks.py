#%% Problem Description:
    # Stacks of crates to be rearranged by crane
    # After rearrangement, desired crates at the top of each stack
    # procedure: move x from y to z
    # x: # crates to be moved
    # y: stack from which crates are moved
    # z: stack to which stakes are moved
    # Crates are moved one by one (if multiple crates moved together)
    # Input: Rearrangment Procedure
    # Output: Crates which end up at the top of each stack after rearrangment
    
#%% Extracting the arearrangement procedure
with open('stackRearrProc.txt') as f:
    lines = f.readlines();
    
#%% Segregating the stacks
# 9 stacks in total
stackList = [[],[],[],[],[],[],[],[],[]]
stacks = range(1,10)
crates = []
ref = []
stackInfo = []
procedure = []

ii = 0
while lines[ii].split(' ')[0] != 'move':
    stackInfo.append(lines[ii].split('\n'))
    ii  = ii + 1

procedure = lines[ii:-1]

lastLine = stackInfo[-2][0].split('  ')
#for count in range(0,len(lastLine[0].split('  '))):
 #   if lastLine[0].split(' ')[count] != '':
  #      ref.append(count)

for jj in range(0,len(stackInfo)-2):
    for kk in range(0,len(stackInfo[jj][0].split(' '))):
        if stackInfo[jj][0].split(' ')[kk] != '':
            for count in stacks:
                if kk//4 == count - 1:
                    stackList[count - 1].append(stackInfo[jj][0].split(' ')[kk])
            crates.append(kk)