def solution(hp):
    answer = 0
    ## 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력
    print(hp / 5)
    a1 = hp // 5
    a2 = (hp % 5) // 3
    a3 = (hp % 5) % 3
    return a1 + a2 + a3