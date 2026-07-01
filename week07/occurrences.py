
def occurrences(character, string):

    count = -1

    if string is not None and character is not None:
      # Input legit, set counter to 0
      count = 0
      for position in range(len(string)):
          if character == string[position]:
              count = count + 1

    return count
