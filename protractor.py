def solution(angle):
    answer = 0
    if angle < 90:        # 예각인 경우
        answer = 1
    elif angle == 90:    # 직각인 경우
        answer = 2
    elif angle < 180:    # 둔각인 경우
        answer = 3
    elif angle == 180:    # 평각인 경우
        answer = 4
    return answer