#�ܾ� �Է¹ް� �빮�ڷ� ����
word = input().upper()
#�ߺ��� ������ ����Ʈ ����
w_list = [i for i in word]
l_list = list(set(w_list))
#�ܾ ������ ������ n_list ����
n_list = [] #n_list�� l_list�� ��ü ���� ��ġ Ȯ���ؾ���
for letter in l_list:
    n_list.append(w_list.count(letter))

max_idx = n_list.index(max(n_list))
if n_list.count(max(n_list)) == 1:
    print(l_list[max_idx])
else: print('?')

