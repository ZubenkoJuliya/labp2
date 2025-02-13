s = input()
a = s[1::].replace('V', '!V!').split('!')
current_pos = 0 
for i in a:
    if i == '': 
        continue 
    elif i[0] == '<':
        current_pos -= len(i)
        print(current_pos * ' ' + s[0] + i.replace('<', s[0]))
    elif i[0] == '>':
        print(current_pos * ' ' + s[0] + i.replace('>', s[0]))
        current_pos += len(i)
    elif i[0] == 'V': 
        print(current_pos * ' ' + s[0])