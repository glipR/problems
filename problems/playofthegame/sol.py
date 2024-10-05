def z_array(s):
    z = [len(s)-1]*len(s)
    L = 0
    R = 0
    for i in range(1, len(s)):
        j = max(min(z[i-L], R-i), 0)
        while i+j<len(s) and s[i+j] == s[j]:
            j += 1
        z[i] = j
        if (i + z[i] > R):
            R  = i + z[i]
            L = i
    return z

n_players, max_length = list(map(int, input().split()))
player_strings = []
for x in range(n_players):
    player_strings.append(input())
begin_state, potg_string = input().split()

def keymap_char(cur_state):
    return chr(ord('a') + 1 * cur_state[0] + 2 * cur_state[1] + 4 * cur_state[2] + 8 * cur_state[3])

# First, translate each tick into compute state
mapping = {
    "w": 0,
    "a": 1,
    "s": 2,
    "d": 3,
}
player_states = []
for string in player_strings:
    cur_state = [False for key in mapping]
    player_states.append([keymap_char(cur_state)])
    for char in string:
        if char == "|":
            player_states[-1].append(keymap_char(cur_state))
        else:
            cur_state[mapping[char]] = not cur_state[mapping[char]]
    player_states[-1].append(keymap_char(cur_state))

cur_state = [key in begin_state for key in mapping]
potg_states = [keymap_char(cur_state)]
for char in potg_string:
    if char == "|":
        potg_states.append(keymap_char(cur_state))
    else:
        cur_state[mapping[char]] = not cur_state[mapping[char]]
potg_states.append(keymap_char(cur_state))

z_str = "".join(potg_states) + "!" + "$".join("".join(s) for s in player_states)
# print(z_str)
z_arr = z_array(z_str)
# print(z_arr)
# Find the maximum index after len(potg_states)
best_player = None
best_index = None
best_value = None
cur_index = len(potg_states) + 1
for player in range(n_players):
    for state in range(len(player_states[player])):
        if z_arr[cur_index] > 0 and (best_value is None or best_value < z_arr[cur_index]):
            best_value = z_arr[cur_index]
            best_player = player
            best_index = state
        cur_index += 1
    cur_index += 1

if best_value is None:
    print("No Play of the Game")
else:
    print(f"Player #{best_player+1} matched {best_value-1} frames starting at frame #{best_index+1}.")