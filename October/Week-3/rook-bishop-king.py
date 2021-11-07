def castle_reach(castle_pos, final_pos):
    if castle_pos[0] == final_pos[0] or castle_pos[1] == final_pos[1]:
        return 1
    else:
        return 2


def can_king_reach(king_pos, final_pos):
    # go diagonal as much as possible then go horizontal or vertical count number of moves
    diag_moves = min(abs(king_pos[0] - final_pos[0]),
                     abs(king_pos[1] - final_pos[1]))
    # print(diag_moves)
    if king_pos[0] < final_pos[0]:
        king_pos[0] += diag_moves
    elif king_pos[0] > final_pos[0]:
        king_pos[0] -= diag_moves

    if king_pos[1] < final_pos[1]:
        king_pos[1] += diag_moves
    elif king_pos[1] > final_pos[1]:
        king_pos[1] -= diag_moves

    horiz_moves = abs(king_pos[0] - final_pos[0])
    vertical_moves = abs(king_pos[1] - final_pos[1])

    return horiz_moves + vertical_moves + diag_moves


def can_bishop_reach(bishop_pos, final_pos):
    odd = True if (bishop_pos[0] + bishop_pos[1]) % 2 == 1 else False
    if ((final_pos[0] + final_pos[1]) % 2 == 1) == odd:
        if abs(bishop_pos[0] - final_pos[0]) == abs(bishop_pos[1] - final_pos[1]):
            return 1
        return 2
    return 0


input_ = [int(i) for i in input().split()]

rook = castle_reach([input_[0], input_[1]], [input_[2], input_[3]])
bishop = can_bishop_reach([input_[0], input_[1]], [input_[2], input_[3]])
king = can_king_reach([input_[0], input_[1]], [input_[2], input_[3]])

print(f"{rook} {bishop} {king}")
