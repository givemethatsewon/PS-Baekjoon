import sys
input = sys.stdin.readline

counts = [0 for i in range(1000001)]
#�ε��� = ���� ��
#�� = �ε����� �ش��ϴ� ������ ����

n = int(input())    #������ ũ��
nums = list(map(int, input().split()))
#���� ���� counts�� �Է�
for num in nums:
    counts[num] += 1

x = int(input()) #a + b = x�� �����ϴ� �������� ����

result = 0
for num in nums:
    if x - num <= 1000000:
        result += (counts[num] * counts[x - num])

print(result//2) 
    
