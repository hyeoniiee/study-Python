"""
Quiz) 비밀번호 만들기
사이트별로 비밀번호를 생성하는 프로그램을 작성하시오

조건1. http:// 부분은 제외한다.
조건2. 처음 만나는 점 . 부분도 제외한다.
조건3. 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e'의 개수 + '!'로 구성한다.

출력문 : http://naver.com의 비밀번호는 nav51!입니다.
"""

url = "http://naver.com"
code = url.replace("http://", "")
print(code)
code = code[:code.index(".")]
pw = code[:3] + str(len(code)) + str(code.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, pw))

"""
셀프체크
영어 문장이 주어졌을때 첫 번째 글자는 대문자, 나머지 글자는 소문자로 변환하는 프로그램 작성하시오.

출력문 
주어진 문장 : the early bird catches the worm.
출력문 : The early bird catches the worm.
"""
string = "the eARly BIrd catches THE WORM"
print(string[0].upper() + string[1:].lower())