def solution(n):
    answer = 0
    
    # 0보다 작으면 1더함, 아니면 그냥 출력
    if n%7 != 0:
        answer = (n//7) + 1
    else:
        answer = n//7
    return answer