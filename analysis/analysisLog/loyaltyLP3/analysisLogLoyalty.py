# _*_ coding:utf-8 _*_
# -*- coding: utf-8 -*-
# @Author: emily
# @Date  : 2018/3/20 13:52
# @Contact : emilyty@163.com
# @Desc: 安踏测试环境做忠诚度计算相关的性能测试时候，无法判断订单是否全部被处理完成。
# 为了解决这个问题，需要从日志里找出订单开始处理和处理完成的两断信息，如果关键信息出现了两次，那么认为已经处理完成。
# 如果没有出现关键信息或者不只出现两次，那么记录下来。

from log.Log import Log
import os
import time

log = Log()

#获取需要分析的全部关键字
def getKeyWord():
    for i in range(0,3):
        orderId  = "record:key:orderEventHandler/152885895197"+str(i)
        searchKeyWord(orderId)
        i += 1


#查询关键字是否存在两个
def searchKeyWord (keywords):
    filename = "C:/test/loyalty2-calc.log"
    word = keywords
    count = 0
    try:
        fobj = open(filename, 'r', encoding='UTF-8')
    except IOError as e:
        log.WriteLog("打开文件异常"+e)
    else:
        for keyword in fobj:
            if word in keyword:
                #print(keyword)
                count += 1
        if count ==2:
            pass
            #print(re.match('完成处理消息.' + word, keyword))
        else :
            writeFile('[事件处理错误]【' + word+'】一共出现：'+str(count)+'次')
    finally:
        fobj.close()

#写入文件
def writeFile(message,flag=False):
    strMessage = '\n' + time.strftime('%Y-%m-%d %H:%M:%S')
    if flag:
        strMessage += ': %s' % message
    else:
        strMessage += ':\n%s' % message

    fileName = os.path.join(os.getcwd(), 'log' + time.strftime('%Y-%m-%d') + '.txt')
    with open(fileName, 'a') as f:
        f.write(strMessage)


if __name__ == '__main__':
    getKeyWord()