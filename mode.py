def solution(array):
    #count 딕셔너리 생성해서 횟수 세기
    count = {}  # count dictionary 선언
    for num in array:   # 입력받은 array의 모든 원소를 반복
        if num not in count:    # array원소가 count에 없으면
            count[num] = 0      # count에 그 원소값 넣고 value 0으로 설정
        count[num] +=1          # array원소가 count에 있으면 value에 1 추가
    
    # 가장 큰 빈도수 찾기
    max_val = 0
    for k, v in count.items(): # 딕셔너리 자료의 키와 값을 쌍으로 하여 반복
        if v > max_val:         # v(빈도수)가 가장 큰 값 찾기
            max_val = v
    
    max_cnt = [k for k,v in count.items() if v == max_val]  # 최빈값 max_cnt리스트에 넣기
    if len(max_cnt) >1 :    # 최빈값이 1개 초과할 경우
        return -1
    else:
        return max(count, key=count.get)    # max함수 안의 값 중 가장 큰 값 리턴