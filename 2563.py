#��ȭ�� ����
paper = [[0]*100 for i in range(100)]

#�ش�Ǵ� �κ� ĥ�ϱ�
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] = 1

#��ü ���� ���ϱ�
dot_sum = 0
for row in paper:
    dot_sum += sum(row)
print(dot_sum)