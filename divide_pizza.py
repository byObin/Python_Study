def solution(n):
    answer = [i for i in range(1,16) if (7*i)//n >= 1]
    return min(answer)
    # return (n - 1) // 7 + 1