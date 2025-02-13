count = int(input("Количество событий: "))
queue = []  # очередь
for i in range(count):
    event = input()
    if "Кто последний?" in event:
        queue.append(event[19:len(event) - 1])
    if "Я только спросить!" in event:
        queue.insert(0, event[23:len(event) - 1])
    if "Следующий!" in event:
        if queue:
            print("Заходит " + queue.pop(0) + "!")
        else:
            print("В очереди никого нет.")
