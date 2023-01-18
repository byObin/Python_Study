numbers = [2,3,4,5,8,9]
for num in numbers:
    if num%2 == 0:  # num이 짝수이면
        continue    # 건너뛰고 다음 반복으로
    print(num)