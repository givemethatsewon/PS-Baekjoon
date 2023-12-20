import sys
input = sys.stdin.readline

n = int(input())
pairs = [list(map(int, input().split())) for i in range(n)]

#sort �޼����� key �Ű������� �����Լ��� �̿��� 2���� �迭 ����
#key: �Լ��� ����� ���� ������ �� �� �ִ�
#lambda: �Լ��� �Ű������� ǥ���ĸ� �Ἥ �����ϰ� �� �� �ִ�
pairs.sort(key=lambda x : (x[0],x[1]))

for pair in pairs:
    print(*pair, sep=' ')
