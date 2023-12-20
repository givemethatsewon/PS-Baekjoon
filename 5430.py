from collections import deque
import sys
input = sys.stdin.readline

t = int(input())    #�׽�Ʈ ���̽�
for _ in range(t):
    r_cnt = 0
    methods = input().rstrip()  #�Լ���(���ڿ� �ε������� ������ ����)
    n = int(input())    #�迭�� ����ִ� ���� ����
    #�迭
    num_str = input().rstrip()[1:-1]
    if ',' in num_str:
        x = num_str.split(',')
        nums = deque(x)
    elif not num_str:
        nums = deque()
    else:
        nums = deque([num_str])
    
    #�Լ� �����Ű��
    for method in methods:
        if method == 'R':
            r_cnt += 1
        
        elif method == 'D' and r_cnt % 2 == 0:
            if not nums:
                print('error')
                break
            else:
                nums.popleft()
        
        elif method == 'D' and r_cnt % 2 == 1:
            if not nums:
                print('error')
                break
            else:
                nums.pop()

                
    else:
        if r_cnt % 2 == 1:
            nums.reverse()
        k = ','.join(list(nums))
        print('[' + k + ']') 