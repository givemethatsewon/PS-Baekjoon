n, m = map(int, input().split())

num_list = list(range(1,n+1))   #[1,2,3,...,n]
for turn in range(m):    #m�� ��ü
    i,j = map(int, input().split())
    i -= 1
    j -= 1
    i_data = num_list[i]    #i�� ��� Ȯ��
    j_data = num_list[j]    #j�� ��� Ȯ��
    del num_list[i] #i��° ��� ����
    num_list.insert(i,j_data)   #i��°�� j_data ����
    del num_list[j] #j��° ��� ����
    num_list.insert(j,i_data)   #j��°�� i_data ����
print(*num_list, sep=' ')