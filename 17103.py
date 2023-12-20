import sys
input = sys.stdin.readline

#�����佺�׳׽��� ü�� �̿��Ͽ� n������ ��� �Ҽ� ���ϱ�
prime = [True for i in range(1000001)]
prime[0] = prime[1] = False
for i in range(2,int(1000001**0.5)+1):
    if prime[i]:
        for j in range(i*i, 1000001, i):
            prime[j] = False

t = int(input())
for _ in range(t):
    N = int(input())
    cnt = 0
    for i in range(2,N//2+1):
        if prime[i] and prime[N-i]:
            cnt += 1

    #��� ���
    print(cnt)