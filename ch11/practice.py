import theater_module # 모듈 가져오기
theater_module.price(3) # 3명이 영화를 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이 조조 영화를 보러 갔을 때 가격
theater_module.price_soldier(5) # 군인 5명이 영화를 보러 갔을 때 가격

import theater_module as mv # theater_module을 별명인 mv로 사용한다는 의미
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module에서 모든 기능을 가져와 사용함
# from random import *
price(3) # theater_module.을 작성할 필요 없음
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 모듈에서 일부 함수만 가져와 사용함
price(5) # 5명
price_morning(6) # 6명
price_soldier(7) # import하지 않아서 사용 불가

# price_soldier를 별명인 price로 대체 사용
from theater_module import price_soldier as price
price(5) # price_soldier() 함수 호출