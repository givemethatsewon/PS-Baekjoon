#�Է�
a,b,v = map(int, input().split())
#�˰���
x = (v-a) % (a-b)
if x > 0:
    result = (v-a) // (a-b) + 2
else:
    result = (v-a) // (a-b) + 1
#���
print(result)