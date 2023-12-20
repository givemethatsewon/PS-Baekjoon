import sys
input = sys.stdin.readline

n = int(input())
num_list = []
most_idxs = []
#[0,4000]�� -4000 ~ 0����
#[4001,8000]�� 1 ~ 4000����
count = [0]*8001
for _ in range(n):
    num = int(input())
    count[num + 4000] += 1

for i in range(8001):
    #���ĵ� ����Ʈ �����
    if count[i]:
        for _ in range(count[i]):
            num_list.append(i - 4000)    
    #�ֺ� ���ϱ� ���� ���� ����
    most = max(count)
    if count[i] == most:
        most_idxs.append(i - 4000)

#������
mean = round(sum(num_list)/n)
print(mean)
#�߾Ӱ�
center = num_list[n//2]
print(center)
#�ֺ�
if len(most_idxs) == 1:
    print(most_idxs[0])
else:
    print(most_idxs[1])
#����
extent = num_list[-1] - num_list[0]
print(extent)


