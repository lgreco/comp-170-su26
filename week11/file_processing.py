# A naive example for fileprocessing

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
                not_unique = contents[i] == word
                i += 1
            # When this while loop ends, it ends either because we did
            # not find `word` in `contents` or because we foud it
            # at index position `i-1`
            if not_unique:
                frequency[i-1] += 1
            else:
                contents.append(word)
                frequency.append(1)
        line = f.readline()

