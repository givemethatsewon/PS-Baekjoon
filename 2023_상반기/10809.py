#���ĺ� ����Ʈ
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#�ܾ� �Է�
s = input()
#�ܾ �ִ��� �ϳ��� Ȯ��
for alphabet in alphabet_list:
    idx = s.find(alphabet)
    print(idx, end=' ')