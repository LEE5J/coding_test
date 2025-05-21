a = int(input())
cnt = 0
Q_loc = list()


# 현재줄에서 가능한 위치들을 체크
# 리턴으로 좌표 리스트를 쏴줌
def check():
    global a
    global Q_loc
    possible_path = list()
    if len(Q_loc) == 0:
        for i in range(a):
            possible_path.append([0, i])
    else:
        full_path = [[0 for col in range(a)] for row in range(a)]
        for loc in Q_loc:
            for j in range(len(Q_loc) - 1, a):
                full_path[j][loc[1]] = 1
            for j in range(1, a):
                if -1 < loc[0] + j and loc[0] + j < a and -1 < loc[1] + j and loc[1] + j < a:
                    full_path[loc[0] + j][loc[1] + j] = 1
                if -1 < loc[0] + j and loc[0] + j < a and -1 < loc[1] - j and loc[1] - j < a:
                    full_path[loc[0] + j][loc[1] - j] = 1
        for i in range(a):
            if full_path[len(Q_loc)][i] == 0:
                possible_path.append([len(Q_loc), i])
        # print(full_path)
    return possible_path


# DFS 재귀로 Q_loc
def search(remain_Q):
    global cnt
    global Q_loc
    if remain_Q == 0:
        # print(cnt)
        cnt += 1
    else:
        possible_path = check()
        if len(possible_path) == 0:
            pass  # 딱히 처리할 것이 없음
        else:
            for loc in possible_path:
                Q_loc.append(loc)
                search(remain_Q - 1)
                Q_loc.pop()


search(a)
print(cnt)
