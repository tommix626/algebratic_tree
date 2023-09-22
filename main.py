# This is a sample Python script.
import math
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# 1; - for (-1); + for add; * for multiplication; e for exponential.
# use prefix

ansList = [[1], [-1]]


##make tree structure (dictionary)

def parse(s, start_index):
    """

    :param s: the sentence list s.
    :param start_index: the start element in the list s
    :return: end: end index of the start_index subtree
    :return: val:[List] or int, depending on the value of the current subtree that starts at start_index.
    """
    if type(s) != list:
        return (s,1)
    op = s[start_index]
    if op != "+" and op != "*" and op != "e":
        return op, start_index

    val1, end1 = parse(s, start_index + 1)
    val2, end2 = parse(s, end1 + 1)
    if (type(val1) != list) and (type(val2) != list):
        if op == "+":
            return val1 + val2, end2
        if op == "*":
            return val1 * val2, end2
        if op == "e":
            try:
                return (math.pow(val1, val2)), end2
            except:
                pass

    if type(val1) != list:
        val1 = [val1]
    if type(val2) != list:
        val2 = [val2]
    val = []
    val.extend([op])
    val.extend(val1)
    val.extend(val2)

    return val, end2


if __name__ == '__main__':
    # s = ["e","e",2,-1,3]
    # print(parse(s,0)) # returns: (['e', 0.5, 3], 4)

    start_time = time.time()

    # Your code here

    for layer in range(2):

        tempList = []
        for i1 in range(len(ansList)):
            for i2 in range(i1,len(ansList)):
                for op in [["+"], ["*"]]:
                    op.extend(ansList[i1])
                    op.extend(ansList[i2])
                    op,_ = parse(op,0)
                    if type(op) != list:
                        op = [op]
                    tempList.append(op)
                op = ['e']
                op.extend(ansList[i1])
                op.extend(ansList[i2])
                op,_ = parse(op,0)
                if type(op) != list:
                    op = [op]
                tempList.append(op)

                op = ['e']
                op.extend(ansList[i2])
                op.extend(ansList[i1])
                op, _ = parse(op, 0)
                if type(op) != list:
                    op = [op]
                tempList.append(op)
        #remove repeat prefix expression
        seen = set()
        no_duplicates = []
        for item in tempList:
            tup = tuple(item)
            if tup not in seen:
                seen.add(tup)
                no_duplicates.append(item)
        ansList.extend(tempList)



    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")

    time.sleep(3)

    for i in ansList:
        print(i)
