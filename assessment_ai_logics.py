# 1.Question

n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))

intervals.sort()

merged = []

current_start, current_end = intervals[0]

for start, end in intervals[1:]:
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start = start
        current_end = end

merged.append((current_start, current_end))

for start, end in merged:
    print(start, end)


# 2.Question

n = int(input())
a = list(map(int, input().split()))
k = int(input())

ans = 0
pos = 1

for i in range(n):
    high = a[i]
    low = a[i]

    for j in range(i, n):
        if a[j] > high:
            high = a[j]

        if a[j] < low:
            low = a[j]

        if high - low <= k:
            size = j - i + 1

            if size > ans:
                ans = size
                pos = i + 1
        else:
            break

print(ans, pos)
