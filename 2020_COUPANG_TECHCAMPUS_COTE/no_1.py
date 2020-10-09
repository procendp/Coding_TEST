def solution(N): # N : 숫자 아무거나
    k = 1
    answer = 0
    for k in range(1, 11):
        while N // k >= 1:
            remain = N % k
            N = N // k
            answer = remain + answer
            if N < k :
                answer = N + answer
        
    return answer

print(solution(10))
print(solution(14))


# number = int(input("숫자를 입력하세요: "))
# n = int(input("변환할 진수를 입력하세요: "))

# answer = ""

# while number // n >= 1:
#     remain = number % n
#     number = number // n
#     answer = str(remain) + answer
#     if number < n :
#         answer = str(number) + answer

# print("변환 값: %s(%s)" % (answer, n))