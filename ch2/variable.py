# 애완동물을 소개해 주세요!
# 변수 : 어떤 값을 저장하는 공간

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal +  " 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# str() 은 값의 자료형을 문자열로 바꾸는 기능을 하는 명령어

print(name, "는 " , age, "살이며, " , hobby, "을 아주 좋아해요")
# , 를 사용하면 형변환을 하지 않아도 되고, 값과 값 사이에 빈칸을 하나씩 포함한다.

print(name + "는 어른일까요?? " + str(is_adult))

