def solution(my_string, letter):
    # my_string에 letter 문자 여부 검사
    if  my_string.find(letter) == -1:    # 없으면
        return my_string
    else:        #있으면
        return my_string.replace(letter,'')