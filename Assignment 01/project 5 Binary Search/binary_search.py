
import random
import time

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2  # 2

    # we'll check if l[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':


    length = 10000
    # build a sorted list of length 10000
    sorted_list = list()
    # while len(sorted_list) < length:  another method for creating a list
    #     sorted_list.add(random.randint(-3*length, 3*length))

    for  i in range(1,10001): # by me
        sorted_list.append(i)
    
    print(sorted_list)
    
    #checking time for naive searching algorithm
    
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    #checking timing for binary search algorithm

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")


