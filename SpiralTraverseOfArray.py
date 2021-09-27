# Spiral Traverse Temur


def spiralTraverse(array):
    temList = []
    # Here I initialize the vectors of the square
    starRow, endRow = 0, len(array)-1
    starCol, endCol = 0, len(array[0]) - 1
    while starRow <= endRow and starCol <= endCol:
        #Top line of a square
        for column in range(starCol, endCol+1):
            temList.append(array[starRow][column])

        for row in range(starRow+1, endRow+1):
            temList.append(array[row][endCol])

        for column in reversed(range(starCol, endCol)):
            if starRow == endRow:
                break
            temList.append(array[endRow][column])

        for row in reversed(range(starRow+1, endRow)):
            if starCol == endCol:
                break
            temList.append(array[row][starCol])
        starCol += 1
        endCol -= 1
        starRow += 1
        endRow -= 1
    return temList
