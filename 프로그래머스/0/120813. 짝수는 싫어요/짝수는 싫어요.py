def solution(n):
    answer = []
    for i in range(0, n+1):
        if(i%2 == 1):   
            answer.append(i)

    return answer