import sys

leftstr = list(sys.stdin.readline())
# 개행 문자를 지우기 위해 사용
# readline().rstrip()을 사용해봤는데 계속 틀림 -> 테케는 안 틀렸음,,,
leftstr.pop()
rightstr = []
n = int(sys.stdin.readline())

for i in range(n):
    OPPEREND = sys.stdin.readline()
    
    if 'L' in OPPEREND and len(leftstr) != 0:
        rightstr.append(leftstr.pop())
    elif 'D' in OPPEREND and len(rightstr) != 0:
        leftstr.append(rightstr.pop())
    elif 'B' in OPPEREND and len(leftstr) != 0:
        leftstr.pop()
    elif 'P' in OPPEREND:
        k = OPPEREND.split()
        leftstr.append(k[1])

# rightstr을 뒤집어서 leftstr이랑 합치기
res = leftstr+rightstr[::-1]

# 리스트로 되어 있는 문자 리스트를 문자열로 정리해서 출력
print("".join(map(str,res)))