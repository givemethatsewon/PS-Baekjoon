n = int(input())

line = 0    #�� ��° ������
end = 0
while n > end:
    line += 1
    end += line

gap = end - n   #�ش� �ٿ��� index
if line % 2 == 0:
    up = line - gap
    down = 1 + gap
else:
    up = 1 + gap
    down = line - gap
    
print(f'{up}/{down}')
