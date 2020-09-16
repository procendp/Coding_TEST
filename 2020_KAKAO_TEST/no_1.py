import re

def solution(new_id):
# 1
    new_id = new_id.lower()
# 2
    new_id = re.sub('[^a-z0-9-_.]', '', new_id) # 문자열 str
# 3
    id = new_id[0]

    for i in range(1, len(new_id)):
        if id[len(id)-1] == "." and new_id[i] == ".":
            continue
        else:
            id += new_id[i]
# 4
    while id.startswith('.') or id.endswith('.'):
        if id.startswith('.'):
            id = id[1:]
        elif id.endswith('.'):
            id = id[:-1]
        
# 5
    if not id:
        id = "a"


# 6
    if len(id) >= 16:
        id = id[:15]
        if id.endswith('.'):
            id = id[:-1]    

# 7
    while len(id) <= 2:
        id += id[len(id)-1]

    return id

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('..abcd[]/'))