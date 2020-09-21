import random

# creates a random list with a random lenght
def getRandomList():
    unsorted = []
    for i in range(0, random.randint(1, 1000), 1):
        unsorted.append(random.randint(1, 1000000))
    return unsorted


def selectionSort(list):
    # loops through all the list elements
    for i in range(len(list)):

        #Find the minimum element in remaining unsorted list
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        # Swaps the found smallest element with the first index
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

print(selectionSort(getRandomList()))
