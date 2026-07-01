
def occurrences(character, string):
    """Count the number of occurrences of character in string."""
    # Initialize count to -1 to indicate an error if inputs are invalid
    count = -1
    # Check if both inputs are valid (not None)
    if string is not None and character is not None:
      # Input legit, set counter to 0
      count = 0
      # Loop through each position in the string to check 
      # for occurrences of the character
      for position in range(len(string)):
          # Check if the character at the current position matches 
          # the target character
          if character == string[position]:
              # If it does, increment the count of occurrences
              count = count + 1
    # Return the count of occurrences, which will be -1 if inputs were invalid
    return count
