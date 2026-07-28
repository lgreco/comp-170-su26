# A naive example for fileprocessing

contents = []  # unique words in a file
frequency = []  # frequency[i] is the number of times contents[i] appears

file_to_process = "tale_of_two_cities.txt"

with open(file_to_process, 'r') as f:
    line = f.readline()
    while line is not None:  # line just read, not empty
        words = line.split()  # A list with the words of the current line

