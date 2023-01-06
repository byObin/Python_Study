def solution(array):

    # return sorted(array)[len(array) // 2]

    array.sort()
    midIdx = len(array)//2
    return array[midIdx]