n = int(input())
c = input()
s = 0
for i in range(len(c) - 1):
    if c[i] == c[i + 1]:
        s += 1
print(s)
