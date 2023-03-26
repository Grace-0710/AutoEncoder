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
* load_mnist 함수의 인수
  1. normalize : 입력 이미지의 픽셀값을 0.0~1.0 사이의 값으로 정규화를 할건지 // False면 원래 값 그대로 0~255 사이의 값 유지
  2. flatten : 입력 이미지를 1차원 배열로 만들건지 // False면 입력 이미지를 1x28x28의 3차원 배열로, True면 784개의 원소로 이뤄진 1차원 배열로 저장한다.
    -> flatten시, 파일에 값을 대입하기 위함 (flatten은 다차원 데이터를 1차원으로 펴주는 역할 )
  3. one_hot_label : 레이블을 원-팟 인코딩 형태로 저장할지를 정한다. // False면 '7'이나 '2'와 같이 숫자 형태의 레이블을 저장함
* torch.no_grad() :autograd를 끔으로써 메모리 사용량을 줄이고 연산 속도를 높히기 위함 -> 사실상 어짜피 안쓸 gradient인데 inference시에 굳이 계산할 필요X
  일반적으로 inference를 진행할 때는 torch.no_grad() with statement로 감싼다는 사실을 알면 된다.
* model.eval() : 이런 layer들의 동작을 inference(eval) mode로 바꿔준다는 목적으로 사용
* AutoEncoder 응용 자료 : https://towardsdatascience.com/what-are-stable-diffusion-models-and-why-are-they-a-step-forward-for-image-generation-aa1182801d46
