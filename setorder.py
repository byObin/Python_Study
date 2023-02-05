def solution(emergency):
    answer = []
    priority = sorted(emergency, reverse = True)    # emergency를 내림차순 정렬해서 priority에 넣음
    for eInEmer in emergency:                       # emergency의 요소에 차례로 접근하면서
        for eInPri in priority:                     # priority의 요소에도 차례로 접근
            if eInPri == eInEmer:                   # 만약 두 요소의 값이 같으면
                answer.append(priority.index(eInEmer)+1)    # 해당 요소의 인덱스값에 1 더해서 answer에 값 추가
    return answer