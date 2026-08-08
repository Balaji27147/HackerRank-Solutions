a= int(input())
c = set(map(int, input().split()))

b = int(input())
d = set(map(int, input().split()))

result = c.symmetric_difference(d)

for value in sorted(result):
    print(value)