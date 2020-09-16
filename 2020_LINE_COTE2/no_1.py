# 재포장

def solution(boxes):
    oned = []
    for i in boxes:
        oned += i # 1차원 리스트
    
    new = {}
    for j in oned:
        if j in new :
            new[j] += 1
        else:
            new[j] = 1

    result = []
    for key in new.keys() :
        if new[key] == 1:
            result.append(key) # 중복값 제거하고 남은 값.
    
    result = int(len(result) / 2)
    # print(int(len(result)/2)) # 중복값 제거 후, 중복되지 않는 값들 / 2 : 짝지어줘야하니까.

    return result

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))
