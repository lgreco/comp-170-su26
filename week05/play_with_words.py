sentence = "The relentless summer heat in Chicago made even the sidewalks shimmer"

# Convert the sentence to individual words stored in a list
words = sentence.split()

# Length criterion
N = 4

output_list = []

for i in range(len(words)):
    if len(words[i]) > N:
        output_list.append(words[i].upper())

print(output_list)

