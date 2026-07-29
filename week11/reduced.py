def where_seen(word, collection):
    idx = -1
    i = 0
    while i < len(collection) and idx == -1:
        if collection[i] == word:
            idx = i
        i += 1
    return idx

def record(word, seen_before):
    if seen_before == -1:
        contents.append(word)
        frequency.append(1)
    else:
        frequency[seen_before] += 1

contents = []
frequency = []

file_to_process = "tale_of_two_cities.txt"

with open(file_to_process, 'r') as f:
    line = f.readline()
    while len(line) > 0:
        words = line.split()
        for word in words:
            w = where_seen(word, contents)
            record(word, w)
        line = f.readline()
