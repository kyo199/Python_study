nums = []

while True :
	num = int(input("숫자를 입력하세요. -1 입력시 중단됩니다.:"))
	if num == -1 :
		break #반복문 탈출
	else :
		if num % 2 == 1 :
			continue #반복문 맨 처음으로
		nums.append(num)
		
for n in nums:
	print(n, end = ' ')