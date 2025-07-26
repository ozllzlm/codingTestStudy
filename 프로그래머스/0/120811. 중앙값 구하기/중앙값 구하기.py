def solution(array):
    answer = 0
    ## 정렬 후 가운데 출력
    array.sort()
    return array[len(array)//2]