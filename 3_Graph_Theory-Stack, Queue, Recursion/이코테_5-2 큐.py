# 큐를 구현하기 위해 deque 라이브러리 사용
from collections import deque

# deque 객체를 이용하여 큐를 구현한다.
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)