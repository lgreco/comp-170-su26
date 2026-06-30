
def find(target_character, in_this_string):
    position_of_target = -1  # Assume that target is not present
    start_from = 0  # First character of input string
    stop_at = len(in_this_string)  # Length of input string
    current_position = start_from
:q!:q    while current_position < stop_at and position_of_target == -1:
        # sequence of steps to execute
     ::   current_char = in_this_string[current_position]
        if current_char == target_character:
            position_of_target = current_position
        current_position = current_position + 1
    # When the loop ends:
    return position_of_target

