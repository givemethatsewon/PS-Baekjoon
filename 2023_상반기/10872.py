def factorial(n):
    if n == 0:  #base case
        result = 1
    else:   #factorial(n-1)Ÿ�� �ٽ� ���ƿ�
        result = n*factorial(n-1)
    return result

if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
