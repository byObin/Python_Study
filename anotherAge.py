def solution(age):
    answer = ''
    # 변환 테이블을 딕셔너리로 선언
    convert = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    for i in str(age):    # int로 들어온 age를 str으로 변환해 반복
        answer += convert[i]
    return answer