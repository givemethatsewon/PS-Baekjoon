n = int(input())
cnt = 0
num = 665

while cnt < n:
    if '666' in str(num):
        cnt += 1
        num += 1
    else:
        num += 1

print(num - 1)
