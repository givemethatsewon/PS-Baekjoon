import sys
input = sys.stdin.readline

k, n = map(int, input().split())    #�̹� ������ �ִ� k���� ����, �ʿ��� n���� ����
k_list = [int(input()) for _ in range(k)]   #������ �ִ� ���� ����Ʈ

#���� Ž���� ���� �������� ���� ����
start = 1
end = max(k_list)

while start <= end:
    mid = (start + end) // 2
    
    total = 0   #�߸� ������ ���� ��
    for k in k_list:
        total += (k // mid)
    
    if total < n: #�߸� ������ ���� ���� n������ ������
        end = mid - 1
    else:   #�߸� ������ ���� ���� n������ ũ�ų� ������
        ans = mid
        start = mid + 1 

print(ans)