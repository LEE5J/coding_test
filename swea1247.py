import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for case in range(1,T+1):
    num_p = int(input())+2
    points = []
    x = int(input())
    y = int(input())
    start = (x,y)
    x = int(input())
    y = int(input())
    end = (x,y)
    for i in range(num_p):
        x = int(input())
        y = int(input())
        points.append((x,y))
    # 입력 완료
    min_distance = 200*10
