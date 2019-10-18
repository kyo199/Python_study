
# 리스트 :: 엘레멘트 여러개을 묶을때 사용.
# 표현방식 2가지
x = list()
y = []

print(x)
print(y)


x = [1,2,3,4]
y = ["hello", "world"]
z = ["Bye", 1,2,3,]

print(x)
print(y)
print(z)
print(x + y)

# Element 변경
x = [1,2,3,4]
#    0 1 2 3    프로그램에서는 0부터 자리를 매긴다.

print(x[3])  # 4가 출력됨

x[3] = 10
print(x)  # [1,2,3,10]으로 출력됨

# len :: 리스트의 사이즈를 알려달라고 함수
x = [1,2,3,4]

num_elements = len(x)
print(num_elements) # 4 가 출력

# sorted :: 정렬을 시켜주는 함수
x = [4,2,3,1]

y = sorted(x)
print(y)  # [1,2,3,4] 출력

# sum :: 리스트의 elements가 숫자로 이뤄져있을경우 전부 더해주는 함수
x = [1,2,3,4]

z = sum(x)
print(z) # 10출력

# 반복문을 같이 쓰기

x = [1,2,3,4]
y = ["hello", "there"]

for n in y: # 리스트에 elements를 순서대로 보여줘. 라는 반복문
  print(n)


# index :: elements 위치 찾기

x = [1,2,3,4]
y = ["hello","there"]

print(x.index(3)) # 4 출력
print(y.index("hello")) # 0 출력


# in :: list 안에 물어보는게 있는지 나타내는 함수
y = ["hello", "there"]

print("hello" in y) # True 값 출력

or

if "hello" in y:
  print("hello 가 있어요.")


# 튜플
# 표현방식 2가지

x = tuple()
y = ()

print(x)
print(y)


# list에서 사용했던 함수들을 튜플에서도 사용가능

x = (1,2,3)
y = ('a','b','c')
z = (1,"hello","there")

print(x + y)
print('a' in y)
print(z.index(1))


# 하지만 Assignment = 튜플안의 값을 업데이트 하는것은 안됨
x = (1,2,3)
y = ('a','b','c')
z = (1,"hello","there")

x[0] = 10

# 가변 (mutable): 값을 바꿀수 있음 - 리스트
# 불변 (immutable) : 값을 바꿀수 없음 - 튜플


# 딕셔너리 :: ket 와 value로 이루어져 있는 자료구조
# 표현방식 2가지
x = dict()
y = {}

print(x)
print(y)

# 딕셔너리 예제
x = {
  "name": "제이스",
  "age": 20,
} 

print(x)
print(x["name"])
print(x["age"])

# key 값에는 불변한것맛 쓸수있어서 가변인 list는 key로 쓸수없다.
x = {
  0: "Winner",
  1: "hello",
  "age": 20,
}

print(x[0])
print(x[1])
print(x["age"])
print("age" in x)
print("name" in x)

# 딕셔너리에서 유용한 함수
# 1. keys
# 2. values
x = {
  0: "Winner",
  1: "hello",
  "age": 20,
}

print(x.keys())
print(x.values())

# 딕셔너리에서 반복문 사용하기
x = {
  0: "Winner",
  1: "hello",
  "age": 20,
}

for key in x:
  # print(key)
  # print(x[key])
  print("key: " + str(key))
  print("value: " + str(x[key]))

# 딕셔너리 안에 있는 값을 바꾸기
x = {
  0: "Winner",
  1: "hello",
  "age": 20,
}

x[0] = "위너"
print(x)

or

x["school"] = "air"
print(x)