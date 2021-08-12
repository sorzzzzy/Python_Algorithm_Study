'''
뱀

'Dummy' 라는 도스게임이 있다. 
이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
게임은 newxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
    1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''

from sys import stdin
from collections import deque

# 상, 우, 하, 좌
case = [[-1,0], [0,1], [1,0], [0,-1]]

N = int(stdin.readline())
dummy = [[0] * N for _ in range(N)]

for _ in range(int(stdin.readline())):
    r, c = map(int, stdin.readline().split())
    dummy[r-1][c-1] = 1

change = []
L = int(stdin.readline())
for _ in range(L):
    x, c = input().split()
    change.append([int(x), c])

q = deque()
q.append([0,0])
d = 1

#change 배열의 index
c = 0 
res = 0
newx, newy = 0, 0
while(1):
    res += 1
    newx += case[d][0]
    newy += case[d][1]
    
    if change[c][0] == res:
        if change[c][1] == 'D':
            d = ((d+1) % 4)
        else:
            d = ((d-1) % 4)
        if c != L-1:
            c += 1
   
    if 0 <= newx < N and 0 <= newy < N:
        for i in q:
            if [newx, newy] == i:
                print(res)
                exit()
        if dummy[newx][newy] == 1:
            dummy[newx][newy] = 0
            q.append([newx, newy])
        
        elif dummy[newx][newy] == 0:
            q.append([newx, newy])
            x, y = q.popleft()
    else:
        break
        
print(res)