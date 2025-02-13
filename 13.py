indxs = [int(i)-1 for i in input().split()]
words = input().split()
print(words[indxs[0]].capitalize(), *(words[i].lower() for i in indxs[1:]))