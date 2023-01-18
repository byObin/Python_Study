def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(-1, length, -1):
        answer.append(num_list[i])
    return answer