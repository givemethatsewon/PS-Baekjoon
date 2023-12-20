import sys
input = sys.stdin.readline

def eratos(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    #��Ʈx������ x���� �Ҽ��� ���ɼ��� ������ ����Ͽ� ��������
    for i in range(2, int(x**0.5) + 1):
        if prime[i]:
            for j in range(i*i, x+1, i):
                prime[j] = False
    return [i for i in range(x+1) if prime[i]]

while True:
    n = int(input())
    if n == 0:
        break
    count =  len(eratos(2*n)) - len(eratos(n))
    print(count)