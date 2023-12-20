import sys
input = sys.stdin.readline

n, target = map(int, input().split())
trees = list(map(int, input().split()))

#�̺�Ž������ ������ cutter���� ã��
start = 0
end = max(trees)
ans = 0

while start <= end:
    cutter = (start + end) // 2
    total = 0   #�߸� �������� �� ����
    
    for tree in trees:
        if tree > cutter:
            total += (tree - cutter)
    
    if total < target:
        end = cutter - 1
    else:
        ans = cutter
        start = cutter + 1

#�� ���
print(ans)