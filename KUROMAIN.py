#记录：2019/11/25
#      进行KURO初代机的开发
#      版本：0.02
#      Vel：0.02  使用了EasyGUI库，进行鼠标操作
#      Vel: 0.03  取消使用EasyGUI,重归代码操作
#      Vel: 0.04  成功在kuro硬件上配置好环境，开始kuro正式开发
#      Vel: 0.05  成功编写天气爬虫
#      All Rights Belong To SK4 Project
import time
import os
from KUROINPRO import*
from KUROH import*

#测试部分
Authority = 0
Shut = 0
Weather = Weather()

Authority=Lock()#安全中心
if Authority==0:
    print('Sorry, You Have No Authority To Enter The System ')
else:
    pass

#本体开始
while(Authority):
    print('**************************************************\n')
    print('Welcome Back, Sir!\n')
    print('                                 ',(time.strftime("%Y-%m-%d %H:%M",time.localtime())))
    print(' ',Weather)
    print('**************************************************\n')
    InPut = input('Enter The Command:')
   #关闭模块
    Shut = InPutProcess(InPut)
    if Shut == 1:
        ShutDown()
        break
    else:
        pass