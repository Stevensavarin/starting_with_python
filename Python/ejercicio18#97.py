tuple1 = (1, 2, 3, 4, 5)
tuple2 = (8, 6, 4, 2, 0)

add_tuples = []
for x, y in zip(tuple1, tuple2):
    add_tuples.append(x + y)

print("Tupla 1:".ljust(13), tuple1)
print("".ljust(14) + "+")
print("Tupla 2:".ljust(13), tuple2)
print("".ljust(14) + "===============")
print("Suma:".ljust(13), tuple(add_tuples))
