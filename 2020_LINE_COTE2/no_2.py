def solution(ball, order):
    
    result = []
    for i in range(0, len(order)-1):
        if order[i] == ball[0] or order[i] == ball[int(len(ball)-1)]:
            result = result.iterable(order[i])
            
             # 같은 값을 추가
            
        else:
            continue
        
    print(result)

    return result

print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))