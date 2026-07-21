class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validRows = True
        for row in board:
            filteredRows = [i for i in row if i != '.']

            if len(filteredRows) != len(set(filteredRows)):
                validRows = False

        validColumns = True
        for column in range(len(board[0])):
            columnElems = []
            for i in board:
                columnElems.append(i[column])
            
            filteredColumns = [i for i in columnElems if i != '.']

            if len(filteredColumns) != len(set(filteredColumns)):
                validColumns = False

        validSquares = True
        squaresDict = {}
        index = 0
        indexC = 0
        for r in range(len(board)):
            for elem in range(len(board[r])):
                if index not in squaresDict:
                    squaresDict[index] = []
                squaresDict[index].append(board[r][elem])
                if (elem + 1) % 3 == 0:
                    index += 1
            if (r + 1) % 3 == 0:
                indexC += 3
            index = indexC  

        for value in squaresDict.values():
            filteredVal = [i for i in value if i != '.']

            if len(filteredVal) != len(set(filteredVal)):
                validSquares = False

        if validRows and validColumns and validSquares:
            return True
        else:
            return False
