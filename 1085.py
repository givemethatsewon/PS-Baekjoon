#�Է�
x, y, w, h = map(int, input().split())
#�˰���
length = [w-x, h-y, x, y]
print(min(length))
