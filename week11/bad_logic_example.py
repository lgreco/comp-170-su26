# A broken first draft of the word-frequency counter, kept exactly as
# written -- bugs included -- as a worked example of what goes wrong.
# The corrected version lives in file_processing.py; this file exists
# only so the mistake stays visible instead of getting overwritten.
#
# The bug: is_unique starts False, meaning "haven't decided yet," but
# it's then used directly as the condition for continuing to search:
#     while i < len(contents) and is_unique:
# Since is_unique is False from the start, that condition is false
# immediately, so the search loop below never runs -- not once, for
# any word. i stays 0 and is_unique never changes, so the code always
# falls into the `else` branch and tries to update frequency[i-1],
# i.e. frequency[-1], on a still-empty list. The very first word
# processed crashes the program with an IndexError.
#
# The lesson: getting a loop's stopping condition backwards doesn't
# just break that loop -- it silently breaks every branch downstream
# that assumed the loop had actually run.

contents = []  # unique words in a file
frequency = []  # frequency[i] is the number of times contents[i] appears

file_to_process = "tale_of_two_cities.txt"

with open(file_to_process, 'r') as f:
    line = f.readline()
    while line is not None:  # line just read, not empty
        words = line.split()  # A list with the words of the current line
        # Consider every word in this line:
        for word in words:
            is_unique = False
            # Search through contents to see if word already there
            i = 0
            while i < len(contents) and is_unique:
                is_unique = contents[i] == word
                i += 1
            # When this while loop ends, it ends either because we did
            # not find `word` in `contents` or because we foud it
            # at index position `i-1`
            if is_unique:
                contents.append(word)
                frequency.append(1)
            else:
                frequency[i-1] = frequency[i-1] + 1  # same as frequency[i-1]+=1
        line = f.readline()

