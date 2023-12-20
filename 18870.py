import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#�ߺ� �����ϰ� ������������ ����Ʈ ����
sorted_nums = sorted(list(set(nums)))

#�˻��� �� �ð����⵵�� ���̱� ���� ��ųʸ��� ����
dic_nums = dict()
for idx,num in enumerate(sorted_nums):
    dic_nums[num] = idx

for num in nums:
    print(dic_nums[num], end=' ')
