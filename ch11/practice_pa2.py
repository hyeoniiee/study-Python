from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
language = input("어떤 언어를 좋아하세요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))
print(dir())
import random # random 모듈 가져다 쓰기
print(dir())
import pickle # pickle 모듈 가져다 쓰기
print(dir())

import random
print(dir(random))
lst = [1, 2, 3]
print(dir(lst))
name = "Jim"
print(dir(name))

import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 출력

import os
print(os.getcwd()) # 현재 작업 폴더 위치(경로)
folder = "sample_dir"
if os.path.exists(folder): # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제했습니다.") # 삭제 문구 출력
else: # 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성했습니다.")
print(os.listdir()) # 현재 작업 폴더 안의 폴더와 파일 목록 출력

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초

import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일째 날짜 저장
print("우리가 만난 지 100일은", today + td) # 오늘부터 100일 후 날짜