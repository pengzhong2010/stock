import time
import os

def current_h():
    return int(time.strftime("%H", time.localtime()))

def current_m():
    return int(time.strftime("%M", time.localtime()))

def judge(h,m):
    if h < 9:
        return False
    if h == 9 and m < 15:
        return False
    if h == 11 and m > 35:
        return False
    if h == 12 and m < 55:
        return False
    if h == 15 and m > 5:
        return False
    if h > 15:
        return False
    return True

# print judge(9,14)
# print judge(9,16)
#
# print judge(11,34)
# print judge(11,36)
#
# print judge(12,54)
# print judge(12,56)
#
# print judge(15,4)
# print judge(15,6)


while judge(current_h(),current_m()) :
    os.system("scrapy crawl attention")
    time.sleep(1)