# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

n = int(input())
num = list(map(int, input().split()))
s = []
for k in num:
    count = 0
    for j in range(1, k + 1):
        if k % j == 0:
            count += 1
    if count == 2:
        s.append(k)

print(len(s))
