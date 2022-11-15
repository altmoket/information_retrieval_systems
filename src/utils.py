
def booleanToInt(boolean):
    if boolean:
        return 1
    return 0

def matchText(text1, text2):
    return text1 == text2

def existItemInList(term, doc):
    EXIST = True
    for docTerm in doc:
        if matchText(docTerm, term):
            return EXIST
    return not EXIST
