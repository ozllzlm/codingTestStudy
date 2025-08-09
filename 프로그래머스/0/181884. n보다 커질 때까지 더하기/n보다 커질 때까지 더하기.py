def solution(numbers, n):
    s = 0
    for x in numbers:
        s += x
        if s > n:
            return s