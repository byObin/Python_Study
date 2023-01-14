def solution(price):
    if price>=100000:    
        if price>=300000:
            if price>=500000:
                return int(0.8*price) # 구매액 50만 이상일 경우 리턴
            return int(0.9*price) # 구매액 30만 이상일 경우 리턴
        return int(0.95*price) # 구매액 10만 이상일 경우 리턴
    return price    # 구매액 10만 미만일 경우 리턴 