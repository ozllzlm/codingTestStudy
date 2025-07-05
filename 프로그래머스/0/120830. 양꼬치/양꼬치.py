def solution(n, k):
    answer = 0
    # 무료인 음료수 수
    drink = int(n/10)
    # (양꼬치 갯수 * 가격) + (구매음료수-무료음료수)*가격
    answer = n * 12000 + (k - drink) * 2000
    return answer