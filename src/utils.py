
def booleanToInt(boolean):
    if boolean:
        return 1
    return 0

def matchText(text1, text2):
    return text1 == text2

def existItemInList(item, list):
    EXIST = True
    for itemList in list:
        if matchText(item, itemList):
            return EXIST
    return not EXIST
