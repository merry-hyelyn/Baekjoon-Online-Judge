from operator import itemgetter

n = int(input())
weight_height = [list(map(int, input().split())) for _ in range(n)]

weight_height.sort(key=itemgetter(0, 1), reverse=True)
grade = 1
result = {}

for i in range(n):
    if i == 0:
        result[weight_height[i]] = 1
    else:
        prev_w, prev_h = weight_height[i-1]
        w, h = weight_height[i]
