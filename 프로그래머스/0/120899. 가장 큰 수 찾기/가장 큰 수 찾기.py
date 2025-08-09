def solution(array):
    max_value = max(array)         # 배열에서 최댓값 찾기
    max_index = array.index(max_value)  # 최댓값의 인덱스 찾기
    return [max_value, max_index]
