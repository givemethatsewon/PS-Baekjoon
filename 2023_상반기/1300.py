n = int(input())
k = int(input())


start = 1
end = k
while start <= end:
    mid = (start + end) // 2    #mid == Ư�� ����
    
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n) 
    
    if cnt >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)