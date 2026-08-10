data = {1: 5, 2: 6, 3: 5, 4: 5, 5: 6, 6: 7, 7: 1, 9: 6}
cycles = []
key = [k for k in data.keys()]
values = [v for v in data.values()]
for k in key:
    if k in values:
        cycles.append(k)
print(key, values)
print(cycles)