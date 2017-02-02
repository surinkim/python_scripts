import sys

print('start!')

fname = 'server.dat'

try:
    f = open(fname, 'r')
except IOError:
    print('Could not read file.', fname)
    sys.exit()

with f:
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
