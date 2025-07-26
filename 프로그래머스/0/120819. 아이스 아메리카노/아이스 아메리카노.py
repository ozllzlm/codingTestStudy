def solution(money):
    answer = []
    qou = money // 5500
    re = money % 5500
    answer = [qou , re]
    return answer