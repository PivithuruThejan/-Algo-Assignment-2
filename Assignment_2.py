from random import randint
import time


def binarySearch(element, array, i, j):
    if i <= j:
        mid = (i + j) / 2
        if array[mid] == element:#finds the mid point
            return mid
        else:
            if element < array[mid]:
                return binarySearch(element, array, i, mid - 1)
            else:
                return binarySearch(element, array, mid + 1, j)
    else:
        return -1


def randomizedBinarySearch(element, array, i, j):
    if i <= j:
        randomIndex = randint(i, j)#finds a random point
        if array[randomIndex] == element:
            return randomIndex
        else:
            if element < array[randomIndex]:
                return randomizedBinarySearch(element, array, i, randomIndex - 1)
            else:
                return randomizedBinarySearch(element, array, randomIndex + 1, j)
    else:
        return -1


def arrayPrepare(size):
    i = 0
    n = 0
    array = []
    members = []
    nonMembersTemperary = []
    nonMembersCount = 0
    membersCount = 0

    memberRange = size / 700

    while i < size:
        if randint(0, 1):
            array.append(n)
            if membersCount < 700 and i % memberRange == 0:
                members.append(n)
                membersCount += 1
            i += 1
        else:
            nonMembersTemperary.append(n)
            nonMembersCount += 1
        n += 1

    while nonMembersCount < 300:
        if randint(0, 1):
            nonMembersTemperary.append(n)
            nonMembersCount += 1
        n += 1
    nonMemberRange = len(nonMembersTemperary) / 300
    nonMembers = [nonMembersTemperary[i * nonMemberRange] for i in range(300)]

    return array, nonMembers, members


for k in range(5, 8):

    arraySize = 10 ** k

    print("Test " + str(k - 4) + "--------------------------------------------------")
    print("")

    array, nonMembers, members = arrayPrepare(arraySize)

    # Binary Search
    start = time.time()
    for m in members:
        binarySearch(m, array, 0, arraySize - 1)

    for nm in nonMembers:
        binarySearch(nm, array, 0, arraySize - 1)
    end = time.time()

    print("Binary Search(N = " + str(arraySize) + ") - Time(microseconds) : " + str(
        1000000 * (end - start) / 1000))
    print("")

    # Randomized Binary Search
    start = time.time()
    for m in members:
        randomizedBinarySearch(m, array, 0, arraySize - 1)

    for nm in nonMembers:
        randomizedBinarySearch(nm, array, 0, arraySize - 1)
    end = time.time()

    print("Randomized Binary Search(N = " + str(arraySize) + ") - Time(microseconds) : " + str(
        1000000 * (end - start) / 1000))
    print("")
