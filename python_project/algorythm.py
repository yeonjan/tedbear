from collections import deque

N = int(input())
arr = [(idx + 1, move) for idx, move in enumerate(map(int, input().split()))]
queue = deque(arr)
answer = []

while queue:
    idx, move = queue.popleft()
    answer.append(idx)
    if move > 0:
        move -= 1
    while move and queue:
        if move > 0:
            queue.append(queue.popleft())
            move -= 1
        else:
            queue.appendleft(queue.pop())
            move += 1

print(*answer)
