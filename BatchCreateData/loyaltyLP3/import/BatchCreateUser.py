# -*- coding: utf-8 -*-
# @Author: emily
# @Date  : 2018/3/27 10:40
# @Contact : emilyty@163.com
# @Desc: 为了验证1W+会员数据的批量导入，测试
import time
f = open('C:/test/testBatchImport.txt', 'a+')
try:
    for num in range(0,3000):
        t = time.time()
        nowtime = int(round(t*1000))
        f.write('删'+str(nowtime)+',删'+str(nowtime)+',入门会员,2018-12-12,1,2018-12-31,13800000000,1990-1-1,123@12.com,模板案例数据\n')
        #给同一个用户造多条数据，例如给一个用户造1000条积分导入记录
        #f.write('201806041759,过期1759,2018-12-12,1,2018-12-31,13800000000,1990-1-1,123@12.com,模板案例数据\n')
        time.sleep(0.001) #需要保证每个会员名称都不一样，所以适当的加了休息时间。
        num = num+1
except Exception as IOError:
    print('errors in writing files.')
finally:
    f.close()