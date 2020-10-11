# 문제
# 자연수 과 정수 가 주어졌을 때 이항 계수 를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 과 가 주어진다. (1 ≤  ≤ 1,000, 0 ≤  ≤ )

# 출력
#  를 10,007로 나눈 나머지를 출력한다.

from math import factorial

n, k = map(int, input().split())

x = factorial(n) / (factorial(n-k) * factorial(k))

print(int(x % 10007))
