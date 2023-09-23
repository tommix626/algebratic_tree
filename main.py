import cmath
import time

ansList = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
ansList[1] = [1, -1]
allElementSet = set([])  # hashset for all the values generated to detect redundancy.
tolerance_1 = 1e-1
tolerance_2 = 1e-12


def limit_precision(cnum, precision=9):
    """
    Limit the number of effective digits for a complex number.
    """
    re = round(cnum.real, precision)
    im = round(cnum.imag, precision)
    return complex(re, im)


##make tree structure (dictionary)


def calculate(op, val1, val2):
    """
    calculate and limit the precision of the result op(val1,val2)
    """
    if op not in ("+", "*", "e"):
        raise RuntimeError
    if op == "+":
        result = val1 + val2
    if op == "*":
        result = val1 * val2
    if op == "e":
        try:
            result = (val1 ** val2)
        except:
            return None
    return limit_precision(result)


def add_new_item(item, layer):
    """
    add item to the ansList and allList, if not redundant.
    """
    # print("test")
    if item not in allElementSet:
        allElementSet.add(item)
        ansList[layer].append(item)


def combine_items(item1, item2, layer):
    """
    generate the composition of the two item by adding a root operation.
    Also save to according ansList[layer] if not redundant.
    """
    for op in ["+", "*"]:
        result = calculate(op, item1, item2)
        if result is not None:
            add_new_item(result, layer)

    result = calculate("e", item1, item2)
    if result is not None:
        add_new_item(result, layer)

    result = calculate("e", item2, item1)
    if result is not None:
        add_new_item(result, layer)


if __name__ == '__main__':

    start_time = time.time()

    for layer in range(3, 27, 2):
        for left_complexity in range(1, (layer + 1) // 2, 2):
            # print(f"left_complexity = {left_complexity}")
            for i1 in ansList[left_complexity]:
                for i2 in ansList[layer - left_complexity -1]:
                    combine_items(i1, i2, layer)
        print(f"layer {layer} has len {len(ansList[layer])}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time} seconds")
    anscnt = 0
    for i in range(1, 27, 2):
        anscnt+=len(ansList[i])
        print(f"all layer {i} has len {anscnt}")
    #     for i1 in range(len(ansList)):  # item1 from the old List
    #         for i2 in range(i1, len(newList)):  # item2 from the new List
    #             add_new_item(ansList[i1], newList[i2])
    #     # new and new
    #     for i1 in range(len(newList)):  # item1 from the new List
    #         for i2 in range(i1, len(newList)):  # item2 from the new List
    #             add_new_item(newList[i1], newList[i2])
    #
    #     ansList.extend(newList)  # merge new element from last layer into answer.
    #     # maintaining no new combination can be formed within ansList.
    #
    #     # remove repeat prefix expression
    #     # remove repeat in tempList
    #     tempList_no_repeat = []
    #     for item in tempList:
    #         if item not in tempList_no_repeat:
    #             tempList_no_repeat.append(item)
    #
    #     # then add element to newList if its not in ansList.
    #     # ansList.extend(tempList)
    #     newList = []
    #     for new_item in tempList_no_repeat:
    #         new_item = zero_check(new_item)
    #         flag_duplicate = 1
    #         for old_item in ansList:
    #             if cmath.isclose(new_item, old_item, rel_tol=tolerance_1, abs_tol=tolerance_1):
    #                 flag_duplicate = 0
    #                 break
    #         if flag_duplicate:
    #             newList.append(new_item)
    #
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"Time taken: {elapsed_time} seconds")
    # print(f"length of answer = {len(ansList)}")
    # time.sleep(3)
    #
    # for i in ansList:
    #     print(i)
