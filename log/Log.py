import os
import time
class Log:
    def __init__(self):
        pass

    def WriteLog(self,message,flag = False):
        strMessage = '\n' + time.strftime('%Y-%m-%d %H:%M:%S')
        if flag:
            strMessage += ': %s' % message
        else:
            strMessage += ':\n%s' % message

        fileName = os.path.join(os.getcwd(), 'log'+time.strftime('%Y-%m-%d')+ '.txt')
        with open(fileName, 'a') as f:
            f.write(strMessage)