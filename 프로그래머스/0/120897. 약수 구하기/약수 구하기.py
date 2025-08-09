import math

def solution(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: # 제곱수가 아니면 n/i도 약수
                divisors.append(n // i)
    return sorted(divisors)
