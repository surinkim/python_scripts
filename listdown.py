from urllib.request import urlretrieve
import os
import sys

hookCount = 0

def hook(blockNumber, blockSize, totalSize):
    #print('Downloading %s of %s' % (blockNumber * blockSize, totalSize))
    percentage = (blockNumber * blockSize * 100) / totalSize

    global hookCount 
    hookCount += 1

    if hookCount < 50 and percentage < 100:
        return
    else:
        hookCount = 0        
        print('%s %% download.' % round(percentage))

readfile = 'server.dat'

try:
    f = open(readfile, 'r')

except IOError:
    print('Could not read file.', readfile)
    sys.exit()

lines = f.readlines()
f.close()

for url in lines:

    pathlist = url.split('/')
    filename = pathlist[-1].rstrip()
    date = pathlist[-2]
    ip = pathlist[-4]
 
    directory = ip + '/' + date
    fullpath = directory + '/' + filename

    print('directory = %s, fullpath = %s' % (directory, fullpath))

    if not os.path.exists(directory):
        os.makedirs(directory)

    fname, header = urlretrieve(url, fullpath, hook)
    print('%s saved.' % fname)
