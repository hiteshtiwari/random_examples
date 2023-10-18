class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_flag = 0
        B_flag = 0
        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    A_flag += 1
                else:
                    B_flag += 1
        return A_flag > B_flag