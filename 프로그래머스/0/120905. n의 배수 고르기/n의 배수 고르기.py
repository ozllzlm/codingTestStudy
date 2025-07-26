def solution(n, numlist):
    answer_arr = []
    ## numlist 반복문에서 n으로 나눠서 0인 매개변수 
    for i in numlist:
        if i % n == 0:
            answer_arr.append(i)

    return answer_arr