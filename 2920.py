#����Ʈ ���·� �Է� ����
user = list(map(int, input().split()))
#���� ����
n_list = [i for i in range(1,9)]
r_list = n_list[::-1]
#���
if user == n_list: print('ascending')
elif user == r_list: print('descending')
else: print('mixed')

