def draw_square(side_length, symbol, filled):
    for i in range(side_length):
        for j in range(side_length):
            if filled:
                print(symbol * side_length)
            else:
                if i == 0 or i == side_length - 1:
                    print(symbol * side_length)
                else:
                    print(symbol + " " * (side_length - 2) + symbol)
draw_square(10, '#', True)
draw_square(6, '$', False)