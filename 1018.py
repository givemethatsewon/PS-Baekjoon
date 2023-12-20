import sys
input = sys.stdin.readline

n,m = map(int, input().split())
original = []
count = []

for _ in range(n):
    original.append(input().rstrip())

for a in range(n-7):
    for b in range(m-7):    #a,b == ������
        draw1 = 0 #ù ��° Ÿ�� ����� ���
        draw2 = 0 #ù ��° Ÿ�� �������� ���
        
        for i in range(a,a+8):
            for j in range(b,b+8):  #�������� �������� 8X8 ü���� Ž��
                if (i+j) % 2 == 0:  #Ȧ����° ����
                    if original[i][j] == 'W': 
                        draw1 += 1
                    if original[i][j] == 'B':
                        draw2 += 1
                else:   #¦����° ����
                    if original[i][j] == 'B': #W�� ���������� �� ���� Ÿ�� B���� ��
                        draw1 += 1
                    if original[i][j] == 'W': #B�� ���������� �� ���� Ÿ�� W���� ��
                        draw2 += 1
#�� ���� draw������ ���� ü������ ��Ģ�� ��� ������ �ǹ�
        count.append(min(draw1,draw2))  #�� ���� draw���� -> �ּ� ���� Ƚ�� �̹Ƿ� min ���
print(min(count)) #�������� 8X8 �� �ּ��̹Ƿ� min ���
