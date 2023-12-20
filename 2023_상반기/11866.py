from collections import deque

n, k = map(int, input().split())
array = deque([i for i in range(1, n+1)])
answer = deque()

#ť�� ȸ����Ű�鼭 answer�� k��° ���� �ֱ�
while array:
    array.rotate(-k+1)
    x = array.popleft()
    answer.append(x)

#������Ŀ� �°� ���
a = ', '.join(map(str, answer))
print(f'<{a}>')
