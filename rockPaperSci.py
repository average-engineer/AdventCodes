#%% First Part
# Input:
    # 1st Col: What the opponent plays
    # A: Rock
    # B: Paper
    # C: Scissors
    # 2nd Col: What I should
    # X: Rock
    # Y: Paper
    # Z: Scissors
    # Score Allocation: 
        # Rock: 1
        # Paper: 2
        # Scissors: 3  
    # Score per round:
        # Loss: 0
        # Draw: 3
        # Win: 6

# Extracting the guide
with open('RockPaperSciGuide.txt') as f:
    lines = f.readlines()

shapeScore = 0
wlScore = 0
roundWon = []
for count in range(0,len(lines)):
    shape = lines[count].split('\n')[0].split(' ')[-1]
    oppShape = lines[count].split('\n')[0].split(' ')[0]
    if shape == 'X':
        if oppShape == 'C': # Rock beats opponent scissor
            wlScore = wlScore + 6
        elif oppShape == 'A': # Rock draws against opponent rock
            wlScore = wlScore + 3
        shapeScore = shapeScore + 1
    elif shape == 'Y':
        if oppShape == 'B': # Paper draws against opponent paper
            wlScore = wlScore + 3
        elif oppShape == 'A': # Paper wins against opponent rock
            wlScore = wlScore + 6
        shapeScore = shapeScore + 2
    elif shape == 'Z':
        if oppShape == 'B': # Scissor beats opponent paper
            wlScore = wlScore + 6
        elif oppShape == 'C': # Scissor draws against opponent scissor
            wlScore = wlScore + 3
        shapeScore = shapeScore + 3
totScore = wlScore + shapeScore
print(totScore)

#%% Second Part
# Input:
    # 1st Col: What the opponent plays
    # A: Rock
    # B: Paper
    # C: Scissors
    # 2nd Col: How the round should end
    # X: Loss 
    # Y: Draw
    # Z: Win
    # Score Allocation: 
        # Rock: 1
        # Paper: 2
        # Scissors: 3  
    # Score per round:
        # Loss: 0
        # Draw: 3
        # Win: 6

# Extracting the guide
with open('RockPaperSciGuide.txt') as f:
    lines = f.readlines()

shapeScore = 0
wlScore = 0
roundWon = []
for count in range(0,len(lines)):
    shape = lines[count].split('\n')[0].split(' ')[-1]
    oppShape = lines[count].split('\n')[0].split(' ')[0]
    if shape == 'X': # Loss Required
        if oppShape == 'C': # Opponent Scissor can beat only paper
            shapeScore = shapeScore + 2
        elif oppShape == 'A': # Opponent Rock can beat only scissor
            shapeScore = shapeScore + 3
        elif oppShape == 'B': # Opponent Paper can beat only rock
            shapeScore = shapeScore + 1
        wlScore = wlScore # No point added due to loss
    elif shape == 'Y': # Draw Required
        if oppShape == 'C': # Opponent Scissor can draw only scissor
            shapeScore = shapeScore + 3
        elif oppShape == 'A': # Opponent Rock can draw only rock
            shapeScore = shapeScore + 1
        elif oppShape == 'B': # Opponent Paper can draw only paper
            shapeScore = shapeScore + 2
        wlScore = wlScore + 3 # 3 points added due to draw
    elif shape == 'Z': # Win Required
        if oppShape == 'C': # Opponent Scissor can lose to only Rock
            shapeScore = shapeScore + 1
        elif oppShape == 'A': # Opponent Rock can lose to only paper
            shapeScore = shapeScore + 2
        elif oppShape == 'B': # Opponent Paper can lose to only scissor
            shapeScore = shapeScore + 3
        wlScore = wlScore + 6 # 6 points added due to win
totScore = wlScore + shapeScore
print(totScore)

