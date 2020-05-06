def solution(n):
    operations = 0
    num_pellets = int(n)
    #loop until we hit 1
    while num_pellets != 1:
        if num_pellets % 2 == 0:
            #Figure out how many times we can divide by 2 by counting the binary strings trailing zeros. Perform bitshift and add the number to operations
            shift_right = count_zeros(bin(num_pellets)[2:])
            num_pellets = num_pellets>>shift_right
            operations += shift_right
        else:
            #When numbers are odd we can move up one number or down one number
            #So we need to figure out with one of those numbers can be divided by 2 the most 
            #That number will have the most trailing zeros
            num_zeros_plus_one = count_zeros(bin(num_pellets + 1)[2:])
            num_zeros_minus_one = count_zeros(bin(num_pellets -1)[2:])
            #Edge case concerning the number 3 b10 can be divided faster than b100 so go with num_pellets - 1 in that case
            if num_zeros_plus_one > num_zeros_minus_one and num_pellets != 3:
                num_pellets = (num_pellets + 1)>>num_zeros_plus_one
                #Adding one to account for + or - operation
                operations += num_zeros_plus_one + 1
            else:
                num_pellets = (num_pellets - 1)>>num_zeros_minus_one
                operations += num_zeros_minus_one + 1
    return operations

def count_zeros(binary_string):
    last_index = len(binary_string) - 1
    count = 0
    for i in range(last_index, -1, -1):
        if binary_string[i] != '0':
            break
        count += 1
    return count

print(solution("47236589782713289507328194732891478913207489312093047320147832914789320578978978978921734891111111111111111111111123456788888888888888888888888888888888888888888888888888888888888888888888888832074892017589279302748213074893275895892013478932"))
