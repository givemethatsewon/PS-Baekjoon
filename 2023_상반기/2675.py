t = int(input())    #�׽�Ʈ ���̽� ����

r_list = []
s_list = []
for i in range(t):
    r,s = input().split()   #�ݺ�Ƚ��, �ݺ��� ����
    s = [s[i] for i in range(len(s))]   #���ڿ� �и�
    r_list.append(r)
    s_list.append(s)

for i in range(len(s_list)):
    for j in range(len(s_list[i])):
        print(s_list[i][j]*int(r_list[i]),end='')
    print()
