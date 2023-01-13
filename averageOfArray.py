def solution(numbers):
    answer = 0
    for n in numbers: #numbers 배열 원소 모두 더하기
        answer += n    
    
    return answer/len(numbers)    # 배열 원소 총합을 배열 길이로 나눔
    # return sum(numbers) / len(numbers) 아니면 이렇게 간단하게도 가능