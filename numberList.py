# def solution(l, t):
#     runningSum = 0
#     for i in range(len(l) - 1):
#         runningSum = 0
#         runningSum += l[i]
#         for j in range(i+1, len(l)):
#             runningSum += l[j]
#             if runningSum == t:
#                 return [i, j]
#     return [-1,-1]


def solution(l,t):
    runningSum = l[0]
    i = 0
    j = 1 
    while j <= len(l):
        while runningSum > t and i < j - 1:
            runningSum -= l[i]
            i += 1
        if runningSum == t:
            return [i, j]

        if j < len(l):
            runningSum += l[j]

        j += 1
    
    return [-1,-1]

