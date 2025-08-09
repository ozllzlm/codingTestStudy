def solution(my_string):
    answer = []

    ## list
    mylist = list(my_string)
    
    for i in mylist:
        if i.isdigit():
            answer.append(int(i))
    ## 오름차순
    answer.sort()
    return answer