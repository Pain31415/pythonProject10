def draw_line(length, direction, symbol):
    if direction == 'horizontal':
        horizontal_line = symbol * length
        print(horizontal_line)
    elif direction == 'direction':
        for _ in range(length):
            print(symbol)
draw_line(25, 'horizontal', '-')
draw_line(10, 'direction', '|')
