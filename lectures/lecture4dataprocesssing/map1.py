import re

with open('small.txt', 'r') as f, open('nouns.txt', 'w') as f2:
    # f is an iterator over the lines of the file
    # almost all of the file is still on disk!
    for line in f:     # input: a stream of lines (lazily fetched from disk)
        words = line.split()
        for word in words:
            # if word starts with a capital letter... 
            # TODO: fill this in?
            m = re.match(r"([A-Z][a-z]+)", word)
            if m is not None:
                f2.write(m.group(1) + '\n')                
                # output: a stream of lines (one word per line)


# how much memory is being used by this program?
# ways we can improve our proper noun detector?