import numpy as np  #수치계산 라이브러리

x_train = np.array([1., 2., 3., 4., 5., 6.])        #x 입력 값
y_train = np.array([9., 12., 15., 18., 21., 24.])   #y 결과 값

W = 0.0         #초기화
b = 0.0

n_data = len(x_train)       #입력 값에 대한 길이
epochs = 5000               #5000번 실행
learning_rate = 0.01        #학습률 0.01 설정

for i in range(epochs):         #5000번 반복
    hypothesis = x_train * W + b        #가설함수, 예측한 결과 값
    cost = np.sum((hypothesis - y_train) ** 2) / n_data     #예측 값과 실제 값 오차 구함

    gradient_w = np.sum((W * x_train - y_train + b) * 2 * x_train) / n_data     #경사하강법, 가중치 구함
    gradient_b = np.sum((W * x_train - y_train + b) * 2) / n_data               #바이어스 구함

    W -= learning_rate * gradient_w             # 가증치 업데이트
    b -= learning_rate * gradient_b             # 편향 값 업데이트

    if i % 100 == 0:                                # 100번 째 에포크마다 학습 상황을 출력
        print('Epoch ({:10d}/{:10d}) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, epochs, cost, W, b))

# 최종 값 출력
    print('W: {:10f}'.format(W))
    print('b: {:10f}'.format(b))
    print('result : ')
    print(x_train * W + b)