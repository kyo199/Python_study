
# for

for i in range(5):
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")

for i in range(3):
  print(i)
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")


# while
# while 문은 무한 루프를 돌릴때 사용

i = 0

while i < 3 :
  print(i) # i = 0
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")
i = i + 1 # i = 0 + 1 = 1, i = 1 + 1 = 2, i = 2 + 1 = 3


# break
# while문은 break 명령어로 멈출수 있다
i = 0
while True:
  print(i)
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")
  i = i + 1

  if i > 2:
   break

for i in range(100):
  print(i)
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")
  
  if i > 2:
   break


# continue

for i in range(5):
  print(i)
  print("철수 : 안녕 영희야 뭐해?")
  print("영희 : 안녕 철수야, 그냥있어.")

  continue

  print("제이스 : 안녕 철수와 영희야!")

for i in range(3):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야, 그냥 있어.")

  if i == 1:
    continue

  print("제이스: 안녕 철수와 영희야!")
