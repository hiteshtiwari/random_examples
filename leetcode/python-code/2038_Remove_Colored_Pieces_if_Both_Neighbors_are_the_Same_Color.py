def winnerOfGame(colors: str) -> bool:
    if len(colors) < 3:
        return False
    
    flag = False
    for i in range(len(colors)-1, 1, -1):
        if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
            if colors[i] == 'A':
                flag = True
            else:
                flag = False
    return False

print(winnerOfGame("AA"))