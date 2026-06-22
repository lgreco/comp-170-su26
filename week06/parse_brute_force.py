def parse(sentence: str, delimiter: str = " ") -> list[str]:
    """Parses, by brute force, a string into tokens separated by a
    given delimiter character. This is what Python's built-in
    str.split(sep) does internally -- we are writing it by hand to
    see how it works.

    Inputs:
    -------
    sentence : str
      The string to break into tokens.
    delimiter : str
      The single character that separates tokens. Defaults to a
      space. If given the empty string, no splitting happens and
      sentence is returned as the only token.

    Returns
    -------
    A list of the tokens found in sentence, in order. Mirrors
    str.split(delimiter) exactly, including its edge cases:
      - consecutive delimiters produce empty-string tokens
      - a leading or trailing delimiter produces an empty-string
        token at that end
      - an empty sentence produces a list containing one empty
        string, e.g. parse("", ",") == [""]
    Note this is NOT the same as sentence.split() with no argument,
    which instead collapses runs of whitespace and drops empty
    tokens at the ends -- a different (and more forgiving) algorithm.

    Known bugs (left in on purpose):
    -------------------------------> real str.split(sep) accepts a
    multi-character sep and raises ValueError on sep="", whereas this
    function only matches a single-character delimiter (a longer
    delimiter just never matches, so the whole sentence comes back as
    one token) and silently returns [] instead of raising on an empty
    delimiter. We're leaving these mismatches alone because the point
    of this exercise is to illustrate how split() works, not to
    reproduce it exactly.
    """
    tokens = []

    if len(delimiter) > 0:
        token = ""          # the token currently being assembled
        current = 0         # index of the character we're looking at

        while current < len(sentence):
            character = sentence[current]
            if character == delimiter:
                # Found the delimiter: the token built so far is
                # complete, even if it's empty (that's how consecutive
                # delimiters produce empty tokens, just like real
                # split() does).
                tokens.append(token)
                token = ""
            else:
                # Not the delimiter: keep building the current token
                # one character at a time.
                token += character
            current += 1

        # There is no delimiter after the last token to trigger the
        # append above, so we always add it here -- even if it's
        # empty. This is what makes a trailing delimiter (or an empty
        # sentence) produce a trailing empty string, matching real
        # split(sep).
        tokens.append(token)

    return tokens


if __name__ == "__main__":
    sentence1 = "it was the best of times it was the worst of times"
    print(parse(sentence1))
    # Our brute-force version should match the built-in exactly.
    assert parse(sentence1) == sentence1.split(" ")

    sentence2 = "now is the winter of our discontent made glorious summer"
    print(parse(sentence2, "i"))
    assert parse(sentence2, "i") == sentence2.split("i")

    # Edge cases that reveal what split(sep) is really doing:
    print(parse("a,,b", ","))      # consecutive delimiters -> ['a', '', 'b']
    print(parse(",a,b,", ","))     # leading/trailing delim -> ['', 'a', 'b', '']
    print(parse("", ","))          # empty sentence -> ['']
