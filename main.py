# This is a sample Python script.
import cmath
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# 1; - for (-1); + for add; * for multiplication; e for exponential.
# use prefix

ansList = []
newList = [1, -1]
tolerance_1 = 1e-6
tolerance_2 = 1e-12


##make tree structure (dictionary)


def parse(op, val1, val2):
    if op not in ("+", "*", "e"):
        raise RuntimeError
    if op == "+":
        return val1 + val2
    if op == "*":
        return val1 * val2
    if op == "e":
        try:
            return (val1 ** val2)
        except:
            return None


def zero_check(cnum):
    re = cnum.real
    im = cnum.imag
    if (abs(cnum.real) < tolerance_2):
        re = 0
    if (abs(cnum.imag) < tolerance_2):
        im = 0
    return complex(re, im)


def add_new_item(item1, item2):
    for op in ["+", "*"]:
        result = parse(op, item1, item2)
        if result is not None:
            tempList.append(result)

    result = parse("e", item1, item2)
    if result is not None:
        tempList.append(result)
    result = parse("e", item2, item1)
    if result is not None:
        tempList.append(result)


if __name__ == '__main__':

    start_time = time.time()

    for layer in range(4):
        tempList = []
        for i1 in range(len(ansList)):  # item1 from the old List
            for i2 in range(i1, len(newList)):  # item2 from the new List
                add_new_item(ansList[i1], newList[i2])
        # new and new
        for i1 in range(len(newList)):  # item1 from the new List
            for i2 in range(i1, len(newList)):  # item2 from the new List
                add_new_item(newList[i1], newList[i2])

        ansList.extend(newList)  # merge new element from last layer into answer.
        # maintaining no new combination can be formed within ansList.

        # remove repeat prefix expression
        # remove repeat in tempList
        tempList_no_repeat = []
        for item in tempList:
            if item not in tempList_no_repeat:
                tempList_no_repeat.append(item)

        # then add element to newList if its not in ansList.
        # ansList.extend(tempList)
        newList = []
        for new_item in tempList_no_repeat:
            new_item = zero_check(new_item)
            flag_duplicate = 1
            for old_item in ansList:
                if cmath.isclose(new_item, old_item, rel_tol=tolerance_1, abs_tol=tolerance_1):
                    flag_duplicate = 0
                    break
            if flag_duplicate:
                newList.append(new_item)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")
    print(f"length of answer = {len(ansList)}")
    time.sleep(3)

    for i in ansList:
        print(i)
