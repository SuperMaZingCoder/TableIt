import math
import random


def printTable(matrix, useFieldNames):
    rows = len(matrix)
    cols = len(matrix[0])

    finalTable = []
    newMatrix = []
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = str(matrix[i][j])
            newMatrix.append(len(str(matrix[i][j])))
    newMatrix.sort()
    largestElementLength = newMatrix[-1]

    for i in range(rows):
        currentRow = ""
        for j in range(cols):
            currentEl = " " + matrix[i][j]
            if (largestElementLength != len(matrix[i][j])):
                # equal to len of currentEl, the other 1 goes so that
                # there will be one space on the end of
                currentEl = currentEl + " " * (largestElementLength - len(currentEl) + 2) + "|"
            else:
                currentEl = currentEl + " " + "|"
            currentRow += currentEl
        finalTable.append("|" + currentRow)
    rowLength = len(currentRow)

    wrappingRows = ""
    for i in range(rowLength - 1):
        wrappingRows += "-"
    wrappingRows = "+" + wrappingRows
    wrappingRows += "+"

    if (useFieldNames):
        rowUnderFields = ""
        for j in range(cols):
            currentElUnderField = "+" 
            currentElUnderField = currentElUnderField + "-" * (largestElementLength - len(currentElUnderField) + 3)
            rowUnderFields += currentElUnderField
        rowUnderFields += "+"
        finalTable.insert(1, rowUnderFields)

    finalTable.insert(0, wrappingRows)
    finalTable.append(wrappingRows)

    for row in finalTable:
        print(row)
