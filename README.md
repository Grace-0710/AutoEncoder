# AutoEncoder
AutoEncoder에 대해 실습합니다

MNIST를 가지고 학습을 하고 AutoEncoder를 통해서도 그대로 복원을 할 수 있도록! 아키텍쳐를 실습합니다

* 불필요한 정보를 삭제하기 위해 encod -> decode 본질적인 정보만 남기고자

* model.py
  
  <img width="241" alt="스크린샷 2023-03-18 오전 1 35 15" src="https://user-images.githubusercontent.com/84004919/225964939-bfa3066d-2a4f-4b9e-bd35-d2a12c13de25.png">

* verbose 옵션 : 상세한 로깅을 출력할지 말지 조정하는 파라미터
  (*로그 출력이 실행 속도에 영향을 줄 수 있다고 함)
  verbose = 0 : 출력X
  verbose = 1 : 자세히
  verbose = 2 : 함축적인 정보만
