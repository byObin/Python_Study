import math     # gcd 사용 위해 import
 
def solution(n):
    # n과 6의 최소공배수 = 조건 만족 위해 필요한 최소의 피자 조각 수
    answer = (n * 6) // math.gcd(n,6)
    return answer//6    # 피자 조각 수를 구했으므로 6으로 나누어 판 수 구하기