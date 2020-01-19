from math import factorial

t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    print(factorial(M)//(factorial(M-N)*factorial(N)))
 