import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    
else:
    #���̵� �����ϱ�
    opinion = [int(input()) for _ in range(n)]
    #�����ϱ�
    length = len(opinion)
    opinion.sort()  #����
    cut = int(length*0.15 + 0.5)
    cutted = opinion[cut:length-cut]
    #��� ���ϱ�
    mean = int((sum(cutted) / len(cutted)) + 0.5)
    print(mean)