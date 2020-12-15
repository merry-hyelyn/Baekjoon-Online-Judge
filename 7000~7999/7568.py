from operator import itemgetter

n = int(input())
grade = 1
result = {}
weight_height = [list(map(int, input().split())) for _ in range(n)]
sort_wh_list = sorted(weight_height, key=itemgetter(0, 1), reverse=True)
for i in range(n):
    index = weight_height.index(sort_wh_list[i])
    if i == 0:
        result[index] = grade
    else:
        prev_w, prev_h = sort_wh_list[i-1]
        w, h = sort_wh_list[i]
        if prev_h > h:
            grade = i + 1
        result[index] = grade

for i, wh in enumerate(weight_height):
    print(result[i], end='')
    if i != n-1:
        print(' ', end='')
