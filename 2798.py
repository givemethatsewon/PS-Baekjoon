from itertools import combinations
import sys
#�Է�
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
#�˰���
combi_list = list(combinations(cards,3))    #���� ��� ����
total_list = list(map(sum, combi_list))     #������ �� ��� ����
differ_list = []    #������ �հ� m���� ���� ������ ����

#0���� ū ��쿡�� idx ���缭 total ���
for total in total_list:
    differ = m - total
    if differ < 0: differ_list.append(m)
    else: differ_list.append(m-total)

idx = differ_list.index(min(differ_list))
print(total_list[idx])
        
