n = int(input())
start = 1
cnt = 0

#n���� ���� �������� ���� ���ϱ�
while start**2 <= n:
    cnt += 1
    start += 1

print(cnt)
