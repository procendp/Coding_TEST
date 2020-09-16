# .split() 한 줄에 값 여러개 받을 때.

inputString = input() # list, input 값을 각 글자로 자르기.

# print(type(inputString))
# print(inputString)

for i in inputString:

if inputString.split() == '{' or '}':
    print("1")

"""
1. 괄호 있을 경우
    1) 열고 닫을 경우
    2) 닫고 열 경우

2. 괄호 없을 경우
    return 0
"""