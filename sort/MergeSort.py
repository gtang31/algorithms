"""
Performs a Merge Sort.
_do_merge() function takes two lists and combines them into one
sorted list.

merge_sort() function takes any list and sorts it using merge sort paradigm
"""
__author__ = "Gary Tang"
def _do_merge(_a, _b):
    """
    merges two lists into one ordered list
    @param _a: list[int]
    @param _b: list[int]
    @return merged: list[int]
    """
    merged = list()
    # set counters
    j, k = 0, 0

    # sort _a, _b into one list 
    while j < len(_a):
        if _a[j] < _b[k]:
            merged.append(_a[j])
            j += 1
        else:
            merged.append(_b[k])
            if k + 1 == len(_b):
                remaining = _a[j:]
                break
            k += 1
    else:
        remaining = _b[k:]
    
    merged.extend(remaining)
    print "Merging {0} and {1} into: {2}".format(_a, _b, merged)
    return merged


def merge_sort(unordered_list):
    """
    @param unordered_list: list[int]
    @return temp: list[int] 
    """
    if not unordered_list:
        return []
        
    temp = [0]*len(unordered_list)
    for i in xrange(len(unordered_list)):  # make each element into a list
        temp[i] = [unordered_list[i]]
    
    # recombine fragmented parts into one sorted list
    while len(temp) > 1:
        sort = list()
        for i in range(1,len(temp),2):
            if i + 2 == len(temp):  # handles when input is odd length
                _a = _do_merge(temp[i], temp[i+1])
            else:
                _a=temp[i]
            _b=temp[i-1]
            
            sort.append(_do_merge(_a, _b))
        temp = sort
    return temp[0] 


assert merge_sort([]) == []
assert merge_sort([4,2,3,1,10,6,5,8,9,7,1]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert merge_sort([2,1,1,2,3,1]) == [1, 1, 1, 2, 2, 3]
assert merge_sort([7,99,53,12,60,35,65,2]) == [2, 7, 12, 35, 53, 60, 65, 99]
