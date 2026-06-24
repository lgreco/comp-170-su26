
def our_split(sentence: str, delimiter: str = " ") -> list[str]:
    """
    Scan `sentence` one character at a time and split it into a list of words,
    using `delimiter` as the separator between words.

    This is a brute-force re-implementation of Python's built-in str.split().
    It exists to show how that method could be written from scratch using only
    a while loop, an index variable, and string concatenation.

    Known bug — multiple consecutive delimiters:
        Python's built-in split() treats any run of spaces as a single boundary:
            "a   b".split()  →  ['a', 'b']
        Our version sees each delimiter character individually, so each extra
        delimiter produces an empty string in the output:
            our_split("a   b")  →  ['a', '', '', 'b']
        Fixing this would require detecting when new_entry is already empty
        before appending it, or skipping repeated delimiters in a nested loop.
    """

    # current_box is our index — it points to the position we are examining
    # right now. We start at position 0 (the first character).
    current_box = 0

    # output is the list we are building up. It starts empty and grows
    # every time we finish reading a word.
    output = list()

    # new_entry holds the word we are currently assembling, one character
    # at a time. It resets to an empty string after each word is saved.
    new_entry = ''

    # Walk through every character in the sentence, left to right.
    while current_box < len(sentence):

        current_char = sentence[current_box]

        if current_char == delimiter:
            # We hit a boundary. The word we have been building is complete,
            # so save it to output and start a fresh word.
            #
            # Bug: if two delimiters appear in a row (e.g. two spaces), we
            # reach this branch again immediately with new_entry still equal
            # to "". That empty string gets appended as if it were a real word.
            output.append(new_entry)
            new_entry = ""          # reset for the next word
        else:
            # Regular character — glue it onto the end of the word in progress.
            new_entry = new_entry + current_char

        # Advance the index to the next character and repeat.
        current_box += 1  # same as: current_box = current_box + 1

    # The loop stops when current_box reaches len(sentence). At that point
    # the last word is still sitting in new_entry (there is no trailing
    # delimiter to trigger the append inside the loop), so we add it here.
    output.append(new_entry)

    return output


def our_parse_fix_1(sentence: str, delimiter: str = " ") -> list[str]:
    """
    Split `sentence` on `delimiter`, ignoring consecutive delimiters.

    Fix approach: before saving new_entry to output, check whether it is
    empty. An empty new_entry means we just saw another delimiter in a row,
    so there is no real word to save — we simply skip the append.
    The same guard is applied to the final append after the loop, which
    handles a trailing delimiter at the end of the sentence.
    """

    current_box = 0
    output = list()
    new_entry = ''

    while current_box < len(sentence):

        current_char = sentence[current_box]

        if current_char == delimiter:
            # Only save new_entry when it actually contains a word.
            # If new_entry is empty we hit two delimiters in a row,
            # so there is nothing real to add — we just reset and move on.
            if new_entry != "":
                output.append(new_entry)
                new_entry = ""
        else:
            new_entry = new_entry + current_char

        current_box += 1

    # Guard the final append the same way: a trailing delimiter leaves
    # new_entry empty, and we do not want a spurious empty string at the end.
    if new_entry != "":
        output.append(new_entry)

    return output


def our_parse_fix_2(sentence: str, delimiter: str = " ") -> list[str]:
    """
    Split `sentence` on `delimiter`, ignoring consecutive delimiters.

    Fix approach: when a delimiter is found, immediately advance the index
    past any additional delimiters that follow it using a nested while loop.
    By the time the outer loop resumes, current_box already points at the
    next real character, so no empty strings are ever built.
    """

    current_box = 0
    output = list()
    new_entry = ''

    while current_box < len(sentence):

        current_char = sentence[current_box]

        if current_char == delimiter:
            output.append(new_entry)
            new_entry = ""

            # Consume every additional delimiter that follows this one.
            # After this inner loop, sentence[current_box + 1] is either a
            # non-delimiter character or we are at the end of the sentence.
            # The outer loop's increment below will then land exactly on the
            # first real character of the next word.
            while current_box + 1 < len(sentence) and sentence[current_box + 1] == delimiter:
                current_box += 1
        else:
            new_entry = new_entry + current_char

        current_box += 1

    # After the loop the last word (if any) is still in new_entry.
    if new_entry != "":
        output.append(new_entry)

    return output


if __name__ == "__main__":

    sentence = "it   was   the   best of times it was the worst of times"

    print("original our_split (shows the bug):")
    print(our_split(sentence))

    print("\nour_parse_fix_1 (guard the append):")
    print(our_parse_fix_1(sentence))
    print(our_parse_fix_1(sentence, "i"))

    print("\nour_parse_fix_2 (nested loop skips extras):")
    print(our_parse_fix_2(sentence))
    print(our_parse_fix_2(sentence, "i"))
