money = int(input("가지고있는 금액을 입력하세요:"))

if money >= 5000 :
    print("택시를 탈 수 있습니다.")
elif money < 5000 and money >= 2000 :
    print("버스를 탈 수 있습니다.")
else :
    print("걸어가야 합니다.")