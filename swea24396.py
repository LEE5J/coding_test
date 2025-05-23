import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for i in range(T):
    B, W, X, Y, Z = map(int, input().split())
    if X + Y > 2*Z:
        print(B*X+W*Y)
    else:
        if B > W:
            print((B-W)*X+2*W*Z)
        else:
            print((W-B)*Y+2*B*Z)