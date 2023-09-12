# 숫자의 합 구하기
n = input()
numbers = list(input())
sum = 0

for number in numbers:
    sum += int(number)
    
print(sum)
