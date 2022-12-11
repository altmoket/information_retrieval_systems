from src.core import rankingOfUserQuery
import sys

def main():
    arguments = sys.argv
    lengthArgs = len(arguments)
    ranking = None
    if lengthArgs == 2:
        query = arguments[1]
        ranking = rankingOfUserQuery(query)
    elif lengthArgs == 3:
        query = arguments[1]
        umbral = arguments[2]
        ranking = rankingOfUserQuery(query, float(umbral))
    elif lengthArgs < 2 or lengthArgs > 3:
        print("Usage: python main.py \'query\' (umbral)?")
        return
    return ranking

MAIN = "__main__"
if __name__ == MAIN:
    main()
