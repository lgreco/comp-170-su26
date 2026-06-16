# Goal: take a sentence and collect every word that is longer than a given
# number of characters, converting each qualifying word to uppercase.
#
# In class we worked with the sentence below and a cutoff of 4 characters.
# We identified the qualifying words by hand first:
# relentless, summer, Chicago, sidewalks, shimmer — then wrote code to do it.
#
# The program demonstrates three ideas working together:
#   1. Strings are objects: sentence.split() breaks a string into a list of words.
#   2. Loops + conditions: iterate over the list, test each word's length.
#   3. Accumulator pattern: start with an empty list and append qualifying results.

sentence = "The relentless summer heat in Chicago made even the sidewalks shimmer"

# split() breaks a string on whitespace and returns a list of the individual words.
# After this line, words = ['The', 'relentless', 'summer', 'heat', 'in', 'Chicago',
#                           'made', 'even', 'the', 'sidewalks', 'shimmer']
words = sentence.split()

# N is the length threshold: only words *longer than* N characters will be kept.
# Changing N here changes the behavior of the entire program — a single point of control.
N = 4

# Start with an empty list; we will fill it one word at a time inside the loop.
output_list = []

# range(len(words)) produces the indices 0, 1, 2, … len(words)-1,
# so words[i] visits every word in order.
for word in words:
    # len(words[i]) counts the characters in the current word.
    # The condition is *strictly greater than* N, so a 4-letter word is excluded.
    if len(word) > N:
        # upper() returns a new string with every letter capitalised;
        # it does not modify words[i] itself.
        # append() adds that new string to the end of output_list.
        output_list.append(word.upper())

# Expected output: ['RELENTLESS', 'SUMMER', 'CHICAGO', 'SIDEWALKS', 'SHIMMER']
print(output_list)
