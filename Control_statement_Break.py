wordslist = []

while True :
	word = input("단어를 입력하세요. 1 입력시 중단됩니다.:")
	if word == "1" :
		break
	else :
		wordslist.append(word)

for w in wordslist :
	print(w, end = ' ')