
# animal package
# dog, cat modules
# dog, cat modules can say  "Hi"

# 첫번째 예제
from animal import dog # animal 패키지에서 dog 이라는 모듈을 갖고와줘
from animal import cat # animal 패키지에서 cat 이라는 모듈을 갖고와줘

d = dog.Dog() # instance
d.hi()

c = cat.Cat() # instance
c.hi()

# 두번째 에제
from animal import dog
from animal import cat

from animal import *

d = Dog()
c = Cat()

d.hi()
c.hi()