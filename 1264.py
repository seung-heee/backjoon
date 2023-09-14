# 모음의 개수
vowel = ['a', 'e','i','o','u', "A","E","I", "O", "U"]
count = 0

while True:
    text = input()
    
    if text == "#":
        break
    else:
        for i in text:
            if i in vowel:
                count += 1
        
print(count)