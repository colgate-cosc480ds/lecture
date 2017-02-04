import re
import sys

with sys.stdin as f, sys.stdout as f2:
    # f is an iterator over the lines of the file
    # most of the file is still on disk!
    last_word = None
    for line in f:     # input: a stream of lines (lazily fetched from disk)
        words = line.split()
        for word in words:
            # if word starts with a capital letter... 
            # output: a stream of lines (one word per line)
            f2.write(word + '\n')


# cat sherlock.txt | python map2.py | grep '^[A-Z][a-z]\+$'