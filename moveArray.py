def solution(numbers, direction):
    answer = []
    length = len(numbers)
    if direction=="right":
        for i in range(0, length-1):
            answer.insert(i+1, numbers[i])
        answer.insert(0, numbers[length-1])
    else:
        answer.insert(-1, numbers[0])
        for i in range(1, length):
            answer.insert(i-1, numbers[i])
    return answer

#print(solution(	[4, 455, 6, 4, -1, 45, 6], "left"))