import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lista = list(map(int, input().split()))

listsum = [0] # 인덱스 문제로 ,,,계속 헤맸다,,,여기에 0을 안 넣어서,, 암튼 해결 ~
temp = 0

for i in range(n):
    temp += lista[i]
    listsum.append(temp)
    
for i in range(m):
    a, b = map(int,input().split())
    print(listsum[b]-listsum[a-1])