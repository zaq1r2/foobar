RANGE = 10

def solution(L):
    flag = findLargestMultipleOfThree(L)
    if flag == True and len(L) > 0:
        return "".join(str(num) for num in L)
    else:
        return 0

def findLargestMultipleOfThree(L):
    sumOfList = sum(L)
    countingSort(L)
    if sumOfList % 3 == 0:
        return True 
    remainder = sumOfList % 3
    if remainder == 1:
        remainderOne(L)
        return True 
        
    elif remainder == 2:
        remainderTwo(L)
        return True 
        
    return False

def countingSort(L):
    countingArray= [0] * RANGE
    for num in L:
        countingArray[num] += 1
    
    currIndex = len(L) - 1
    for i in range(RANGE):
        while countingArray[i] > 0:
            L[currIndex] = i
            currIndex -= 1
            countingArray[i] -= 1

def removeElements(L, idx1, idx2 = -1):
    L.remove(L[idx1])
    if idx2 != -1:
        L.remove(L[idx2 - 1])

def remainderOne(L):
    remainderEquals2Holder = [-1,-1]
    for i in range(len(L)):
        if L[i] % 3 == 1:
            removeElements(L, i)
            return 
                
        if L[i] % 3 == 2:
            if remainderEquals2Holder[0] == -1:
                remainderEquals2Holder[0] = i
            elif remainderEquals2Holder[1] == -1:
                remainderEquals2Holder[1] = i

    if remainderEquals2Holder[0] != -1 and remainderEquals2Holder[1] != -1:
        removeElements(L, remainderEquals2Holder[0], remainderEquals2Holder[1])
        return 

def remainderTwo(L):
    remainderEquals1Holder = [-1,-1]
    for i in range(len(L)):
        if L[i] % 3 == 2:
            removeElements(L, i)
            return 
        elif L[i] % 3 == 1:
            if remainderEquals1Holder[0] == -1:
                remainderEquals1Holder[0] = i
            elif remainderEquals1Holder[1] == -1:
                remainderEquals1Holder[1] = i

    if remainderEquals1Holder[0] != -1 and remainderEquals1Holder[1] != -1:
        removeElements(L, remainderEquals1Holder[0], remainderEquals1Holder[1])
        return 




