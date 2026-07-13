in_string = "bananas"
sub_string = "as"


for i in range(len(in_string)):
    if in_string[i] == sub_string[0]:
        hope_for = True:
            for j in range(1,len(sub_string)):
                hope_for = hope_for and (in_string[i+j] == sub[j])
