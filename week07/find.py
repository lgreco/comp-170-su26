def find(target_character, in_string):
    """Find the position of the first occurrence of target_character
    in in_string."""
    # position_of_target is -1 if target_character is not found
    position_of_target = -1
    # current_position is the index of the character currently being checked
    current_position = 0
    # Loop through the string until either the target_character is found
    # or the end of the string is reached
    while current_position < len(in_string) and position_of_target == -1:
        # Check if the character at current_position is the target_character
        current_char = in_string[current_position]
        if current_char == target_character:
            # If it is, set position_of_target to current_position
            position_of_target = current_position
        # Regardless of whether the character was found, increment
        # current_position to check the next character in the next iteration
        current_position = current_position + 1
    # When the loop ends, return position_of_target, which will be -1 
    # if the target_character was not found
    return position_of_target
