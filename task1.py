def pythagor(limit):
    triplets = []
    count = 0
    for z in range(1, limit + 1):
        for y in range(1, z):
            for x in range(1, y):
                if x ** 2 + y ** 2 == z ** 2:
                    triplets.append((x, y, z))
                    count += 1
    return triplets, count

limit = 200
triplets, count = pythagor(limit)
print("Количество пифагоровых троек:", count)
for triplet in triplets:
    print(triplet)
