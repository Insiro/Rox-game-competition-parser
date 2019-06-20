

def Short(str1):
    strs = str1.lower()
    if(strs == 'jan'):
        return '01'
    elif(strs == 'feb'):
        return '02'
    elif(strs == 'mar'):
        return '03'
    elif (strs == 'apr'):
        return '04'
    elif (strs == 'may'):
        return '05'
    elif (strs == 'jun'):
        return '06'
    elif (strs == 'jul'):
        return '07'
    elif (strs == 'aug'):
        return '08'
    elif (strs == 'sep'):
        return '09'
    elif (strs == 'oct'):
        return '010'
    elif (strs == 'nov'):
        return '011'
    elif (strs == 'dec'):
        return '012'
    else:
        return None
