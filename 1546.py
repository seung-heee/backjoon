# 평균 구하기

n = int(input())
mylist = list(map(int, input().split()))

mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax/ n)