## 패키지 : 모듈들을 모아둔 집합.
import travel.thailand # import : 모듈, 패키지만 가능. 클래스는 불가.
trip_to = travel.thailand.ThaiilandPackage() # 클래스
trip_to.detail()

from travel.thailand import ThaiilandPackage # from 쓰면 클래스 import 가능
trip_to = ThaiilandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

## __all__
from random import * # random 내 모든 것을 사용
from travel import * # 개발자가 __init__.py 파일에서 공개범위를 설정해야 함.
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThaiilandPackage()
trip_to.detail()

