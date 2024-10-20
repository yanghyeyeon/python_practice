# - 패키지 구조
```
C:\USERS\YHY40\DESKTOP\HYEYEON\PYTHON_PRACTICE\PRACTICE
|   calculation.sqlite3
|   main.py
|
+---dependencies
|       database.py
|
+---models
|       models.py
|
+---schemas
|       schemas.py
|
+---service
|       calculate_crud.py
|
\---__pycache__
        calculate_crud.cpython-312.pyc
        database.cpython-312.pyc
        main.cpython-312.pyc
        models.cpython-312.pyc
        schemas.cpython-312.pyc
```
## - 패키지 분리 이유
- 모듈화: 패키지를 통해 코드를 기능별로 분리하여, 각 모듈이 특정 책임을 지도록 했습니다. 이렇게 하면 코드 구조가 명확해지고, 각 모듈의 역할을 쉽게 이해할 수 있습니다.
- 재사용성:특정 기능을 수행하는 코드(예: 데이터베이스 접근, 인증 로직 등)를 별도의 패키지로 분리함으로써, 다른 프로젝트에서도 재사용할 수 있도록 했습니다. 이를 통해 코드의 중복을 줄이고 개발 효율성을 높였습니다.
- 가독성:관련된 기능들을 그룹화하여 패키지를 구성함으로써, 코드의 가독성을 향상시켰습니다. 개발자는 필요한 기능을 쉽게 찾을 수 있고, 코드를 읽기 더 용이하게 되었습니다.
- 유지보수: 코드의 특정 부분을 수정할 때, 해당 패키지만 수정하면 되므로 유지보수가 용이합니다. 이는 코드의 변경이 다른 부분에 미치는 영향을 최소화할 수 있게 도와줍니다.
  
## - 추가기능 설명
- 사칙연산외의 제곱과 제곱근 계산하는 기능을 추가 하였습니다
- 계산한 내용을 데이터베이스에 저장하여 그 계산 기록들을 볼수있게 전체조회 기능까지 추가 하였습니다.
  
