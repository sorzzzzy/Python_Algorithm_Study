'''
슬라임 합치기

영선이와 효빈이는 슬라임을 합치는 게임을 하고 있다. 
두 사람은 두 슬라임을 골라서 하나로 합쳐야 한다. 게임은 슬라임이 하나 남았을 때 끝난다.
모든 슬라임은 양수 크기를 가지고 있다. 
두 슬라임 x와 y를 합쳤을 때, 합친 슬라임의 크기는 x+y가 된다. 
또한, 슬라임을 합칠 때 마다 두 사람은 x*y 점수를 얻게 된다.
영선이와 효빈이가 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''

from sys import stdin

N = int(stdin.readline())
slimes = list(map(int, stdin.readline().split()))
res = 0
score = 0
for slime in range(len(slimes)-1):
    # 점수값 저장(= x*y)
    score = slimes[slime] * slimes[slime+1]
    # 두개를 합쳤으므로 그 다음부턴 합친 슬라임의 크기로 바꿔주어야 함
    slimes[slime+1] = slimes[slime] + slimes[slime+1] 
    res += score
print(res)
