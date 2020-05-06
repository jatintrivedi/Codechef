t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dis = []
    count = 0
    mini = 200000
    maxi = 0
    for i in range(len(arr)):
        if(i == 0):
            continue
        dis.append(arr[i] - arr[i-1])
        if(dis[i-1] < 3):
            count += 1
            continue
        if(count >= maxi):
                maxi = count + 1
        if(count < mini):
            mini = count + 1
        count = 0
    if(count>=maxi):
        maxi = count + 1
    if(count < mini):
        mini = count + 1
    print(mini,maxi)