# 함수의 기본값 설정
def profile(name, age, main_lang):
  print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}".format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 학년, 반, 수업
def profile(name, age=17, main_lang="파이썬"):
  print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}".format(name,age,main_lang))

profile("유재석")
profile("김태호")

# 키워드 값을 이용한 함수 호출
def profile(name, age=17, main_lang="파이썬"):
  print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(age = 25, name = "김태호", main_lang = "자바" )

# 가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
  print(lang1, lang2, lang3, lang4, lang5)
# end = " " 사용시 문장을 출력후 이어서 밑에있는 문장을 계속 출력한다. 

profile("유재석", 20, "Python", "Java", "C", "C++", "c#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# *를 사용한다. 
def profile(name, age, *language):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
  for lang in language:
    print(lang, end = " ")
  print()

profile("유재석", 20, "Python", "Java", "C", "C++", "c#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")