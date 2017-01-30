from urllib.request import urlretrieve

hookCount = 0

def hook(blockNumber, blockSize, totalSize):
    #print('Downloading %s of %s' % (blockNumber * blockSize, totalSize))
    percentage = (blockNumber * blockSize * 100) / totalSize

    global hookCount 
    hookCount += 1

    if hookCount < 10 and percentage < 100:
        return
    else:
        hookCount = 0        
        print('%s %% download.' % round(percentage))

fname, header = urlretrieve('http://legacy.python.org/download/releases/binaries-1.5/python-doc-1.5-2.i386.rpm', 'test.rpm', hook)
print('%s saved.' % fname)

