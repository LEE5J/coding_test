n, w, L = map(int,input().split())
trucks = list(map(int,input().split()))
max_time = w*n
elapsed_time = 0
load = 0
current_truck = 0
weight_and_pos = []
while elapsed_time < max_time+10:
    elapsed_time += 1
    for i in range(len(weight_and_pos)): # 위치 업데이트 과정
        weight_and_pos[i] = [weight_and_pos[i][0],weight_and_pos[i][1]+1]
    if len(weight_and_pos) != 0:
        if weight_and_pos[0][1] == w: 
            load -= weight_and_pos[0][0]
            weight_and_pos.pop(0)
            
    if current_truck<n: # 더 들어가야할 트럭이 있음
        if load + trucks[current_truck] <= L: # 트럭 추가
            load += trucks[current_truck]
            weight_and_pos.append([trucks[current_truck],0])
            current_truck += 1
    else:
        if len(weight_and_pos) == 0:
            break
print(elapsed_time)
    
    