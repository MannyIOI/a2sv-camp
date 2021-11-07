def kingEscape(q_loc, b_loc, c_loc):
    qx, qy = q_loc
    bx, by = b_loc
    cx, cy = c_loc
    x_true, y_true = False, False
    if (bx < qx and cx < qx) or (bx > qx and cx > qx):
        x_true = True
    if (by < qy and cy < qy) or (by > qy and cy > qy):
        y_true = True

    return x_true and y_true

board_size = int(input())
queen_loc = [int(i) for i in input().split()]
b_loc = [int(i) for i in input().split()]
c_loc = [int(i) for i in input().split()]

canEscape = kingEscape(queen_loc, b_loc, c_loc)
if canEscape:
    print('YES')
else:
    print('NO')