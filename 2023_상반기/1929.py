def seive(x):
    if x == 0:
        return []
    prime = [True] * (x+1)
    prime[0] = prime[1] = False
    #x���� ���� �� �߿��� x�� ����� ���� ��Ʈx���� �۰ų� ����.
    for i in range(2,int(x**0.5)+1):
        if prime[i]:    #i�� �Ҽ��̸�
            #i�� ������� ���� �Ҽ��� �ƴϹǷ� False�� �ٲ�����
            for j in range(i**2,x+1,i):
                prime[j] = False
    return [i for i in range(x+1) if prime[i]]

m,n = map(int, input().split())
m_set = set(seive(m-1))
n_set = set(seive(n))
result = list(n_set - m_set)
result.sort()
print(*result, sep='\n')