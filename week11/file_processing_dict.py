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

# DRUM ROLL ... INTRODUCING DICTIONARIES (AKA LOOK UP TABLES,
# AKA HASH TABLES, AKA KEY-VALUE PAIRS, AKA ASSOCIATE ARRAYS)

count = dict()  # same as: count = {}

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
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        line = f.readline()

# Known limitation: matching is case-sensitive, so "It" and "it" are
# currently counted as different words. Normalizing case (and later,
# stripping punctuation) is left for a future pass.
