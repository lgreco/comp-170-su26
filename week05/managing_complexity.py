def filter_words(sentence: str, cutoff_length: int) -> list[str]:
    """This method parses a sentence and returns words that exceed the
    specified cutoff_length.

    Inputs:
    -------
    sentence : str
      A string with a sentence that I will parse into words for
      further processing
    cutoff_length : int
      A length criterion to reject words whose length is <=

    Returns
    -------
    A list of words in the input sentence that are longer than the
    cutoff_length. These words are converted first into upper case.
    If no words match the criterion, the method returns an empty list.
    """
    # The method promised to return a list of strings.
    # Here is a trivial list of strings
    list_of_strings = []

    # First ensure that the input values are legit.
    # For example, if the input sentence is empty, skip to the output
    if len(sentence) > 0 and cutoff_length > -1 and cutoff_length < 100:
        # Now it's safe to parse the sentence into words and place them
        # into a list:
        words = sentence.split()
        # Process this list, one word at a time, to measure its lenght
        # and determine if it should be included in the output.
        for i in range(len(words)):
            current_word = words[i]
            current_word_length = len(current_word)
            # Check against the length criterion
            if current_word_length > cutoff_length:
                # Add this word to the output
                converted_current_word = current_word.upper()
                list_of_strings.append(converted_current_word)
    return list_of_strings


### NOT THE "PRO" WAY TO DO THINGS, BUT SIMPLER ANYWAY

if __name__ == "__main__":
    outcome = filter_words("it was the best of times it was the worst of times", 3)
    print(outcome)
