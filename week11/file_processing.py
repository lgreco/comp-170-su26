# A naive example for file processing: count how many times each word
# appears in a text file (the opening paragraphs of "A Tale of Two Cities").
#
# The words we've seen so far and their counts are kept in two separate
# lists, lined up position by position -- contents[i] and frequency[i]
# describe the same word. This is called "array synchronization," and
# it's deliberately used here even though it is NOT a safe technique:
# nothing enforces that the two lists stay in sync except our own care
# when writing the code below. It's easy to get right and just as easy
# to break (an off-by-one below very nearly did). We're using it once,
# on purpose, so the risk is visible, before replacing it with a
# dictionary -- a data structure built to hold exactly this kind of
# word-to-count relationship safely.

# contents holds the unique words in the file, in the order first seen.
contents = []
# frequency[i] is how many times contents[i] appears.
frequency = []

file_to_process = "tale_of_two_cities.txt"

with open(file_to_process, 'r') as f:
    line = f.readline()
    # len(line) > 0 rather than "line is not None": readline() never
    # returns None. At end of file it returns "" (an empty string),
    # which is falsy but not None, so checking against None caused an
    # infinite loop the first time this was written. Checking length
    # directly stops the loop exactly when there's nothing left to read.
    while len(line) > 0:
        # words is a list with the words of the current line.
        words = line.split()
        # Consider every word in this line:
        for word in words:
            # Search through contents to see if the current word
            # has already been counted. This is a linear search: start
            # at the front and stop as soon as we find a match or run
            # out of words to compare against.
            i = 0
            # found starts False: assume the word has not been seen before.
            found = False
            while i < len(contents) and not found:
                found = contents[i] == word
                # i = i + 1 is the same as i += 1.
                i = i + 1
            if found:
                # The while loop above always advances i one step past
                # the position where the match was found (that's what
                # let the loop stop), so the matching word -- and its
                # count -- is one position behind, at i - 1. Losing
                # track of that offset here is exactly the kind of
                # mistake array synchronization makes easy.
                # frequency[i-1] = frequency[i-1] + 1 is the same as
                # frequency[i-1] += 1.
                frequency[i-1] = frequency[i-1] + 1
            else:
                # Not found: this is the first time we've seen this
                # word, so it gets a new entry in both lists, at the
                # same new position, keeping them in sync.
                contents.append(word)
                frequency.append(1)
        line = f.readline()

# Known limitation: matching is case-sensitive, so "It" and "it" are
# currently counted as different words. Normalizing case (and later,
# stripping punctuation) is left for a future pass.
