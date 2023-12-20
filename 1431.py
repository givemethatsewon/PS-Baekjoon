import sys
input = sys.stdin.readline

processed = []
#�ø��� ��ȣ �Է� �� ��ó��
n = int(input())
for _ in range(n):
    #�ø����ȣ ��ü
    serial = input().rstrip()
    #����
    length = len(serial)
    #���ڵ��� ��
    total = 0
    for i in serial:
        try:
            total += int(i)
        except ValueError:
            pass
    #��ó�� ����Ʈ�� ����Ʈ ���·� �߰�
    processed.append([length, total, serial])

processed.sort(key = lambda x : (x[0], x[1], x[2]))

for serial in processed:
    print(serial[2])