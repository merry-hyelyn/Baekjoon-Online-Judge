# 문제
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.

# 출력
# 첫째 줄에 0의 개수를 출력한다.


def count_num(n, div):
    count = 0
    while n >= div:
        n = n // div
        count += n
    return count


n, m = map(int, input().split())

count_five = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)
count_two = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)

print(min(count_five, count_two))
