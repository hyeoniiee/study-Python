import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

"""
import travel.thailand.ThailandPackage # 클래스 import 불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
"""

# travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
from travel.thailand import ThailandPackage 
trip_to = ThailandPackage() # from~import 문에서는 travel.thailand. 제외
trip_to.detail()

#from random import *
from travel import *
trip_to = vietnam.VietnamPackage() # 베트남
#trip_to = thailand.ThailandPackage() # 태국
trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
# from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand)) # thailand 모듈 위치