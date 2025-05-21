from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def back(i,j,k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >=len(board[0]) or word[k] != board[i][j]:
                return False
            
            char = board[i][j]
            board[i][j] = '&'

            if back(i+1, j, k+1) or back(i-1, j, k+1)or back(i, j+1, k+1)or back(i, j-1, k+1):
                return True
            
            board[i][j] = char
            return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if back(i,j,0):
                    return True
        return False
    
def main():
    board = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    result = solution.exist(board, word)
    print(result)

if __name__ =="__main__":
    main()