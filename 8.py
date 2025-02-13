s = input()
if len(s) % 2 == 0:
    n = len(s) // 2
    for i in range(n):
        print(' ' * (n - i - 1) + s[n - i - 1] + ' ' * i +
              ' ' * i + s[n + i])
else:
    d = (len(s) + 1) // 2
    print(' ' * ((len(s) - 1) // 2) + s[d - 1] + ' ' * ((len(s) - 1) // 2))
    for i in range(1, d):
        print(' ' * (d - i - 1) + s[d - i - 1] + ' ' * i +
              ' ' * (i - 1) + s[d + i - 1])
