#�Է�
target = int(input())
n = 0
#������ ���ϴ� �˰���
while True:
    n += 1
    sum = 0
    for digit in str(n):
        sum += int(digit)
    sum = sum + n
    if sum == target:
        print(n)
        break
    elif n >= target:
        print(0)
        break