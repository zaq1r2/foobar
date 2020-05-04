def numsNotDivisableByThree(n):
    nums = []
    for i in range(n):
        if i % 3 != 0:
            nums.append(i)

    return nums

print(numsNotDivisableByThree(9999999))