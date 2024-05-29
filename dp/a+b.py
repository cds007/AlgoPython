while True:
    try:
        line = input()
        line = line.split(' ')
        a, b = int(line[0]), int(line[1])
        print(a+b)
    except EOFError:
        break
# 这段代码会一直输出
