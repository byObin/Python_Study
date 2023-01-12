def solution(slice, n):
    # n(인원 수)를 slice(조각 수)로 나눈 몫, 나머지를 d,m에 넣기
    d, m = divmod(n, slice)
    
    # 필요한 피자 판 수(d)를 반환하는데, 
    # 나머지가 0이 아닐 경우 한 판이 더 필요하므로 1 더하기
    return d + int(m != 0)