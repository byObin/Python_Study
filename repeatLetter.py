# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''
    
    for i in my_string:
        for j in range(1,n+1):
            answer += i
 
    return answer