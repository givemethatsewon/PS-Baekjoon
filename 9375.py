import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        cloth = input().split()[1]  #�� ����
        if cloth in clothes:
            clothes[cloth] += 1
        else:
            clothes[cloth] = 1
        
    net = 1
    for cloth in clothes:
        net *= (clothes[cloth] + 1) #VALUE�� �̾ƿͼ� ����Ʈ ����� �ͺ��� �̰� ��ųʸ����� �ٷ� �����ϴ°� �޸� ���鿡�� �̵�
    print(net - 1) #�˸��� ��� ����
