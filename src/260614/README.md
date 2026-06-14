# 2026-06-14 Pygame 수업 진행 내용

## 최종 목표

이번 수업에서는 Pygame을 이용하여

- Meteor 객체 만들기
- Fighter 객체 만들기
- 여러 객체 관리하기
- 충돌 판정하기

를 학습하였다.

최종 결과는

- 운석 5개가 화면을 돌아다님
- 비행기를 방향키로 조작
- 충돌 시 빨간 원 표시

까지 구현하였다.

---

# 1. 게임 프로그램의 기본 구조

가장 먼저 게임 프로그램의 기본 구조를 만들었다.

```python
while running:
    update()
    draw()
    event()
```

실제 코드에서는

```python
while running:

    # 업데이트
    ...

    # 충돌 체크
    ...

    # 그리기
    ...

    # 이벤트 처리
    ...
```

형태로 작성하였다.

학습 내용

- 게임 루프
- 매 프레임 반복
- 화면 갱신

---

# 2. Meteor 클래스 만들기

Meteor 클래스를 새로 작성하였다.

Meteor 객체는 다음 정보를 가진다.

```python
self.x
self.y
self.dx
self.dy
```

의미

- x : 현재 위치
- y : 현재 위치
- dx : x 방향 속도
- dy : y 방향 속도

---

# 3. 생성자와 기본값

Meteor 생성자는 다음과 같이 작성하였다.

```python
def __init__(
    self,
    x=None,
    y=None,
    dx=None,
    dy=None
):
```

값이 주어지지 않으면

```python
Meteor()
```

랜덤 위치와 랜덤 속도를 사용한다.

```python
if x is None:
    x = random.randint(...)
```

학습 내용

- 생성자
- 매개변수 기본값
- None 사용법

---

# 4. 클래스 변수 사용하기

처음에는 객체마다 이미지를 로드하였다.

문제점

```python
Meteor()
Meteor()
Meteor()
Meteor()
Meteor()
```

를 만들면

```python
pygame.image.load(...)
```

가 여러 번 호출된다.

이를 해결하기 위해

```python
class Meteor:
    image = None
```

을 사용하였다.

```python
if Meteor.image is None:
    Meteor.image = pygame.image.load(...)
```

결과

- 이미지는 한 번만 로드
- 모든 Meteor 객체가 공유

학습 내용

- 클래스 변수
- 객체 변수와 클래스 변수 차이

---

# 5. 이미지 중심 좌표 사용하기

초기에는

```python
x
y
```

가 이미지의 좌상단 좌표였다.

수정 후에는

```python
x
y
```

를 이미지 중심 좌표로 사용하였다.

그래서 그림을 그릴 때

```python
screen.blit(
    image,
    (
        x - half_width,
        y - half_height
    )
)
```

를 사용한다.

장점

- 충돌 판정이 쉬움
- 거리 계산이 쉬움
- 원형 충돌 구현이 쉬움

---

# 6. 화면 경계 계산하기

이미지 크기를 고려하여

```python
Meteor.min_x
Meteor.max_x
Meteor.min_y
Meteor.max_y
```

를 계산하였다.

```python
Meteor.min_x = half_width
Meteor.max_x = screen_width - half_width
```

장점

- 화면 밖으로 나가지 않음
- 이미지가 잘리지 않음

---

# 7. move() 함수

운석은 매 프레임 이동한다.

```python
self.x += self.dx
self.y += self.dy
```

벽에 닿으면

```python
self.dx = -self.dx
```

```python
self.dy = -self.dy
```

로 방향을 반전시킨다.

학습 내용

- 이동
- 반사
- 속도 벡터

---

# 8. 여러 개의 Meteor 만들기

운석을 여러 개 생성하였다.

```python
meteors = [
    Meteor()
    for _ in range(5)
]
```

학습 내용

- 리스트 컴프리헨션
- 객체 리스트

---

# 9. 모듈 분리

Meteor 클래스를

```text
meteor.py
```

로 분리하였다.

메인 프로그램에서는

```python
from meteor import Meteor
```

를 사용한다.

학습 내용

- 모듈
- import
- 코드 분리

---

# 10. 설정 파일 분리

공통 설정을

```text
cfg.py
```

로 분리하였다.

```python
screen_width = 800
screen_height = 600
```

사용 예

```python
cfg.screen_width
```

학습 내용

- 설정 파일
- 상수 관리

---

# 11. Fighter 클래스 만들기

새로운 객체

```python
class Fighter
```

를 추가하였다.

초기 위치

```python
self.x = screen_width // 2
self.y = screen_height // 2
```

즉 화면 중앙이다.

---

# 12. 이벤트를 객체에게 전달하기

기존 방식

```python
if event.key ...
```

를 게임 루프에서 직접 처리

개선 후

```python
fighter.handle_event(event)
```

사용

장점

- Fighter가 자기 입력을 스스로 처리
- 코드가 깔끔해짐

학습 내용

- 캡슐화
- 객체 책임 분리

---

# 13. 속도(speed) 개념 추가

Fighter는

```python
self.speed = 3
```

을 가진다.

실제 이동은

```python
self.x += self.dx * self.speed
```

으로 계산한다.

장점

- 방향과 속도를 분리 가능

---

# 14. VSYNC 사용

창 생성 시

```python
pygame.display.set_mode(
    ...,
    vsync=1
)
```

사용

효과

- 모니터 주기에 맞춰 화면 갱신
- CPU 사용량 감소
- 화면 찢어짐 감소

---

# 15. 충돌 판정

## 원형 충돌

현재 실제 사용 중인 방법

```python
dist_sq =
    (dx * dx) +
    (dy * dy)
```

```python
if dist_sq < radius_sum ** 2:
```

특징

- sqrt 사용 안 함
- 더 빠름

학생들에게는

```python
distance < radius
```

버전을 먼저 설명하고

이후 최적화 버전으로 발전시킬 수 있다.

---

# 16. AABB 충돌

추가로 구현

```python
check_collision_aabb()
```

```python
abs(self.x - meteor.x)
```

방식을 사용한다.

특징

- 사각형 충돌
- 계산이 간단

---

# 17. 충돌 효과

충돌이 발생하면

```python
self.collision_count = 10
```

을 설정한다.

매 프레임

```python
self.collision_count -= 1
```

한다.

충돌 중에는

```python
pygame.draw.circle(
    ...
)
```

로 빨간 원을 그린다.

결과

- 충돌 후 약 10프레임 동안 표시
- 충돌 여부를 눈으로 확인 가능

학습 내용

- 프레임 기반 타이머
- 시각적 피드백

---

# 이번 수업에서 배운 개념

## Python

- 클래스
- 생성자
- 클래스 변수
- 객체 변수
- 리스트 컴프리헨션
- 모듈
- import

## Pygame

- 게임 루프
- 이미지 로드
- 화면 갱신
- 이벤트 처리
- VSYNC

## 게임 프로그래밍

- 이동
- 속도
- 반사
- 충돌 판정
- 원형 충돌
- 사각형 충돌
- 충돌 효과
- 프레임 기반 타이머

## 객체지향 프로그래밍

- 객체 생성
- 책임 분리
- 캡슐화
- 모듈화