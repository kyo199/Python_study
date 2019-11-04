num = int(input("입력할 단어 개수를 입력하세요:"))
wordslist = []

for i in range(num) :
    word = input("단어를 입력하세요:")
    wordslist.append(word)

for w in wordslist :
    print(w, end = ' ')   