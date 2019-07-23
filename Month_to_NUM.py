
def Short(str1):
    strs = str1.lower()
    if(strs == 'jan'):
        return 1
    elif(strs == 'feb'):
        return 2
    elif(strs == 'mar'):
        return 3
    elif (strs == 'apr'):
        return 4
    elif (strs == 'may'):
        return 5
    elif (strs == 'jun'):
        return 6
    elif (strs == 'jul'):
        return 7
    elif (strs == 'aug'):
        return 8
    elif (strs == 'sep'):
        return 9
    elif (strs == 'oct'):
        return '10'
    elif (strs == 'nov'):
        return '11'
    elif (strs == 'dec'):
        return '12'
    else:
        return None
