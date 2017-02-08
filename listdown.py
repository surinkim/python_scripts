from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import urlretrieve
import os
import sys
import logging
import time
from logging.handlers import TimedRotatingFileHandler

# logger 인스턴스 생성 및 로그 레벨 설정#
logger = logging.getLogger("downloader")
logger.setLevel(logging.INFO)

# timehandler
timeHandler = TimedRotatingFileHandler('downloader.log', when='m', interval = 1, backupCount = 5)

# formmater 생성
formatter = logging.Formatter('[%(asctime)s %(levelname)s|%(filename)s:%(lineno)s] > %(message)s')

# fileHandler와 StreamHandler를 생성
#fileHandler = logging.FileHandler('downloader.log')
streamHandler = logging.StreamHandler()

# handler에 fommater 세팅
#fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
timeHandler.setFormatter(formatter)

# Handler를 logging에 추가
#logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.addHandler(timeHandler)

# 아래 urlretrieve 사용할 hook
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
        logger.debug('%s %% download.' % round(percentage))

logger.info('>>> Downloader start.')

# url 리스트가 있는 파일
readfile = 'server.dat'

try:
    f = open(readfile, 'r')

except IOError:
    logger.critical('Could not read file.', readfile)
    sys.exit()

lines = f.readlines()
f.close()

for url in lines:

    # url open validation 확인
    try:
        urlopen(url)

    except HTTPError as e:
        logger.error('Coud not open url = %s' % url)
        continue

    pathlist = url.split('/')
    filename = pathlist[-1].rstrip()
    date = pathlist[-2]
    ip = pathlist[-4]
 
    directory = ip + '/' + date
    fullpath = directory + '/' + filename

    logger.debug('directory = %s, fullpath = %s' % (directory, fullpath))

    if not os.path.exists(directory):
        os.makedirs(directory)

    logger.info('%s download start.' % fullpath)

    # 파일 다운로드
    fname, header = urlretrieve(url, fullpath, hook)
    logger.info('%s download end.' % fullpath)

logger.info('<<< Downloader end.')