def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:    # num_list값에 접근
        if i%2 == 0:     # 2로 나눈 나머지가 0이면
            even += 1    # (=짝수면) even값 1증가
        else:            # 2로 나눈 나머지가 0이 아니면
            odd += 1     # (=홀수면) odd값 1증가
    answer = [even, odd]
    return answer