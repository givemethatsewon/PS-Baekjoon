import sys
input = sys.stdin.readline

n, c = map(int, (input().split()))
x_list = [int(input()) for _ in range(n)]
x_list.sort()

start = 1
end = x_list[-1] - x_list[0]
while start <= end:
    mid = (start + end) // 2
    s_point = x_list[0] #starting point
    routers = c - 1 #ù��° ������ s_point�� ��ġ�����Ƿ�
    for x in x_list:
        if x - s_point >= mid:
            s_point = x
            routers -= 1
        
        if routers == 0: break  #������ �� ������ �� ���ƺ� �ʿ� �����Ƿ� Ż��
    
    if routers > 0:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)
