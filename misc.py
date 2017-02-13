
import time

# time example

#1970/01/01/0시 기준으로 지금까지 경과한 시간(초)
print('time.time() = %s' % time.time())

#세계 표준시
print('time.gmtime() = ', time.gmtime())

#지역 표준시
print('time.localtime()', time.localtime())

#문자열로 시간 변환
print('time.asctime() = %s' % time.asctime())

#지역 시간 문자열로 변환
print('time.ctime() = %s' % time.ctime())

#포맷 문자열
print('time.strftime = %s' % time.strftime('%Y/%m/%d'))
print('time.strftime = %s' % time.strftime('%Y-%m-%d:%H:%M:%S'))

#################################################################

## string example
url = 'www.dummy.net/%s/test.txt'
url = url % ('2015-01-11')
print(url)

url = 'www.dummy.net/%s/test.txt'
url = url % time.strftime('%Y-%m-%d')
print(url)

url = 'www.dummy.net\\test.txt\n'
print(url)

url = url + '123'
print(url)

url = 'www.dummy.net\\test.txt\n'
url = url.strip() + '123'
print(url)
