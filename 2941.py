sentence = input()
total = len(sentence)   #��ü ���� ���� ���
remainder = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for letter in remainder:
    cnt += sentence.count(letter)
    
if 'dz=' not in sentence:
    total = total - cnt
else:
    dzcnt = sentence.count('dz=')
    cnt = cnt + dzcnt
    total = total - cnt
print(total)