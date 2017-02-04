

# Generate input files
with open('file1.txt', 'w') as f:
    for i in range(25, 75, 3):
        f.write(str(i) + "\n")

with open('file2.txt', 'w') as f:
    for i in range(0, 100, 4):
        f.write(str(i) + "\n")


def get_next_line(lines):
    try:
        x = int(next(lines))
    except:
        x = None
    return x

# Input: file1 and file2 each have sequence of *sorted* numbers, one number per line
# Ouput: prints sequence of sorted
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2: 
    lines1 = (line for line in f1)   # generators: python is lazy, data still on disk!
    lines2 = (line for line in f2)

    x1 = None
    x2 = None

    while True:   # because lines1 and lines2 are (lazy) generators, only a 
                  # small amount of data is in memory at any point in time

        if x1 is None:
            x1 = get_next_line(lines1)
        if x2 is None:
            x2 = get_next_line(lines2)

        if x1 is None and x2 is None:
            break
        elif x1 is None:
            print x2
            x2 = None
        elif x2 is None:
            print x1
            x1 = None
        elif x1 < x2:
            print x1
            x1 = None
        else:
            print x2
            x2 = None
        
        
        
        
        
        