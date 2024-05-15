hexNumbers = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    string_list = list(hexNum)
    string_list.reverse()
    for elements in string_list:
        if elements not in hexNumbers:
            return None
            break
    #print(string_list)
    result_list = []
    for value in string_list:
        position = string_list.index(value)
        key_val = hexNumbers.get(value)
        #print(value,position,key_val)
        if position == 0:
            result = key_val
            #print(result)
            result_list.append(result)
        else:
            result = pow(16, position) * key_val
            #print(result)
            result_list.append(result)
    final_result = sum(result_list)
    return final_result


print(hexToDec("CMA"))
