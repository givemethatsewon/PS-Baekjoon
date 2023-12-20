import sys

n = int(sys.stdin.readline())
stack = []
result = []
count = 1

for _ in range(n):
    data = int(sys.stdin.readline())    #������ �Է�
    while count <= data:    #�����ϴ� ���ڰ� �Էµ� ���ں��� ���ų� ������
        stack.append(count) #���ÿ� �߰�
        count += 1  #���� 1���� ��Ŵ
        result.append('+')  #���� ���
        #���ڰ� �����ϸ鼭 �Էµ� ���ں��� Ŀ��  -> while�� Ż��
    if stack[-1] == data:   #������ last in�� �Էµ� ���ڿ� ������
        stack.pop() #���ÿ��� first out
        result.append('-')  #���� ���
    else:   #last in�� �Էµ� ���ڿ� ���� ������
        print('NO')
        exit(0)#�ڵ� ��������

print(*result, sep='\n')