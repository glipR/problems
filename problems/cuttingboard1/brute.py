def solve_known(square_list, player, dep=0) -> int:
    for idx, square in enumerate(square_list):
        if square[player] != 1:
            # We can play this one.
            for size in range(1, square[player]):
                # Try cutting into portions of size and square[player]-size.
                new_square_1 = square[:]
                new_square_1[player] = size
                new_square_2 = square[:]
                new_square_2[player] = square[player] - size
                new_squares = square_list[:idx] + square_list[idx+1:] + [new_square_1, new_square_2]
                print(f"Player {player+1} is cutting {square} into {new_square_1, new_square_2} [{dep}] New: {new_squares}.")
                res = solve_known(new_squares, 1-player, dep=dep+1)
                print(f"After player {player+1} cuts {square} into {new_square_1, new_square_2} [{dep}], the winner is player {res+1}.")
                if res == player:
                    # We win this universe. Force it
                    return player
    # We can't force a win.
    return 1 - player

n, m = list(map(int, input().split()))

p1 = solve_known([[n, m]], 0)
p2 = solve_known([[n, m]], 1)

if p1 == 0 and p2 == 0:
    print("Vaughn")
elif p1 == 1 and p2 == 1:
    print("Hazel")
elif p1 == 0 and p2 == 1:
    print("1st Player")
else:
    print("2nd Player")
