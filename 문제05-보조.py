#숫자를 입력하고 입력받은 숫자가 몇번 박수를 치는지 알아보쟝

#방법 1 : 사람이 생각하는 방법
a = 31
문자열 = str(a)
카운트 = 0

for x in 문자열:
    if x in ['3','6','9']:
        카운트 += 1
        
print(카운트)


#방법 2 : 컴퓨터가 생각하는 방법
a = 31
카운트 = 0

while a:
    if a % 10 == [3,6,9]:
        카운트 += 1
    a = a // 10

print()