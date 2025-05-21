import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    x, y, z = map(int, input().split())
    tmp = 1
    base = x
    cut_off = 1000*z
    max_hit = False
    while y > 0:
        if y & 1:
            tmp = base*tmp
            if tmp > cut_off:
                max_hit = True
                tmp = tmp%cut_off
        y >>= 1
        if max_hit:
            base = (base*base)%cut_off
        else:
            base = (base*base)
    if max_hit:
        tmp += cut_off
    res = float(tmp / z)
    round_res = round(res, 3)
    if round_res > res:
        round_res -= 0.001
    str_res = f'{round_res:.3f}'
    print(str_res[-7:])