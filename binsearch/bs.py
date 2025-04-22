N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
large = arr[-1]

def cal(leng):
    result = 0
    for i in arr:
        if i>leng:
            result+=(i-leng)
    return result

s, e = 0, large
mid = (s+e)//2
while not(cal(mid)>=M and cal(mid-1)<M):
    if cal(mid)<M:
        e = mid-1
    elif cal(mid)>M:
        s = mid+1
    else:
        break
    mid = (s+e)//2
print(mid)
