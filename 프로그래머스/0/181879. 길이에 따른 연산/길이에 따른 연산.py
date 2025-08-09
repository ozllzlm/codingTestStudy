import math

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)           # 길이가 11 이상이면 합
    else:
        return math.prod(num_list)     # 길이가 10 이하이면 곱