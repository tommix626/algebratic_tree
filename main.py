# This is a sample Python script.
import cmath
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
    if start_index==None:
        return None,None
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
                # print(val1**val2)
                return (val1**val2), end2
            except:
                return None,None

    if type(val1) != list:
        val1 = [val1]
    if type(val2) != list:
        val2 = [val2]
    val = []
    val.extend([op])
    val.extend(val1)
    val.extend(val2)

    return val, end2


def zero_check(cnum):
    re = cnum.real
    im = cnum.imag
    if(abs(cnum.real) < tolerance_2):
        re = 0
    if (abs(cnum.imag) < tolerance_2):
        im = 0
    return complex(re,im)

def add_new_item(item1,item2):
    for op in [["+"], ["*"]]:
        op.extend(item1)
        op.extend(item2)
        op, _ = parse(op, 0)
        if (_ == None):
            return
        if type(op) != list:
            op = [op]
        tempList.append(op)
    op = ['e']
    op.extend(item1)
    op.extend(item2)
    op, _ = parse(op, 0)
    if (_ == None):
        return
    if type(op) != list:
        op = [op]
    tempList.append(op)

    op = ['e']
    op.extend(item2)
    op.extend(item1)
    op, _ = parse(op, 0)
    if (_ == None):
        return
    if type(op) != list:
        op = [op]
    tempList.append(op)

if __name__ == '__main__':
    tolerance_1 = 1e-6
    tolerance_2 = 1e-12
    # s = ["e","e",-1,0.5,3]
    # print(parse(s,0)) # returns: (['e', 0.5, 3], 4)
    # time.sleep(100)
    start_time = time.time()

    # Your code here

    for layer in range(3):

        tempList = []
        for i1 in range(len(ansList)):
            if(i1%100 == 0):
                print(f"layer {layer}, i1={i1} out of {len(ansList)}")
            for i2 in range(i1,len(ansList)):
                add_new_item(ansList[i1],ansList[i2])

        # remove repeat prefix expression
        ansList.extend(tempList)
        no_duplicates = []
        for item1 in ansList:
            assert (len(item1) == 1)
            t = zero_check(item1[0])
            flag_duplicate = 1
            for item2 in no_duplicates:
                if(cmath.isclose(t, item2[0], rel_tol=tolerance_1, abs_tol=tolerance_1)):
                    flag_duplicate = 0
            if(flag_duplicate):
                no_duplicates.append([t])
        ansList = no_duplicates



    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")
    print(f"length of answer = {len(ansList)}")
    time.sleep(30)

    for i in ansList:
        print(i)

