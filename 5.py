s = input().lower()
while True:
    s1 = input().lower()
    if s[-1] != s1[0]:
        print(s1)
        break
    s = s1
