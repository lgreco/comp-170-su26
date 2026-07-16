# Search for the substring "as" inside "bananas" using two nested
# loops, without relying on Python's built-in `in`/`.find()`.

in_string = "bananas"
sub_string = "as"

# Only start checking at positions where the rest of sub_string could
# still fit inside in_string -- stopping len(sub_string) - 1 positions
# early avoids stepping past the end of in_string in the inner loop.
for i in range(len(in_string) - len(sub_string) + 1):
    # A position is only worth checking further if its first letter
    # matches the first letter of what we're looking for.
    if in_string[i] == sub_string[0]:
        # Assume we have a match, then let each remaining letter
        # comparison confirm or deny it. Logical `and` combines them:
        # once one comparison is False, hope_for stays False no matter
        # what the rest say, and Python's `and` doesn't even bother
        # evaluating them once that happens.
        hope_for = True
        for j in range(1, len(sub_string)):
            hope_for = hope_for and (in_string[i + j] == sub_string[j])
        if hope_for:
            print(f"Found '{sub_string}' in '{in_string}' at position {i}")
