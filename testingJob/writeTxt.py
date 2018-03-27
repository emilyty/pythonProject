# -*- coding: utf-8 -*-
# @Author: emily
# @Date  : 2018/3/27 10:40
# @Contact : emilyty@163.com
# @Desc: 为了验证1W+会员数据的批量导入
import time
f = open('D:\BatchImport.txt', 'a')
try:
    for num in range(1,10000):
        t = time.time()
        nowtime = int(round(t*1000))
        f.write('删'+str(nowtime)+',删'+str(nowtime)+',入门会员,2018-12-12,100,2018-12-31,13800000000,1990-1-1,123@12.com,模板案例数据\n')
        time.sleep(0.001) #需要保证每个会员名称都不一样，所以适当的加了休息时间。
        num = num+1
except Exception as IOError:
    print('errors in writing files.')
finally:
    f.close()