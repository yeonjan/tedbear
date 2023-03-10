M, N = map(int, input().split())
stores = []
for _ in range(int(input()) + 1):
    dir, dis = map(int, input().split())
    conv_pos = -1
    # 북쪽
    if dir == 1:
        conv_pos = M - dis
    # 남쪽
    if dir == 2:
        conv_pos = N + M + dis
    # 서쪽
    if dir == 3:
        conv_pos = M + dis
    # 동쪽
    if dir == 4:
        conv_pos = N + M + M + N - dis

    stores.append(conv_pos)

my_pos = stores.pop()
answer = 0
for store_pos in stores:
    dis1 = abs(my_pos - store_pos)
    dis2 = N * 2 + M * 2 - dis1
    answer += min(dis1, dis2)
print(answer)
