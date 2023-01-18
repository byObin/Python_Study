sample_list = ['element1', 'element2', 'element3']

# 방법 1 : 리스트 반복해서 전체 출력, 인덱스 i는 0부터 1씩 증가
i = 0
for item in sample_list:
    print('{}번째 요소 : {}'.format(i, item))
    i += 1

# 방법 2 : 리스트 길이만큼 반복해서 출력, 리스트 인덱스 지정해 값에 접근
for j in range(len(sample_list)):
    print('{}번째 요소 : {}'.format(j, sample_list[j]))

# 방법 3 : enumerate 함수와 for문 사용
for k,value in enumerate(sample_list):
        print('{}번째 요소 : {}'.format(k, value))

print(enumerate(sample_list))   # enumerate 실행 결과 iterator 출력
print(list(enumerate(sample_list))) # enumerate함수 실행 -> list 변환 결과 튜플 형태 출력


