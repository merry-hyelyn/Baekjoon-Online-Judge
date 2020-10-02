n = int(input())

rings = list(map(int, input().split()))

first = rings.pop(0)

for ring in rings:
    if first % ring == 0:
        print(f"{int(first/ring)}/1")

    else:
        r = first % ring
