n,m = map(int, input().split())
#n���� �ٱ��� �����
box = [i for i in range(1,n+1)]
def do(x):
    return int(x)-1
#m�� ����
for turn in range(m):
    b,e,m = map(do, input().split())
    box = box[:b] + box[m:e+1] + box[b:m] + box[e+1:]
print(*box, sep=' ')
    