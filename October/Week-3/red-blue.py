def more_probability(red, blue):
    red_win = 0
    blue_win = 0
    for i in red:
        for j in blue:
            if int(i) > int(j):
                red_win += 1
            elif int(i) < int(j):
                blue_win += 1
    
    if red_win > blue_win:
        print('RED')
    elif blue_win > red_win:
        print('BLUE')
    else:
        print('EQUAL')


test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    red = list(input())
    blue = list(input())

    more_probability(red, blue)
    