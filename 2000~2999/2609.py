# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

def make_factor(num):
    n = int(num**0.5)
    result = []

    for i in range(2, n+1):
        if num % i == 0:
            result.extend((i, int(num/i)))

    return result


a, b = map(int, input().split())

factor_a = set(make_factor(a))
factor_b = set(make_factor(b))

factor = factor_a.intersection(factor_b)

multiple_a = set([a*i for i in range(2, max(factor))])
multiple_b = set([b*i for i in range(2, max(factor))])

multiple = multiple_a.intersection(multiple_b)

print(max(factor))
print(min(multiple))
