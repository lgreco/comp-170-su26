# A refactored version of the word-frequency counter from
# file_processing.py. The counting logic hasn't changed -- still two
# synchronized lists (contents and frequency), still a linear search,
# still split() on whitespace -- but it's now organized into two
# functions instead of one long top-level script. Read this file next
# to file_processing.py to see what packaging the same logic into
# functions buys you, and what it doesn't fix.

def search(list, target):
    # idx doubles as both "have we found it" and "where." In
    # file_processing.py those were two separate pieces of state: a
    # found flag, plus a loop counter i that the while loop always
    # left one step past the match, which is why that version had to
    # write frequency[i-1] instead of frequency[i] -- exactly the kind
    # of off-by-one that bad_logic_example.py got wrong in a different
    # way. Here, idx IS the answer: -1 means "not found," anything
    # else is the exact position of the match, so there's no separate
    # flag and no offset for the caller to remember.
    idx = -1
    # Guard clause: an empty list has nothing to search, and an empty
    # (falsy) target isn't a real word to search for, so skip the loop
    # entirely instead of running it and finding nothing.
    if list and target:
        i = 0
        # idx < 0 means "still haven't matched" -- once idx is set to
        # a real index (>= 0) the loop stops, the same way "found"
        # stopped the while loop in file_processing.py.
        while i < len(list) and idx < 0:
            if list[i] == target:
                idx = i
            i += 1
    return idx

def process(filename):
    # contents and frequency are local variables here, not
    # module-level globals sitting at the top of the script the way
    # they are in file_processing.py. That means process() can be
    # called again, on a different file, without one call's leftover
    # word counts bleeding into the next -- the global version can't
    # do that without being reset by hand first.
    contents = list()  # same as = []
    frequency = []  # same as = list()
    # Guard clause: skip straight to returning empty results instead
    # of letting open() blow up on a missing/empty filename.
    if filename:
        with open(filename, 'r') as book:
            line = book.readline()
            while len(line) > 0:
                words = line.split()
                for word in words:
                    # One call to search() replaces the entire inline
                    # while loop that sat here in file_processing.py.
                    idx = search(contents, word)
                    if idx == -1:
                        # New word, not previously encountered
                        contents.append(word)
                        frequency.append(1)
                    else:
                        # No i-1 bookkeeping needed: idx already
                        # points straight at the match, because
                        # search() hands back the position itself
                        # instead of a flag plus a counter left one
                        # step past it.
                        frequency[idx] += 1
                line = book.readline()
    # Returning the two lists -- instead of leaving them as globals
    # the rest of the script reaches into -- means the caller decides
    # what to do with them (print, test, pass along) without needing
    # to know process() used two synchronized lists internally. That's
    # the real payoff of wrapping this logic in a function: the
    # fragile array-synchronization technique from file_processing.py
    # is still here, still fragile, and still due to be replaced by a
    # dictionary -- but now it's fragile in exactly one place instead
    # of spread across a whole script.
    return contents, frequency
