def solution(arr):
    result = []
    for num in arr:
        if num >= 50 and num % 2 == 0:      # 50 이상 짝수
            result.append(num // 2)
        elif num < 50 and num % 2 == 1:     # 50 미만 홀수
            result.append(num * 2)
        else:
            result.append(num)              # 조건에 해당 안 됨
    return result