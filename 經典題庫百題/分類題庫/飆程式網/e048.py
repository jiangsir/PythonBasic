a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]

for item in b:
    print(' '.join(str(item*i) for i in a))

