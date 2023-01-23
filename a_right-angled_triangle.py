n = int(input())
for i in range(1,n+1):    # 첫번째 줄부터 n번째 줄까지 반복
    for j in range(1,i+1):    # * 출력횟수는 j(몇번째 줄)만큼 반복
        print('*', end='')    # * 출력 후 줄바꿈 방지 위해 end=''
    print('\n', end='')        # 줄바꿈 후 또 줄바꿈으로 빈 행 발생 방지 위해 end=''