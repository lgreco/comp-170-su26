# A naive example for fileprocessing

contents = []  # unique words in a file
frequency = []  # frequency[i] is the number of times contents[i] appears

file_to_process = "tale_of_two_cities.txt"

with open(file_to_process, 'r') as f:
    line = f.readline()
    while line:  # line just read, not empty
        words = line.upper().split()  # A list with the words of the current line
        # Consider every word in this line:
        for word in words:
            # Search through contents to see if current word
            # has been encountered before
            i = 0
            found = False  # Assume not seen before
            while i < len(contents) and not found:
                found = contents[i] == word
                i = i + 1  # same as i += 1
            if found:
                frequency[i-1] = frequency[i-1] + 1  #  same += 1
            else:
                contents.append(word)
                frequency.append(1)
        line = f.readline()

