f = open('day1input.txt', 'r')
# f = open('day1sample.txt', 'r')
lines = f.read().strip()

instr = lines.split(', ')

dir = 0 # 0 is North, 1 is East, -1 West South always 2 -2


# Part 1
# def move(dir, steps, x, y):
#     if dir % 4 == 0: # north
#         for i in range(steps):
#             y += 1
#     elif dir % 4 == 1: # east
#         for i in range(steps):
#             x += 1
#     elif dir % 4 == 3: # west
#         for i in range(steps):
#             x -= 1
#     elif dir % 4 == 2: # south
#         for i in range(steps):
#             y -= 1
#     return x, y

# x, y = 0, 0
# for dirstep in instr:
#     if dirstep[0] == 'L':
#         dir -= 1
#     elif dirstep[0] == 'R':
#         dir += 1
#     x, y = move(dir, int(dirstep[1:]), x, y)

# print(abs(x) + abs(y))

# Part 2
visited = [(0, 0)]
def move(dir, steps, x, y, visited):
    if dir % 4 == 0: # north
        for i in range(steps):
            y += 1
            if (x, y) in visited:
                print(x, y)
                return x, y
            else:
                visited.append((x, y))
    elif dir % 4 == 1: # east
        for i in range(steps):
            x += 1
            if (x, y) in visited:
                print(x, y)
                return x, y
            else:
                visited.append((x, y))
    elif dir % 4 == 3: # west
        for i in range(steps):
            x -= 1
            if (x, y) in visited:
                print(x, y)
                return x, y
            else:
                visited.append((x, y))
    elif dir % 4 == 2: # south
        for i in range(steps):
            y -= 1
            if (x, y) in visited:
                print(x, y)
                return x, y
            else:
                visited.append((x, y))
    return x, y

x, y = 0, 0
for dirstep in instr:
    if dirstep[0] == 'L':
        dir -= 1
    elif dirstep[0] == 'R':
        dir += 1
    x, y = move(dir, int(dirstep[1:]), x, y, visited)

print(x, y) # first output is solution