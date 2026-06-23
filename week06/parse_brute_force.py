
def our_split(sentence: str, delimiter: str = " ") -> list[str]:

    current_box = 0
    output = list()
    new_entry = ''

    while current_box < len(sentence):

        current_char = sentence[current_box]

        if current_char == delimiter:
            # move to a new entry in the output
            output.append(new_entry)
            # reset new entry for next word
            new_entry = ""
        else:
            # copy the current char to the new entry
            new_entry = new_entry + current_char

        # move to the next box
        current_box += 1  # same as: current_box = current_box + 1

    # After the loop ends, add the current content of new_item
    # to the output
    output.append(new_entry)

    return output

if __name__ == "__main__":

    sentence = "it   was   the   best of times it was the worst of times"
    result = our_split(sentence)
    print(result)
    another_result = our_split(sentence, "i")
    print(another_result)
